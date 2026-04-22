from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text.lower()


def analyze_skills(text):
    skills_dict = {
        "python": ["python", "py"],
        "sql": ["sql", "mysql", "postgres"],
        "java": ["java"],
        "machine learning": ["machine learning", "ml"],
        "c++": ["c++", "cpp"],
        "html": ["html"],
        "css": ["css"]
    }

    found_skills = {}

    for skill, variations in skills_dict.items():
        for word in variations:
            if word in text:
                found_skills[skill] = word
                break

    missing_skills = []

    for skill in skills_dict:
        if skill not in found_skills:
            missing_skills.append(skill)

    return found_skills, missing_skills