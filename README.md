# PDF Keyword Index Generator

## Overview

This Python script extracts and indexes keywords from PDF documents. It scans through a specified PDF file to identify occurrences of predefined keywords and generates an organized report showing which pages contain each keyword. The script is particularly useful for quickly navigating large technical documents, research papers, or reference manuals.

## Features

- **Keyword indexing**: Scans PDF documents for specific keywords and records the page numbers where each appears
- **Multi-word support**: Properly handles both single-word and multi-word phrases with flexible spacing
- **Page exclusion**: Allows specific pages to be excluded from analysis (e.g., references, appendices)
- **Progress reporting**: Shows real-time progress indicators during processing
- **Comprehensive output**: Generates a text report containing found and not-found keywords
- **Error handling**: Robust error checking for file access and text extraction issues

## Requirements

- Python 3.6+
- PyPDF2 library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mihir-28/PDFKeyWordMapper.git
   cd PDFKeyWordMapper
   ```

2. Install the required dependencies:
   ```
   pip install PyPDF2
   ```

## Usage

1. Place your PDF file in the same directory as the script or provide the correct path in the script.

2. Edit the `pdf_path` variable in the script to point to your PDF file:
   ```python
   pdf_path = "path/to/your/file"
   ```

3. Customize the list of `extended_keywords` to include terms relevant to your document.

4. If needed, update the `pages_to_skip` list to exclude specific pages from analysis:
   ```python
   # For individual pages: [1, 5, 9]
   # For page ranges: list(range(37, 100)) + list(range(122, 126))
   pages_to_skip = []

5. Run the script:
   ```
   python keywords.py
   ```

6. Check the generated keywords_index.txt file for results.

## Output Format

The output file keywords_index.txt contains:

```
Keyword Index Results:
Document: your_document.pdf
Total pages: 125
Pages skipped: 122, 123, 124, 125

FOUND KEYWORDS:
Authentication: 15, 42, 87
Blockchain: 3, 8, 10, 12, 45, 67
React: 56, 78, 92
...

NOT FOUND KEYWORDS:
ABI
Cloud Functions
...
```

## Configuration Options

You can easily customize the script by modifying:

- `pdf_path`: Path to the PDF file to analyze
- `pages_to_skip`: List of page numbers to exclude from analysis
- `extended_keywords`: List of keywords to search for

## How It Works

1. The script opens and validates the specified PDF file
2. It iterates through each page, extracting text content
3. For each page, it searches for all keywords in the predefined list
4. Single-word keywords use word boundary regex matching for accuracy
5. Multi-word phrases use flexible spacing pattern matching
6. Found keywords and their page numbers are compiled into a dictionary
7. Results are written to an output file with statistics

## Advanced Pattern Matching

The script uses regular expressions with word boundaries to ensure accurate matching:

- For single words: `\bkeyword\b` matches the exact word
- For multi-word phrases: It allows flexible spacing between words while maintaining word order

## Limitations

- Depends on PDF text extraction quality (some PDFs with scanned content or unusual fonts may not extract properly)
- Case-insensitive matching is used, so capitalization variants are treated as the same keyword

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
