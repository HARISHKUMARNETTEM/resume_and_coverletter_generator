from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resume = ""
    cover_letter = ""
    show_output = False

    education_options = ["12th", "BTech - CSE", "BTech - Electrical", "MTech"]
    experience_options = ["Fresher", "1 Year", "2 Years", "3-5 Years", "5+ Years"]

    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        education = request.form['education']
        experience = request.form['experience']
        job_role = request.form['job_role']
        certifications = request.form['certifications']
        company = request.form['company']
        skills = request.form['skills']
        address = request.form['address']
        achievements = request.form['achievements']

        prompt = f"""
        Create a professional resume and a formal cover letter.
       
        
        Name: {name}
        Contact: {contact}
        Address: {address}
        Education: {education}
        Work Experience: {experience}
        Job Role: {job_role}
        Company: {company}
        Skills: {skills}
        Certifications: {certifications}
        Achievements: {achievements}

        First provide the resume, then the cover letter.
        """

        response = model.generate_content(prompt)
        output = response.text.strip()
        output = output.replace("Summary", "Objective")

        if "Cover Letter" in output:
            parts = output.split("Cover Letter")
            resume = parts[0].strip()
            cover_letter = "Cover Letter" + parts[1].strip()
        else:
            resume = output

        show_output = True

    return render_template("index.html",
                           resume=resume,
                           cover_letter=cover_letter,
                           show_output=show_output,
                           education_options=education_options,
                           experience_options=experience_options)

if __name__ == '__main__':
    app.run(debug=True)
