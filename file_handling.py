
import os
from gpt_interaction import process_content_with_gpt
from web_scraping import scrape_web_content
from utils import read_file, convert_pdf_to_text, convert_docx_to_text, convert_excel_to_csv

def process_files(input_dir, tmp_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Handle different file types
            if file.endswith('.pdf'):
                text_content = convert_pdf_to_text(file_path, tmp_dir)
            elif file.endswith('.docx'):
                text_content = convert_docx_to_text(file_path, tmp_dir)
            elif file.endswith('.xlsx'):
                text_content = convert_excel_to_csv(file_path, tmp_dir)
            else:
                text_content = read_file(file_path)

            # Process text content with GPT-4 API
            json_content, json_filename = process_content_with_gpt(text_content)
            # Save JSON content to output directory
            with open(os.path.join(output_dir, json_filename), 'w') as json_file:
                json_file.write(json_content)

def process_links(links_file, tmp_dir, output_dir):
    with open(links_file, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        text_content = scrape_web_content(url.strip(), tmp_dir)
        # Process text content with GPT-4 API
        json_content, json_filename = process_content_with_gpt(text_content)
        # Save JSON content to output directory
        with open(os.path.join(output_dir, json_filename), 'w') as json_file:
            json_file.write(json_content)
