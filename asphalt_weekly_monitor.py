import requests
import pymupdf
import re
import pandas as pd
from datetime import datetime


# Function to download PDF
def download_pdf(url, file_path):
    page = requests.get(url)
    if page.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(page.content)
        print('PDF downloaded successfully.')
    else:
        print(f'Failed to Download PDF. Status code: {page.status_code}')


# Function to extract data from PDF
def extract_data_from_pdf(file_path):
    doc = pymupdf.open(file_path)
    page = doc[0]
    text = page.get_text()

    filtered_text = re.sub(r'[A-Za-z]+', '', text).strip()
    lines = filtered_text.splitlines()

    non_blank_lines = [line for line in lines if line.strip()]
    if len(non_blank_lines) > 5:
        trimmed_lines = non_blank_lines[3:-2]
    else:
        trimmed_lines = []

    columns = ['Posted Date', 'From', 'To', 'low-NH', 'high-NH', 'english-NH', 'metric-NH', 'english-BOS', 'metric-BOS']
    rows = [trimmed_lines[i:i + 9] for i in range(0, len(trimmed_lines), 9)]

    data_dict_list = [dict(zip(columns, row)) for row in rows]
    df = pd.DataFrame(data_dict_list)

    return df


# Main execution
if __name__ == "__main__":
    url = 'https://portal.ct.gov/-/media/dot/documents/dconstruction/asphalt_hist.pdf'

    # Create timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Define file paths with timestamp
    pdf_file_path = f'asphalt_hist_{timestamp}.pdf'
    csv_file_path = f'asphalt_prices_{timestamp}.csv'

    # Download the PDF
    download_pdf(url, pdf_file_path)

    # Extract data from the downloaded PDF
    df = extract_data_from_pdf(pdf_file_path)

    # Save the data to a CSV file
    df.to_csv(csv_file_path, index=False)

    # Retrieve and print the most recent data
    recent_prices_date = df['Posted Date'].iloc[-1]
    ct_recent_price = df['english-NH'].iloc[-1]
    ma_recent_price = df['english-BOS'].iloc[-1]
    from_date_recent = df['From'].iloc[-1]
    to_date_recent = df['To'].iloc[-1]

    print(f'Last Published Date: {recent_prices_date}')
    print(f'From {from_date_recent} to {to_date_recent}')
    print(f'Most Recent CT Price: {ct_recent_price}')
    print(f'Most Recent MA Price: {ma_recent_price}')

