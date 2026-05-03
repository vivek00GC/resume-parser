import PyPDF2
import re

# Predefined skills list (you can expand this)
skills_list = [
    "python", "java", "c++", "sql", "html", "css",
    "javascript", "react", "node", "machine learning"
]

# Function to extract text from PDF
def extract_text(pdf_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "" 
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

# Extract email using regex
def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    return match[0] if match else "Not found"

# Extract name (simple logic: first line)
def extract_name(text):
    lines = text.split("\n")
    return lines[0].strip()

# Extract skills
def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

# Main function
def parse_resume(pdf_file):
    text = extract_text(pdf_file)

    name = extract_name(text)
    email = extract_email(text)
    skills = extract_skills(text)

    print("\n----- Resume Details -----")
    print("Name:", name)
    print("Email:", email)
    print("Skills:", ", ".join(skills))

# Run program
parse_resume("C:/Users/VICTUS/OneDrive/Desktop/resume_parser/sample_resume.pdf")