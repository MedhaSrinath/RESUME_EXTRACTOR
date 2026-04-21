from PyPDF2 import PdfReader

print("Resume Skill Extractor")
print("-" * 40)

file_path = input("Enter PDF file name (e.g., resume.pdf): ")

reader = PdfReader(file_path)
text = ""

for page in reader.pages:
    extracted = page.extract_text()
    if extracted:  # important for safety
        text += extracted

text = text.lower()

skills = ["python", "sql", "java", "machine learning", "c++", "html", "css"]

found_skills = []

for skill in skills:
    if skill in text:
        found_skills.append(skill)

missing_skills = []

for skill in skills:
    if skill not in found_skills:
        missing_skills.append(skill)

# OUTPUT
if found_skills:
    print("✅ Skills found:", ", ".join(found_skills))
else:
    print("❌ No matching skills found")

print("Total skills detected:", len(found_skills))

print("\n💡 Suggested skills to learn:")

if missing_skills:
    print(", ".join(missing_skills))
else:
    print("You have all listed skills 🎉")