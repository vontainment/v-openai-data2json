
import os
import PyPDF2
import pandas as pd
import docx
import openpyxl

def create_directories(dir_list):
    for dir in dir_list:
        if not os.path.exists(dir):
            os.makedirs(dir)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def convert_pdf_to_text(pdf_path, tmp_dir):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text_content = '\n'.join([reader.getPage(i).extractText() for i in range(reader.numPages)])
    tmp_path = os.path.join(tmp_dir, os.path.basename(pdf_path) + '.txt')
    with open(tmp_path, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write(text_content)
    return tmp_path

def convert_docx_to_text(docx_path, tmp_dir):
    doc = docx.Document(docx_path)
    text_content = '\n'.join([para.text for para in doc.paragraphs])
    tmp_path = os.path.join(tmp_dir, os.path.basename(docx_path) + '.txt')
    with open(tmp_path, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write(text_content)
    return tmp_path

def convert_excel_to_csv(excel_path, tmp_dir):
    df = pd.read_excel(excel_path)
    csv_path = os.path.join(tmp_dir, os.path.basename(excel_path) + '.csv')
    df.to_csv(csv_path, index=False)
    return csv_path
