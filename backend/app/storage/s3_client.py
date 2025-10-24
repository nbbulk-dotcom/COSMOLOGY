
"""
S3 storage client for managing audit logs and artifacts.
Compatible with both MinIO (local) and AWS S3 (production).
"""
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from typing import BinaryIO, Optional, Dict
import structlog
import json

from app.config import settings

logger = structlog.get_logger()


class S3Client:
    """
    S3-compatible storage client.
    Handles file uploads, downloads, and JSONL append operations.
    """
    
    def __init__(self):
        """Initialize S3 client with configuration from settings."""
        self.client = boto3.client(
            's3',
            endpoint_url=settings.S3_ENDPOINT_URL,
            aws_access_key_id=settings.S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.S3_SECRET_ACCESS_KEY,
            region_name=settings.S3_REGION,
            config=Config(signature_version='s3v4')
        )
        self.bucket = settings.S3_BUCKET_NAME
        self._ensure_bucket()
    
    def _ensure_bucket(self):
        """Create bucket if it doesn't exist."""
        try:
            self.client.head_bucket(Bucket=self.bucket)
            logger.info("S3 bucket exists", bucket=self.bucket)
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                try:
                    self.client.create_bucket(Bucket=self.bucket)
                    logger.info("Created S3 bucket", bucket=self.bucket)
                except Exception as create_error:
                    logger.error("Failed to create S3 bucket", error=str(create_error))
            else:
                logger.error("S3 bucket check failed", error=str(e))
    
    def upload_file(
        self,
        file_obj: BinaryIO,
        key: str,
        metadata: Optional[Dict] = None
    ) -> bool:
        """
        Upload file object to S3.
        
        Args:
            file_obj: File-like object to upload
            key: S3 object key (path)
            metadata: Optional metadata dict
            
        Returns:
            True if successful, False otherwise
        """
        try:
            extra_args = {}
            if metadata:
                extra_args['Metadata'] = metadata
            
            self.client.upload_fileobj(file_obj, self.bucket, key, ExtraArgs=extra_args)
            logger.info("Uploaded file to S3", key=key, bucket=self.bucket)
            return True
        except Exception as e:
            logger.error("Failed to upload file to S3", key=key, error=str(e))
            return False
    
    def download_file(self, key: str) -> Optional[bytes]:
        """
        Download file from S3.
        
        Args:
            key: S3 object key (path)
            
        Returns:
            File contents as bytes, or None if failed
        """
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
            return response['Body'].read()
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                logger.warning("S3 key not found", key=key)
            else:
                logger.error("Failed to download file from S3", key=key, error=str(e))
            return None
    
    def upload_json(self, data: Dict, key: str) -> bool:
        """
        Upload JSON data to S3.
        
        Args:
            data: Dictionary to serialize as JSON
            key: S3 object key (path)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=json.dumps(data, indent=2).encode('utf-8'),
                ContentType='application/json'
            )
            logger.info("Uploaded JSON to S3", key=key)
            return True
        except Exception as e:
            logger.error("Failed to upload JSON to S3", key=key, error=str(e))
            return False
    
    def append_jsonl(self, data: Dict, key: str) -> bool:
        """
        Append JSONL entry to file (for audit logs).
        
        Args:
            data: Dictionary to append as JSON line
            key: S3 object key (path)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            entry = json.dumps(data) + '\n'
            
            # Try to download existing file
            existing = self.download_file(key)
            if existing:
                content = existing.decode('utf-8') + entry
            else:
                content = entry
            
            # Upload updated content
            self.client.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=content.encode('utf-8'),
                ContentType='application/x-ndjson'
            )
            logger.debug("Appended JSONL entry", key=key)
            return True
        except Exception as e:
            logger.error("Failed to append JSONL", key=key, error=str(e))
            return False
    
    def list_objects(self, prefix: str = "") -> list:
        """
        List objects in bucket with given prefix.
        
        Args:
            prefix: Object key prefix to filter by
            
        Returns:
            List of object keys
        """
        try:
            response = self.client.list_objects_v2(Bucket=self.bucket, Prefix=prefix)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            return []
        except Exception as e:
            logger.error("Failed to list S3 objects", prefix=prefix, error=str(e))
            return []


# Global S3 client instance
s3_client = S3Client()
