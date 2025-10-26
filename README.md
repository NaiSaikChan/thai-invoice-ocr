# Thai-English Invoice OCR System

🚀 A powerful local Python OCR system for processing Thai and English invoices with PDF support, table extraction, and web interface.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## ✨ Features

- 📄 **Multi-format Support**: Process single or multi-page PDF invoices
- 🌏 **Dual Language**: Thai and English OCR with mixed-language support
- 📊 **Table Extraction**: Automatically detect and extract table data
- 🎯 **Smart Detection**: Invoice field extraction (number, date, amounts, line items)
- 🖼️ **Image Preprocessing**: Auto-enhancement, deskewing, noise reduction
- 💾 **Multiple Outputs**: JSON, CSV, and Excel formats
- 🌐 **Web Interface**: FastAPI-based REST API with upload UI
- 🐳 **Docker Ready**: Containerized deployment
- 🔒 **100% Local**: No internet required, complete privacy

## 🎯 Quick Start

### Prerequisites

- Python 3.8+
- Tesseract OCR 4.1.1+
- Poppler (for PDF conversion)

### Installation

#### Option 1: Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/NaiSaikChan/thai-invoice-ocr.git
cd thai-invoice-ocr

# Build and run with Docker
docker-compose up -d

# Access the web interface at http://localhost:8000
```

#### Option 2: Local Installation

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-tha tesseract-ocr-eng poppler-utils

# Clone and setup
git clone https://github.com/NaiSaikChan/thai-invoice-ocr.git
cd thai-invoice-ocr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**macOS:**
```bash
brew install tesseract tesseract-lang poppler

# Clone and setup
git clone https://github.com/NaiSaikChan/thai-invoice-ocr.git
cd thai-invoice-ocr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
1. Download Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install with Thai language pack
3. Add Tesseract to PATH
4. Clone and setup:
```bash
git clone https://github.com/NaiSaikChan/thai-invoice-ocr.git
cd thai-invoice-ocr
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Usage

### Command Line Interface

**Process a single invoice:**
```bash
python main.py process invoice.pdf
```

**Process with custom output:**
```bash
python main.py process invoice.pdf --output ./results
```

**Batch process multiple invoices:**
```bash
python main.py batch ./invoices_folder --output ./results
```

**Verbose mode:**
```bash
python main.py process invoice.pdf --verbose
```

### Web Interface

**Start the web server:**
```bash
python web/app.py
```

Then open http://localhost:8000 in your browser.

**API Endpoints:**
- `POST /api/process` - Upload and process invoice
- `POST /api/batch` - Batch upload
- `GET /api/status/{job_id}` - Check processing status
- `GET /api/results/{job_id}` - Get results

### Python API

```python
from src.invoice_processor import InvoiceProcessor

# Initialize processor
processor = InvoiceProcessor()

# Process invoice
result = processor.process_invoice("invoice.pdf")

# Access extracted data
print(result['invoice']['invoice_number'])
print(result['invoice']['total'])
print(result['invoice']['line_items'])
```

## 📁 Project Structure

```
thai-invoice-ocr/
├── src/
│   ├── pdf_handler/          # PDF processing
│   ├── image_processor/      # Image preprocessing
│   ├── layout_analyzer/      # Document layout detection
│   ├── ocr_engine/           # OCR processing
│   ├── table_extractor/      # Table extraction
│   ├── data_extractor/       # Invoice data extraction
│   ├── output_manager/       # Output formatting
│   ├── invoice_processor.py  # Main orchestrator
│   └── utils.py              # Utilities
├── web/
│   ├── app.py                # FastAPI application
│   ├── templates/            # HTML templates
│   └── static/               # CSS, JS files
├── tests/
│   ├── unit/                 # Unit tests
│   └── integration/          # Integration tests
├── data/
│   ├── input/                # Sample invoices
│   ├── output/               # Processed results
│   └── temp/                 # Temporary files
├── docs/                     # Documentation
├── config.py                 # Configuration
├── main.py                   # CLI entry point
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose
└── README.md                 # This file
```

## 🔧 Configuration

Edit `config.py` to customize:

- OCR settings (language, confidence threshold)
- Image preprocessing options
- PDF processing limits
- Output formats
- Extraction patterns

## 📊 Output Format

**JSON Example:**
```json
{
  "metadata": {
    "filename": "invoice_001.pdf",
    "processing_date": "2025-10-26T07:25:09Z",
    "page_count": 1,
    "processing_time_seconds": 3.2
  },
  "invoice": {
    "invoice_number": "INV-2025-001",
    "invoice_date": "2025-10-25",
    "total": 2140.00,
    "tax_amount": 140.00,
    "currency": "THB",
    "vendor": {
      "name": "ABC Company Ltd.",
      "tax_id": "0123456789012"
    },
    "line_items": [
      {
        "description": "Product A",
        "quantity": 10,
        "unit_price": 100.00,
        "total": 1000.00
      }
    ]
  }
}
```

## 🧪 Testing

Run tests:
```bash
# All tests
pytest

# Unit tests only
pytest tests/unit/

# With coverage
pytest --cov=src tests/
```

## 📈 Performance

- Single page: < 5 seconds
- 10-page invoice: < 30 seconds
- Batch (100 invoices): < 5 minutes
- Memory usage: < 2GB

## 🔍 Accuracy

- Printed Thai text: > 90%
- Printed English text: > 95%
- Mixed language: > 90%
- Table extraction: > 90%

## 🛠️ Troubleshooting

**Issue: Tesseract not found**
- Solution: Install Tesseract or set path in config.py

**Issue: Low accuracy for Thai**
- Solution: Ensure Thai language pack is installed
```bash
sudo apt-get install tesseract-ocr-tha
```

**Issue: Memory error**
- Solution: Reduce DPI in config.py or process fewer pages at once

**Issue: Table detection fails**
- Solution: Enable all preprocessing options and adjust table detection parameters

## 📚 Documentation

- [Product Requirements Document (PRD)](docs/PRD_Thai_English_Invoice_OCR.md)
- [Technical Implementation Guide](docs/TECHNICAL_IMPLEMENTATION_GUIDE.md)
- [Quick Start Guide](docs/QUICKSTART_GUIDE.md)
- [API Documentation](docs/API_DOCUMENTATION.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [pdf2image](https://github.com/Belval/pdf2image)
- [OpenCV](https://opencv.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

## 📧 Contact

Project Link: [https://github.com/NaiSaikChan/thai-invoice-ocr](https://github.com/NaiSaikChan/thai-invoice-ocr)

## 🗺️ Roadmap

- [ ] Add support for more languages (Chinese, Japanese)
- [ ] Machine learning-based field detection
- [ ] Automatic template learning
- [ ] Mobile app
- [ ] Cloud deployment option
- [ ] Real-time processing
- [ ] Integration with accounting software

---

Made with ❤️ by NaiSaikChan
