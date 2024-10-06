import os
import json
import PyPDF2
import docx
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text
def extract_resume_text(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")
def convert_resume_to_json(resume_text):
    resume_json = {
        "name": "Pooja K",  
        "contact_information": {
            "email": "poojakarunagaran25@gmail.com", 
        },
        "summary": "Experienced Data Analyst...",  
        "work_experience": [],
        "education": [],
        "skills": [],
    }
    resume_json["raw_text"] = resume_text
    return resume_json
def resume_to_json(file_path):
    resume_text = extract_resume_text(file_path)
    resume_json = convert_resume_to_json(resume_text)
    json_file_path = file_path + '.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(resume_json, json_file, indent=4)
    print("Resume converted to JSON format:")
    print(json.dumps(resume_json, indent=4))
    return resume_json
file_path = r'C:\Users\pooja\Downloads\KPooja_Resume.pdf'  
resume_json = resume_to_json(file_path)
print(json.dumps(resume_json, indent=4))