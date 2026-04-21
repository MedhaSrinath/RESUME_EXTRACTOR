print("Resume Skills Extractor")
text = input("Paste your resume text: ")
skills = ["Python", "SQL", "Java", "Machine Learning", "C++", "HTML", "CSS"]
found_skills = []
for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)

print("Skills found:", ",".join(found_skills))