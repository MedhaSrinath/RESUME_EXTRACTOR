print("Resume Skill Extractor")
print("-" * 40)

text = input("Paste your resume text: ").lower()

skills = ["python", "sql", "java", "machine learning", "c++", "html", "css"]

found_skills = []

for skill in skills:
    if skill in text:
        found_skills.append(skill)

missing_skills = []

for skill in skills:
    if skill not in found_skills:
        missing_skills.append(skill)

if found_skills:
    print("✅ Skills found:", ", ".join(found_skills))
else:
    print("❌ No matching skills found")

print("Total skills detected:", len(found_skills))

print("\n💡 Suggested skills to learn:")
print(", ".join(missing_skills))