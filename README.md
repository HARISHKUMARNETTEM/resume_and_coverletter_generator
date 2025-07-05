# 📄 AI Resume & Cover Letter Generator using Gemini API

This project is a web-based application that helps users generate personalized resumes and cover letters using Google's Gemini 1.5 Flash model. Built with Flask for the backend and styled using HTML and CSS, the app takes user input and produces professional content automatically, tailored to their chosen job role.

---

## 🚀 Project Highlights

- Uses **Generative AI** to create resumes and cover letters instantly  
- Developed with **Flask (Python)** for backend logic  
- Responsive **HTML/CSS frontend** for easy input  
- User form includes: Name, Contact, Education, Experience, Skills, Certifications, Achievements, Job Role, Company  
- Environment variables are handled securely with a `.env` file  
- Output is clean, readable, and copyable from the browser

---

## 🛠️ Tech Stack

- **Backend:** Python + Flask  
- **Frontend:** HTML5, CSS3  
- **AI Integration:** Google Gemini 1.5 Flash (`google-generativeai`)  
- **Config:** `python-dotenv` for environment variable management

---

## 📁 Folder Structure

```text
resume_writer_project/
├── app.py                # Core Flask application
├── .env                  # Contains API key (excluded from GitHub)
├── .gitignore            # Files/folders to ignore in version control
├── requirements.txt      # Python package dependencies
│
├── templates/
│   └── index.html        # Web form for user inputs
│
└── static/
    └── style.css         # CSS for form layout and results
🧑‍💻 Running the App
Step 1: Clone the project
bash
Copy
Edit
git clone https://github.com/your-username/resume_writer_project.git
cd resume_writer_project
Step 2: Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Add your Gemini API key
Create a .env file and paste your API key:

env
Copy
Edit
GEMINI_API_KEY=your_actual_api_key
Step 4: Start the application
bash
Copy
Edit
python app.py
Now open your browser and go to:
http://127.0.0.1:5000/

📋 How It Works
The user fills out a form with basic job application information

The backend sends the data to Gemini using a structured prompt

The AI responds with a professional resume and cover letter

The output is displayed in a formatted, scrollable interface

✅ Testing and Evaluation
To validate the performance of the application, several tests were conducted:

Input scenarios: Fresher, experienced, invalid, and long-form data

Output accuracy: Matched job role, skills, and achievements

Form validation: Required fields enforced properly

Device compatibility: Responsive across screens

Error handling: Handled edge cases without crashes

📊 Test Results
Relevance: AI output aligned well with input fields

Performance: Average output time was 2–3 seconds

Stability: Handled repeated or malformed inputs gracefully

🔮 Future Enhancements
Download as PDF
Export the generated resume and cover letter as downloadable PDF files.

Template Selection
Let users choose between multiple resume formats.

User Login System
Allow account creation to save, edit, and manage past resumes.

Live Recommendations
Provide AI-powered job role, skill, and achievement suggestions while typing.

Language Support
Generate resumes in languages like Hindi, French, Telugu, etc.

Integration with Job Portals
Autofill or sync details with platforms like LinkedIn or Naukri.

👨‍🎓 Developer Info
Harish Kumar Nettem
B.Tech CSE | AIML Specialization
Email: harish.23bce7749@vitapstudent.ac.in
Vellore Institute of Technology, Amaravati

📄 License
This project is intended for educational purposes only. Please verify and edit AI-generated resumes before submitting to companies or institutions.