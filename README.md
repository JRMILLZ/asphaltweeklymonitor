# asphaltweeklymonitor
weekly monitor for asphalt in CT and MA

PDF Data Extraction Script
This Python script downloads a PDF file containing historical asphalt prices for 2024, extracts relevant data from the PDF, and saves it as a CSV file. Additionally, it prints out the most recent price data for both Connecticut (CT) and Massachusetts (MA).

Features:
PDF Download: The script downloads a PDF file from a specified URL using requests and saves it locally with a timestamped filename.
Text Extraction: It utilizes PyMuPDF to extract text from the first page of the PDF.
Data Parsing: Extracted text is cleaned using regular expressions and parsed into a structured format.
Data Storage: Parsed data is saved into a Pandas DataFrame and exported to a CSV file with a timestamped filename for version control.
Recent Data Display: After saving the data, the script prints the most recent asphalt prices, including the date range and prices for CT and MA.

Key Libraries Used:
requests: To download the PDF.
pymupdf: For PDF reading and text extraction.
re: For cleaning and filtering text.
pandas: To structure and save extracted data.
datetime: To generate timestamps for file versioning.

How It Works:
Download PDF: The script downloads the PDF file from a given URL and saves it locally with a timestamp.
Extract Data: Text is extracted from the first page of the PDF and filtered to remove unwanted characters. Relevant data is split into rows and columns based on the format of the document.
Save Data to CSV: The extracted data is stored in a CSV file with a timestamp in the filename for easy tracking of multiple runs.
Display Latest Prices: The script prints the most recent published asphalt prices for Connecticut and Massachusetts, including the date range of the data.

-----example output-----
Last Published Date: 08/30/2024
From 08/01/2024 to 08/30/2024
Most Recent CT Price: 150.45
Most Recent MA Price: 160.75

Usage:
Clone the repository.
Install the required dependencies listed in requirements.txt.
Run the script to download the latest asphalt prices and save the data to a CSV file.
