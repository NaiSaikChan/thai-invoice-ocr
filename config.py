import os
from pathlib import Path
from typing import Dict, List

# Base Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
TEMP_DIR = DATA_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"
MODEL_DIR = BASE_DIR / "models"

# Create directories if they don't exist
for directory in [INPUT_DIR, OUTPUT_DIR, TEMP_DIR, LOG_DIR, MODEL_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# OCR Configuration
OCR_CONFIG = {
    "tesseract_path": os.getenv("TESSERACT_PATH", None),  # Auto-detect or set via env
    "tesseract_config": {
        "thai": "--oem 3 --psm 6 -l tha",
        "english": "--oem 3 --psm 6 -l eng",
        "mixed": "--oem 3 --psm 6 -l tha+eng",
    },
    "confidence_threshold": 60,
    "use_easyocr": False,
}

# Image Processing Configuration
IMAGE_CONFIG = {
    "dpi": 300,
    "format": "PNG",
    "preprocessing": {
        "resize": True,
        "target_dpi": 300,
        "denoise": True,
        "deskew": True,
        "enhance_contrast": True,
        "binarize": True,
        "border_removal": True,
    },
    "deskew_threshold": 0.5,
}

# PDF Configuration
PDF_CONFIG = {
    "max_pages": 50,
    "max_file_size_mb": 100,
    "timeout_seconds": 300,
}

# Table Extraction Configuration
TABLE_CONFIG = {
    "method": "camelot",
    "min_confidence": 70,
    "detect_borderless": True,
}

# Data Extraction Configuration
EXTRACTION_CONFIG = {
    "invoice_patterns": {
        "invoice_number": [
            r"invoice\s*(?:no|number|#)?:?\s*(\S+)",
            r"เลขที่ใบกำกับภาษี:?\s*(\S+)",
            r"INV[-/]?\s*(\d+)",
        ],
        "date": [
            r"date:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
            r"วันที่:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
        ],
        "total": [
            r"total:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
            r"รวมทั้งสิ้น:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
            r"grand\s*total:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
        ],
        "tax": [
            r"tax:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
            r"VAT:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
            r"ภาษี:?\s*([฿$€£¥]?\s*[\d,]+\.?\d*)",
        ],
    },
    "required_fields": ["invoice_number", "date", "total"],
}

# Output Configuration
OUTPUT_CONFIG = {
    "formats": ["json", "csv", "excel"],
    "save_annotated_images": True,
    "save_intermediate_results": False,
}

# Logging Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(__asctime__)s [%(__levelname__)s] %(__name__)s: %(__message__)s"
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": str(LOG_DIR / "ocr_processing.log"),
            "formatter": "standard",
            "level": "INFO",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["file", "console"],
        "level": "INFO",
    },
}

# Error Codes
ERROR_CODES = {
    "E-001": "File not found",
    "E-002": "Invalid file format",
    "E-003": "Corrupted PDF",
    "E-004": "Password protected PDF without password",
    "E-005": "File too large",
    "E-101": "Image conversion failed",
    "E-102": "OCR engine error",
    "E-103": "Memory error",
    "E-104": "Timeout error",
    "E-201": "No text detected",
    "E-202": "Table extraction failed",
    "E-203": "Invalid data format",
    "E-204": "Missing required fields",
    "E-301": "Cannot write output file",
    "E-302": "Invalid output path",
    "E-303": "Disk space full",
}