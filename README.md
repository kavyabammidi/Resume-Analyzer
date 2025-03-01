# 📄 ATS Resume Analyzer

## 📌 Overview
ATS Resume Analyzer is an AI-powered application designed to analyze resumes and compare them against job descriptions using **Google Gemini AI**. It helps users understand how well their resumes align with job requirements and suggests improvements.

---

## 🚀 Features
- Upload **PDF resumes** and extract text.
- Compare resumes against **job descriptions**.
- Generate **percentage match** and **keyword suggestions**.
- AI-powered insights for **resume optimization**.
- User-friendly **Streamlit** interface.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Google Gemini AI
- **PDF Processing:** PyPDF2
- **Deployment:** Heroku / Hugging Face Spaces

---

## 📂 Project Structure
```
📦 ATS_RESUME_ANALYZER
├── 📄 app.py            # Main application file
├── 📄 requirements.txt  # Dependencies
├── 📄 .env              # Environment variables (API Key)
└── 📄 README.md         # Project documentation
```

---

## 🔧 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### **5️⃣ Run the Application**
```bash
streamlit run app.py
```

---

## 🖥️ Usage
1. Upload a **PDF resume**.
2. Enter the **job description**.
3. AI evaluates the resume and provides a **match percentage**.
4. Get **keyword suggestions** to improve alignment.

---

## 🌍 Deployment
### **Deploy to Heroku**
```bash
git init
git add .
git commit -m "Deploying ATS Resume Analyzer"
heroku create ats-resume-analyzer
git push heroku main
heroku open
```

### **Deploy to Hugging Face Spaces**
1. Create a **new space** on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Upload **app.py**, `requirements.txt`, and `.env`.
3. Commit changes and **Deploy**.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 🙌 Acknowledgments
- **Google Gemini AI** for resume evaluation.
- **Streamlit** for the interactive UI.
- **PyPDF2** for resume text extraction.

---

### 🎯 Future Enhancements
- Support for **multiple resume formats (Word, TXT, etc.)**.
- **Integration with job portals** for real-time job matching.
- **AI-powered resume rewriting suggestions**.

💡 Feel free to contribute or suggest new features!
