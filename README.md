# 🧠 AI Resume Skill Extractor

A smart web application that analyzes resumes (PDF) and extracts relevant technical skills using NLP-based logic.

---

## 🚀 Features

* 📄 Upload resume in PDF format
* 🔍 Extracts text from PDF
* 🧠 Detects skills using intelligent matching (handles variations like "ML" → Machine Learning)
* 💡 Suggests missing skills
* 📊 Displays total detected skills
* 🌐 Interactive web interface using Streamlit

---

## 🧰 Tech Stack

* Python
* Streamlit
* PyPDF2

---

## 📦 How to Run Locally

1. Clone the repository:

```
git clone <your-repo-link>
cd <your-repo-name>
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 📁 Project Structure

```
resume-skill-extractor/
│
├── app.py              # Main web app
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. The app extracts text using PyPDF2
3. Converts text to lowercase for uniform processing
4. Matches skills using a dictionary of keywords and variations
5. Displays detected skills along with how they were identified
6. Suggests missing skills from the predefined list

---

## 🎯 Example

**Input:**
"I have experience in ML and Py"

**Output:**

* Python (detected as: py)
* Machine Learning (detected as: ml)

---

## 🌱 Future Improvements

* Support for more skills
* Better NLP using ML models
* Resume scoring system
* OCR support for scanned PDFs

---

## 🏁 Author

Built as part of my journey into AI and software development 🚀
