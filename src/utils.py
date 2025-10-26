import logging
import logging.config
from pathlib import Path
from typing import Any, Dict, Optional
import json
from datetime import datetime
import config

def setup_logging():
    """Setup logging configuration"""
    logging.config.dictConfig(config.LOGGING_CONFIG)
    return logging.getLogger(__name__)

logger = setup_logging()

class OCRException(Exception):
    """Base exception for OCR errors"""
    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


def validate_file(file_path: str) -> bool:
    """
    Validate input file
    
    Args:
        file_path: Path to the file
        
    Returns:
        bool: True if valid
        
    Raises:
        OCRException: If file is invalid
    """
    path = Path(file_path)
    
    if not path.exists():
        raise OCRException(
            f"File not found: {file_path}",
            error_code="E-001"
        )
    
    if path.suffix.lower() not in ['.pdf']:
        raise OCRException(
            f"Invalid file format: {path.suffix}. Only PDF supported.",
            error_code="E-002"
        )
    
    file_size_mb = path.stat().st_size / (1024 * 1024)
    if file_size_mb > config.PDF_CONFIG["max_file_size_mb"]:
        raise OCRException(
            f"File too large: {file_size_mb:.2f}MB. Max: {config.PDF_CONFIG['max_file_size_mb']}MB",
            error_code="E-005"
        )
    
    logger.info(f"File validated: {file_path} ({file_size_mb:.2f}MB)")
    return True

def save_json(data: Dict, output_path: str) -> bool:
    """Save data as JSON"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"JSON saved: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to save JSON: {e}")
        raise OCRException(f"Cannot write output file: {e}", error_code="E-301")

def generate_output_filename(input_path: str, suffix: str, extension: str) -> str:
    """Generate output filename"""
    input_file = Path(input_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{input_file.stem}_{suffix}_{timestamp}.{extension}"

def calculate_confidence(scores: list) -> float:
    """Calculate average confidence score"""
    if not scores:
        return 0.0
    valid_scores = [s for s in scores if s is not None]
    return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0