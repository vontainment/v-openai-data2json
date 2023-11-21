
import requests
from bs4 import BeautifulSoup

def scrape_web_content(url, tmp_dir):
    response = requests.get(url)
    response.raise_for_status()  # Ensures HTTP requests were successful

    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove scripts, styles, and other non-text elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    # Get text and clean it up
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text_content = '\n'.join(chunk for chunk in chunks if chunk)

    # Save the extracted text as a temporary file
    tmp_filename = url.split('/')[-1] + '.txt'
    tmp_path = os.path.join(tmp_dir, tmp_filename)
    with open(tmp_path, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write(text_content)

    return tmp_path
