import streamlit as st
from resume_extractor import extract_text_from_pdf, analyze_skills

st.title("🧠 Resume Skill Extractor")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    try:
        text = extract_text_from_pdf(uploaded_file)
    except ValueError:
        st.error("Please enter a valid file type.")
        st.stop()

    found_skills, missing_skills = analyze_skills(text)

    if found_skills:
        formatted = []
        for skill, word in found_skills.items():
            formatted.append(f"{skill} (detected as: {word})")

        st.success("✅ Skills found: " + ", ".join(formatted))
    else:
        st.error("❌ No matching skills found")

    st.write("📊 Total skills detected:", len(found_skills))

    st.subheader("💡 Suggested skills to learn")

    if missing_skills:
        st.info(", ".join(missing_skills))
    else:
        st.success("You have all listed skills 🎉")
