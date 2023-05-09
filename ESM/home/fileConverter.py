import io
import os
import PyPDF2
import json
from pathlib import Path


#폴더 내 파일 이름 가져오기

def convert():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),))

    
    
    file_path = os.path.join(f'{BASE_DIR}', 'inputfile')
    txt_path  = os.path.join(f'{BASE_DIR}', 'txt')

    # 텍스트 파일을 저장할 폴더가 없는 경우 폴더 생성
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)

    
    # 모든 PDF 파일을 리스트로 가져오기
    pdf_files = [f for f in os.listdir(file_path) if f.endswith('.pdf')]

    # PDF 파일을 텍스트 파일로 변환
    for pdf_file in pdf_files:
        name = pdf_file[0]
        ftpye =  pdf_file[1]
        txt_file = os.path.join(txt_path, f'{name}.txt')

        

        with open(txt_file, "w+", encoding='utf-8') as file:
            pdf = open(os.path.join(file_path, pdf_file), 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf)


            for i in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[i]
                text = page.extract_text()
                file.write(text)
                file.write(f"\n\n\n")
            #file.write(f"---End---")
            pdf.close()
        
    os.remove(os.path.join(file_path, pdf_file))

