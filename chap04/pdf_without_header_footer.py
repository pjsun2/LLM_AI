import pymupdf
import os

pdf_file_path = r"C:\Users\parkj\Desktop\LLM_AI\chap04\data\5.pdf"
doc = pymupdf.open(pdf_file_path)

header_height = 80
footer_height = 80

full_text = ''

for page in doc:
    rect = page.rect

    header = page.get_text(clip=(0, 0, rect.width , header_height))
    footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
    text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))

    full_text += text + '\n-------------------------------------------\n'

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

txt_file_path = f"C:/Users/parkj/Desktop/LLM_AI/chap04/output/{pdf_file_name}_with_preprocessing.txt"

with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)