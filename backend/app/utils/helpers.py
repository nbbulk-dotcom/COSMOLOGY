
"""
Utility functions and helpers.
"""
import hashlib
from typing import Any
import json


def compute_sha256(data: str) -> str:
    """
    Compute SHA256 hash of string data.
    
    Args:
        data: String to hash
        
    Returns:
        Hexadecimal hash string
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def compute_sha256_bytes(data: bytes) -> str:
    """
    Compute SHA256 hash of bytes data.
    
    Args:
        data: Bytes to hash
        
    Returns:
        Hexadecimal hash string
    """
    return hashlib.sha256(data).hexdigest()


def serialize_json(data: Any) -> str:
    """
    Serialize data to JSON string with consistent formatting.
    
    Args:
        data: Data to serialize
        
    Returns:
        JSON string
    """
    return json.dumps(data, sort_keys=True, ensure_ascii=False)


def generate_retrieval_id(slug: str, version: str, chunk_id: int) -> str:
    """
    Generate standard retrieval ID format.
    
    Args:
        slug: Work slug
        version: Work version
        chunk_id: Chunk ID
        
    Returns:
        Retrieval ID in format "slug:version:chunk_id"
    """
    return f"{slug}:{version}:{chunk_id}"


def parse_retrieval_id(retrieval_id: str) -> tuple:
    """
    Parse retrieval ID into components.
    
    Args:
        retrieval_id: Retrieval ID string
        
    Returns:
        Tuple of (slug, version, chunk_id)
    """
    parts = retrieval_id.split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid retrieval ID format: {retrieval_id}")
    return parts[0], parts[1], int(parts[2])
