# 📄 Smart Resume & Cover Letter Generator (Powered by Gemini AI)

This web application allows users to generate professional-quality resumes and cover letters using just a few personal and academic details. The app is powered by Google’s Gemini 1.5 Flash model and designed with Flask, HTML, and CSS.

---

## 🌟 What It Does

- 💬 Accepts user inputs like Name, Education, Skills, Certifications, Achievements, and more  
- 🤖 Utilizes the Gemini API to dynamically generate full resume and cover letter text  
- 🖥️ Clean and modern user interface  
- 🔒 Keeps your API key secure using environment variables  
- 📤 Displays formatted AI-generated content instantly — no hardcoded templates

---

## 🧰 Technologies Used

- **Backend**: Flask (Python)  
- **Frontend**: HTML5, CSS3  
- **AI Engine**: Gemini 1.5 Flash (`google-generativeai`)  
- **Config Management**: `python-dotenv` for securing credentials

---

## 📁 Folder Structure

```text
resume_writer_project/
├── app.py                  # Main Python app with Flask routing
├── requirements.txt        # List of dependencies
├── .env                    # API key file (excluded from Git)
├── .gitignore              # Files ignored by version control
│
├── templates/
│   └── index.html          # Frontend input form
│
└── static/
    └── style.css           # Webpage styling
```

---

## ⚙️ Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-username/resume_writer_project.git
cd resume_writer_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a file named `.env` and insert your API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Run the application

```bash
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000/`

---

## 🔁 How It Works

1. User fills out a simple form on the webpage  
2. Input is sent to Google’s Gemini model  
3. AI generates both the resume and a cover letter in proper format  
4. Output is displayed instantly and is fully copyable

---

## ✅ Tests Performed

- 🧪 Various input combinations tested (fresher, experienced, with/without university/year)
- 🎯 Accuracy of Gemini output reviewed manually
- 🛡️ Handled missing inputs without crashing
- 🧩 Compatible across different browsers and screen sizes

---

## 🔮 Possible Add-ons

- 📄 PDF download for resume & cover letter  
- 🌐 Language translation for multilingual support  
- 🧑‍💼 User login & profile saving  
- 🎨 Multiple resume templates  
- 🔍 Job recommendation integration

---

## 👨‍🎓 Developed By

**Harish Kumar Nettem**  
B.Tech CSE | AIML Specialization  
📧 harish.23bce7749@vitapstudent.ac.in  
🎓 VIT University, Amaravati

---

## 📄 License

This project is created for academic and demonstration purposes only. Users are encouraged to review AI-generated content before professional use.
