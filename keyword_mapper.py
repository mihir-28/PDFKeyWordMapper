# Import necessary libraries
import sys          # For system operations like exiting the program
import os           # For file path operations
import re           # For regular expression matching
from PyPDF2 import PdfReader  # For reading PDF files

# Path to the PDF file that will be analyzed
pdf_path = "path/to/your/file"

# List of page numbers to exclude from the analysis (e.g., references, appendices)
# Add comma separated page numbers to skip individual pages like [1, 5, 9]
# Or use ranges for consecutive pages like: list(range(37, 100)) + list(range(122, 126))
pages_to_skip = []

try:
    # Check if the specified PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        sys.exit(1)
    
    # Create a PDF reader object and get the total number of pages
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    
    # Print status information
    print(f"Successfully opened PDF with {num_pages} pages.")
    if pages_to_skip:
        print(f"Skipping pages: {', '.join(map(str, pages_to_skip))}")

    # Define a list of keywords to search for in the PDF
    # These keywords are related to blockchain and web development concepts
    extended_keywords = [
      'Keywords', 'you', 'want', 'to', 'search'
    ]

    # Initialize a dictionary to store the page numbers where each keyword appears
    extended_index = {keyword: [] for keyword in extended_keywords}

    # Process each page in the PDF
    for page_num in range(num_pages):
        # Skip pages that were explicitly marked to be skipped
        if (page_num + 1) in pages_to_skip:
            print(f"Skipping page {page_num + 1} as requested")
            continue
            
        try:
            # Extract text from the current page
            page = reader.pages[page_num]
            text = page.extract_text() or ""
            
            # Check if the page has extractable text
            if not text.strip():
                print(f"Warning: Page {page_num + 1} appears to have no extractable text")
                continue
                
            # Search for each keyword in the current page's text
            for keyword in extended_keywords:
                if ' ' not in keyword:
                    # For single-word keywords, use word boundary in regex to match exact words
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    if re.search(pattern, text, re.IGNORECASE):
                        extended_index[keyword].append(page_num + 1)
                else:
                    # For multi-word keywords, split into parts and allow flexible spacing
                    parts = [re.escape(part) for part in keyword.split()]
                    flexible_pattern = r'\b' + r'\s+'.join(parts) + r'\b'
                    if re.search(flexible_pattern, text, re.IGNORECASE):
                        extended_index[keyword].append(page_num + 1)
            
            # Display progress after every 10 pages or on the last page
            if (page_num + 1) % 10 == 0 or page_num + 1 == num_pages:
                # Calculate and show progress percentage, accounting for skipped pages
                processed_count = page_num + 1 - len([p for p in pages_to_skip if p <= page_num + 1])
                total_to_process = num_pages - len(pages_to_skip)
                percent_done = processed_count / total_to_process * 100
                print(f"Processed {page_num + 1} of {num_pages} pages ({percent_done:.1f}%)")
                
        except Exception as e:
            # Handle errors that occur during page processing
            print(f"Error processing page {page_num + 1}: {str(e)}")

    # Remove duplicate page numbers for each keyword and ensure they're sorted
    for keyword in extended_index:
        extended_index[keyword] = sorted(set(extended_index[keyword]))

    # Filter out keywords that weren't found in the document
    extended_index_cleaned = {k: v for k, v in extended_index.items() if v}
    
    # Create a list of keywords that weren't found
    not_found_keywords = [k for k, v in extended_index.items() if not v]

    # Generate output filename based on the input PDF name
    output_filename = "keywords_index.txt"

    # Write results to a text file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("Keyword Index Results:\n")
        f.write(f"Document: {pdf_path}\n")
        f.write(f"Total pages: {num_pages}\n")
        if pages_to_skip:
            f.write(f"Pages skipped: {', '.join(map(str, pages_to_skip))}\n")
        f.write("\n")
        
        # Write the found keywords and their page numbers
        if not extended_index_cleaned:
            f.write("No matches found for any keywords.\n")
        else:
            f.write("FOUND KEYWORDS:\n")
            for keyword, pages in sorted(extended_index_cleaned.items()):
                f.write(f"{keyword}: {', '.join(map(str, pages))}\n")
        
        # Write the list of keywords that weren't found
        if not_found_keywords:
            f.write("\nNOT FOUND KEYWORDS:\n")
            for keyword in sorted(not_found_keywords):
                f.write(f"{keyword}\n")

    # Print summary statistics to the console
    print(f"\nKeyword index saved to {output_filename}")
    print(f"Found matches for {len(extended_index_cleaned)} out of {len(extended_keywords)} keywords")
    print(f"Not found: {len(not_found_keywords)} keywords")

except Exception as e:
    # Handle any general errors that occur during script execution
    print(f"Error: {str(e)}")
