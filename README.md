# Product Requirements Document (PRD)
# Thai-English Invoice OCR System

**Version:** 1.0  
**Date:** 2025-10-26  
**Project Owner:** NaiSaikChan  
**Document Status:** Draft

---

## 1. Executive Summary

### 1.1 Project Overview
A local, offline-capable Python-based OCR system designed to extract structured and unstructured data from complex Thai and English invoices in PDF format.

### 1.2 Business Goals
- Automate invoice data extraction process
- Support both Thai and English languages
- Handle complex invoice layouts (forms, tables, plain text)
- Process multi-page PDF documents
- Run completely offline for data security
- Achieve >95% accuracy for printed text

### 1.3 Success Metrics
- OCR accuracy: >95% for clear invoices
- Processing speed: <5 seconds per page
- Support for 10+ common invoice formats
- Table detection accuracy: >90%
- Error rate: <5%

---

## 2. Product Requirements

### 2.1 Functional Requirements

#### FR-1: PDF Processing
- **FR-1.1**: Accept PDF files as input (single or multi-page)
- **FR-1.2**: Convert PDF pages to high-quality images
- **FR-1.3**: Handle encrypted PDFs with password support
- **FR-1.4**: Support PDF resolution up to 300 DPI

#### FR-2: OCR Capabilities
- **FR-2.1**: Recognize Thai language text (UTF-8)
- **FR-2.2**: Recognize English language text
- **FR-2.3**: Support mixed Thai-English documents
- **FR-2.4**: Handle various fonts and font sizes
- **FR-2.5**: Process handwritten text (optional, lower accuracy)

#### FR-3: Layout Detection
- **FR-3.1**: Detect and identify different regions (header, body, footer)
- **FR-3.2**: Identify table structures
- **FR-3.3**: Distinguish between form fields and values
- **FR-3.4**: Detect logos and images (skip OCR for these)
- **FR-3.5**: Maintain reading order (top-to-bottom, left-to-right)

#### FR-4: Table Extraction
- **FR-4.1**: Detect table boundaries
- **FR-4.2**: Identify rows and columns
- **FR-4.3**: Extract table data into structured format (CSV/JSON)
- **FR-4.4**: Handle merged cells
- **FR-4.5**: Support borderless tables

#### FR-5: Data Extraction
- **FR-5.1**: Extract key invoice fields:
  - Invoice number
  - Date
  - Vendor/Supplier name
  - Customer name
  - Total amount
  - Tax amount
  - Line items (description, quantity, unit price, total)
  - Payment terms
- **FR-5.2**: Output data in structured format (JSON, CSV, Excel)
- **FR-5.3**: Preserve original text formatting where applicable

#### FR-6: Image Preprocessing
- **FR-6.1**: Automatic image enhancement (contrast, brightness)
- **FR-6.2**: Deskewing (straighten rotated images)
- **FR-6.3**: Noise reduction
- **FR-6.4**: Binarization for better OCR accuracy
- **FR-6.5**: Resolution upscaling for low-quality scans

#### FR-7: Error Handling
- **FR-7.1**: Validate input file format
- **FR-7.2**: Handle corrupted PDFs gracefully
- **FR-7.3**: Log errors with detailed messages
- **FR-7.4**: Provide confidence scores for OCR results
- **FR-7.5**: Flag low-confidence extractions for manual review

#### FR-8: Output Management
- **FR-8.1**: Save extracted data to multiple formats (JSON, CSV, Excel)
- **FR-8.2**: Generate processing reports
- **FR-8.3**: Save annotated images with detected regions
- **FR-8.4**: Batch processing support

### 2.2 Non-Functional Requirements

#### NFR-1: Performance
- Process single page in <5 seconds
- Support batch processing of 100+ invoices
- Memory usage <2GB for typical invoice

#### NFR-2: Reliability
- 99% uptime for processing service
- Automatic recovery from processing errors
- Data integrity validation

#### NFR-3: Usability
- Command-line interface (CLI)
- Clear documentation
- Progress indicators for batch processing
- Informative error messages

#### NFR-4: Maintainability
- Modular code architecture
- Comprehensive logging
- Unit test coverage >80%
- Well-documented code

#### NFR-5: Security
- Run completely offline (no internet required)
- No data transmission to external services
- Secure file handling

#### NFR-6: Compatibility
- Python 3.8+
- Cross-platform (Windows, macOS, Linux)
- Support common PDF versions (1.4 - 2.0)

---

## 3. Technical Architecture

### 3.1 Technology Stack

#### Core Libraries
- **Tesseract OCR**: OCR engine with Thai language support
- **pytesseract**: Python wrapper for Tesseract
- **pdf2image**: PDF to image conversion
- **Pillow (PIL)**: Image processing
- **OpenCV**: Advanced image preprocessing
- **pandas**: Data manipulation
- **numpy**: Numerical operations

#### Optional/Advanced Libraries
- **easyocr**: Alternative OCR engine with better Thai support
- **paddleocr**: Advanced OCR with layout analysis
- **camelot-py** or **tabula-py**: Table extraction
- **pdfplumber**: Alternative PDF text extraction
- **layoutparser**: Document layout analysis
- **scikit-image**: Advanced image processing

### 3.2 System Architecture

```
┌─────────────────┐
│   PDF Input     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PDF Processor  │
│  - Page Split   │
│  - Convert to   │
│    Images       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Image Processor │
│  - Preprocessing│
│  - Enhancement  │
│  - Deskewing    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Layout Analyzer │
│  - Region Det.  │
│  - Table Det.   │
│  - Zone Class.  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   OCR Engine    │
│  - Thai OCR     │
│  - English OCR  │
│  - Mixed Text   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Data Extractor │
│  - Field Detect │
│  - Table Parse  │
│  - Validation   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Output Handler │
│  - JSON         │
│  - CSV          │
│  - Excel        │
└─────────────────┘
```

### 3.3 Module Design

#### Module 1: PDF Handler (`pdf_handler.py`)
- Load PDF files
- Extract pages
- Convert pages to images
- Handle password-protected PDFs

#### Module 2: Image Preprocessor (`image_preprocessor.py`)
- Image enhancement
- Noise reduction
- Deskewing
- Binarization
- Resolution adjustment

#### Module 3: Layout Analyzer (`layout_analyzer.py`)
- Detect document regions
- Identify tables
- Classify zones (header, body, footer)
- Determine reading order

#### Module 4: OCR Engine (`ocr_engine.py`)
- Perform OCR on image regions
- Support Thai and English
- Return text with confidence scores
- Handle multiple OCR engines

#### Module 5: Table Extractor (`table_extractor.py`)
- Detect table boundaries
- Identify rows and columns
- Extract cell data
- Convert to structured format

#### Module 6: Data Extractor (`data_extractor.py`)
- Parse invoice fields
- Apply business rules
- Validate extracted data
- Structure output

#### Module 7: Output Manager (`output_manager.py`)
- Format output (JSON, CSV, Excel)
- Generate reports
- Save annotated images
- Logging

#### Module 8: Utils (`utils.py`)
- Configuration management
- Logging setup
- Error handling
- File operations

---

## 4. Detailed Workflow

### 4.1 Processing Pipeline

```
Step 1: Input Validation
├─ Check file exists
├─ Verify PDF format
├─ Check file size
└─ Validate permissions

Step 2: PDF Conversion
├─ Load PDF
├─ Extract page count
├─ Convert each page to image (300 DPI)
└─ Store images temporarily

Step 3: Image Preprocessing
├─ Grayscale conversion
├─ Noise reduction (Gaussian blur)
├─ Contrast enhancement (CLAHE)
├─ Deskewing (Hough transform)
├─ Binarization (Otsu's method)
└─ Border removal

Step 4: Layout Analysis
├─ Detect text regions (contours)
├─ Identify table areas (line detection)
├─ Classify regions (ML/rule-based)
├─ Sort regions by reading order
└─ Generate region masks

Step 5: OCR Processing
├─ For each region:
│  ├─ Apply appropriate OCR (Thai/English)
│  ├─ Get text and confidence score
│  └─ Store with coordinates
└─ Combine results

Step 6: Table Processing
├─ Extract table regions
├─ Detect grid lines
├─ Identify cells
├─ Apply OCR to each cell
└─ Structure as DataFrame

Step 7: Data Extraction
├─ Apply regex patterns for fields
├─ Extract invoice metadata
├─ Parse line items
├─ Calculate totals
└─ Validate data

Step 8: Post-Processing
├─ Clean text (remove artifacts)
├─ Normalize values
├─ Apply business rules
└─ Flag low-confidence items

Step 9: Output Generation
├─ Format as JSON/CSV/Excel
├─ Generate processing report
├─ Save annotated images
└─ Log results

Step 10: Cleanup
├─ Remove temporary files
├─ Close file handles
└─ Free memory
```

### 4.2 Algorithm Details

#### A. Image Deskewing Algorithm
```
1. Convert image to grayscale
2. Apply edge detection (Canny)
3. Detect lines using Hough transform
4. Calculate dominant angle
5. If angle > threshold:
   - Rotate image to correct angle
6. Crop to remove black borders
```

#### B. Table Detection Algorithm
```
1. Preprocessing:
   - Binarize image
   - Invert colors
   
2. Line Detection:
   - Detect horizontal lines (morphology)
   - Detect vertical lines (morphology)
   
3. Grid Detection:
   - Find intersections
   - Identify cells
   
4. Table Extraction:
   - Crop table region
   - Extract cell coordinates
   - Apply OCR to each cell
   - Build structured table
```

#### C. Invoice Field Extraction Algorithm
```
1. Text Preprocessing:
   - Remove extra whitespace
   - Normalize encoding
   
2. Pattern Matching:
   - Invoice Number: Regex patterns
   - Date: Date parsing
   - Amount: Number extraction with currency
   
3. Contextual Extraction:
   - Find key labels (e.g., "Total:", "รวม:")
   - Extract value to the right/below
   
4. Validation:
   - Check format validity
   - Verify calculations
   - Flag inconsistencies
```

#### D. Confidence Scoring
```
1. OCR Confidence: From Tesseract (0-100)
2. Field Confidence:
   - High (90-100): Clear pattern match
   - Medium (70-89): Partial match
   - Low (<70): No clear match
3. Overall Confidence: Weighted average
```

---

## 5. Error Handling Strategy

### 5.1 Error Categories

#### Category 1: Input Errors
- **E-001**: File not found
- **E-002**: Invalid file format
- **E-003**: Corrupted PDF
- **E-004**: Password-protected (no password provided)
- **E-005**: File too large

**Handling**: Return clear error message, suggest fix, log error

#### Category 2: Processing Errors
- **E-101**: Image conversion failed
- **E-102**: OCR engine error
- **E-103**: Memory error
- **E-104**: Timeout

**Handling**: Retry with fallback options, log detailed error, continue with partial results

#### Category 3: Data Errors
- **E-201**: No text detected
- **E-202**: Table extraction failed
- **E-203**: Invalid data format
- **E-204**: Missing required fields

**Handling**: Flag for manual review, provide partial results, log warnings

#### Category 4: Output Errors
- **E-301**: Cannot write output file
- **E-302**: Invalid output path
- **E-303**: Disk space full

**Handling**: Try alternative location, notify user, preserve in-memory results

### 5.2 Error Handling Patterns

```python
# Pattern 1: Try-Except with Fallback
try:
    result = primary_method()
except Exception as e:
    log_error(e)
    result = fallback_method()

# Pattern 2: Validation with Early Return
if not validate_input(file):
    return error_response("Invalid input", code="E-002")

# Pattern 3: Retry with Exponential Backoff
for attempt in range(max_retries):
    try:
        return process()
    except TransientError:
        time.sleep(2 ** attempt)
        
# Pattern 4: Partial Success Handling
results = []
errors = []
for item in items:
    try:
        results.append(process(item))
    except Exception as e:
        errors.append((item, e))
return results, errors
```

---

## 6. Data Models

### 6.1 Invoice Data Structure (JSON)

```json
{
  "metadata": {
    "filename": "invoice_001.pdf",
    "processing_date": "2025-10-26T05:23:59Z",
    "page_count": 2,
    "ocr_engine": "tesseract",
    "processing_time_seconds": 4.5,
    "overall_confidence": 87.5
  },
  "invoice": {
    "invoice_number": "INV-2025-001",
    "invoice_date": "2025-10-25",
    "due_date": "2025-11-25",
    "currency": "THB",
    "confidence": {
      "invoice_number": 95,
      "invoice_date": 92,
      "due_date": 88
    }
  },
  "vendor": {
    "name": "ABC Company Ltd.",
    "address": "123 Bangkok Road, Bangkok 10100",
    "tax_id": "0123456789012",
    "phone": "+66-2-123-4567",
    "confidence": 89
  },
  "customer": {
    "name": "XYZ Corporation",
    "address": "456 Sukhumvit Road, Bangkok 10110",
    "tax_id": "9876543210987",
    "confidence": 91
  },
  "line_items": [
    {
      "item_number": 1,
      "description": "Product A",
      "quantity": 10,
      "unit_price": 100.00,
      "total": 1000.00,
      "confidence": 93
    },
    {
      "item_number": 2,
      "description": "Product B (ผลิตภัณฑ์ บี)",
      "quantity": 5,
      "unit_price": 200.00,
      "total": 1000.00,
      "confidence": 88
    }
  ],
  "summary": {
    "subtotal": 2000.00,
    "tax_rate": 7,
    "tax_amount": 140.00,
    "total": 2140.00,
    "confidence": 94
  },
  "payment_terms": "Net 30",
  "notes": "Thank you for your business",
  "raw_text": "Full OCR text...",
  "warnings": [
    "Low confidence on line item 2 description"
  ]
}
```

---

## 7. Implementation Phases

### Phase 1: Foundation (Week 1-2)
- ✅ Setup project structure
- ✅ Install dependencies
- ✅ Implement PDF to image conversion
- ✅ Basic image preprocessing
- ✅ Simple OCR (English only)

### Phase 2: Thai Language Support (Week 3)
- ✅ Install Thai language data for Tesseract
- ✅ Test Thai OCR accuracy
- ✅ Implement mixed language detection
- ✅ Tune OCR parameters

### Phase 3: Layout Analysis (Week 4-5)
- ✅ Implement region detection
- ✅ Table detection algorithm
- ✅ Reading order determination
- ✅ Zone classification

### Phase 4: Data Extraction (Week 6-7)
- ✅ Invoice field extraction
- ✅ Table parsing
- ✅ Validation logic
- ✅ Confidence scoring

### Phase 5: Error Handling & Optimization (Week 8)
- ✅ Comprehensive error handling
- ✅ Performance optimization
- ✅ Memory management
- ✅ Logging implementation

### Phase 6: Testing & Documentation (Week 9-10)
- ✅ Unit tests
- ✅ Integration tests
- ✅ User documentation
- ✅ API documentation

---

## 8. Testing Strategy

### 8.1 Test Cases

#### TC-1: Basic Functionality
- **TC-1.1**: Single page Thai invoice
- **TC-1.2**: Single page English invoice
- **TC-1.3**: Multi-page mixed invoice
- **TC-1.4**: Invoice with tables
- **TC-1.5**: Invoice with forms

#### TC-2: Edge Cases
- **TC-2.1**: Low quality scan (150 DPI)
- **TC-2.2**: Rotated invoice
- **TC-2.3**: Skewed invoice
- **TC-2.4**: Invoice with watermark
- **TC-2.5**: Handwritten annotations

#### TC-3: Error Conditions
- **TC-3.1**: Corrupted PDF
- **TC-3.2**: Empty PDF
- **TC-3.3**: Image-based PDF (no text layer)
- **TC-3.4**: Very large file (>50MB)

### 8.2 Performance Benchmarks
- Single page processing: <5 seconds
- 10-page invoice: <30 seconds
- 100 invoice batch: <5 minutes
- Memory usage: <2GB

---

## 9. Dependencies & Requirements

### 9.1 System Requirements
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 20.04+
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB for libraries, 10GB for temp files
- **Tesseract**: Version 4.1.1 or higher

### 9.2 Python Dependencies
See `requirements.txt` in technical documentation

---

## 10. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Low OCR accuracy for Thai | High | Medium | Use multiple OCR engines, manual review |
| Complex table structures | High | High | Implement multiple table detection algorithms |
| Performance issues | Medium | Medium | Optimize algorithms, use multiprocessing |
| Memory overflow | Medium | Low | Stream processing, chunking |
| Tesseract installation issues | Low | Medium | Provide detailed setup guide |

---

## 11. Future Enhancements

### Version 2.0
- ✨ Web interface (Flask/FastAPI)
- ✨ Database integration
- ✨ Machine learning for field classification
- ✨ Support for more languages (Chinese, Japanese)
- ✨ Real-time processing API

### Version 3.0
- ✨ Deep learning-based OCR
- ✨ Automatic invoice template learning
- ✨ Cloud deployment option
- ✨ Mobile app

---

## 12. Glossary

- **OCR**: Optical Character Recognition
- **DPI**: Dots Per Inch (resolution)
- **Binarization**: Converting image to black and white
- **Deskewing**: Straightening a tilted image
- **CLAHE**: Contrast Limited Adaptive Histogram Equalization
- **Tesseract**: Open-source OCR engine
- **UTF-8**: Unicode character encoding

---

## 13. Appendix

### A. Sample Invoices for Testing
- Thai tax invoice
- English commercial invoice
- Mixed Thai-English invoice
- Multi-page invoice with tables
- Complex form-based invoice

### B. References
- Tesseract Documentation: https://tesseract-ocr.github.io/
- Thai Language Support: https://github.com/tesseract-ocr/tessdata
- OpenCV Documentation: https://docs.opencv.org/

---

**Document Approval**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | NaiSaikChan | 2025-10-26 | |
| Developer | TBD | | |
| QA Lead | TBD | | |
