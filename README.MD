# 💼 JobSage – Resume Analyzer & Smart Job Recommender

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-orange?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

**JobSage** is an intelligent, end-to-end resume evaluation and job recommendation system that:
- Parses resumes
- Scores them against job roles
- Suggests improvements and learning resources
- Recommends real-time job openings based on your extracted skills

> Built using Flask + Streamlit + MongoDB + NLP – optimized for career readiness 🚀

---

## ✨ Features

✅ Resume parsing and information extraction (Name, Email, Skills, Education, etc.)  
✅ Resume scoring based on job role skill match  
✅ Skill gap analysis with course suggestions  
✅ Real-time job recommendation from Remotive API  
✅ Streamlit UI with clean card-based job listings  
✅ MongoDB integration for resume and feedback storage  
✅ Modular and extensible codebase for easy scaling

---

## 🗂 Project Structure

JobSage/
│
├── api/
│ ├── constants.py # All constant data (roles, weights, etc.)
│ ├── helpers.py # Text cleaning & NLP helper functions
│ ├── job_recommender.py # Real-time job fetcher using Remotive API
│ ├── resume_parser.py # Resume parsing logic (spaCy + PyPDF2)
│ ├── scorer.py # Resume scoring engine
│ ├── skill_recommender.py # Recommends skills + learning courses
│ ├── utils.py # Common utilities
│
├── database/
│ ├── mongodb_client.py # MongoDB connection setup
│ └── schema.json # Resume schema format
│
├── tests/ # For unit tests (optional)
│
├── venv/ # Python virtual environment
│
├── .env # API keys and environment variables
├── app.py # Streamlit UI frontend
├── config.py # Global config (URLs, DB, etc.)
├── main.py # Flask backend server
├── requirements.txt # Python dependencies
├── runtime.txt # Python runtime version

---

## 🔧 Setup & Installation

### 1. Clone the Repo
```bash
git clone https://github.com/sethiii-git/jobsage.git
cd jobsage

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.ps1

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Setup Environment Variables
Create a .env file in the root directory with:
FLASK_API_URL=http://localhost:5000
MONGO_URI=your_mongo_connection_string
REMOTIVE_API_URL=https://remotive.io/api/remote-jobs

### 🚀 Run the Project
Start Flask Backend
python main.py

Start Streamlit Frontend
In a separate terminal:
streamlit run app.py

### 🧠 How It Works
Upload your resume (PDF)

The system extracts name, email, phone, skills, education, etc.

Skills are compared to job-role-specific expectations

Resume score is calculated and visualized

Lacking skills are suggested alongside relevant courses

Matching job listings are fetched in real-time from Remotive API

### 💡 Use Cases
🧑‍🎓 Students/freshers preparing for placements

👩‍💼 Professionals exploring job switches

🧑‍💻 Developers seeking personalized learning paths

🧠 Recruiters doing automated resume-job matching

### 🛠 Future Enhancements
Integrate GPT or BERT for smarter NLP understanding

Add PDF-based Resume Improvement Report (via Jinja2 + pdfkit)

JWT Auth and User Dashboard

Admin analytics for job & resume metrics

Multi-resume analysis feature

### 👨‍💻 Author
Machint Sethi
Software Engineering @ DTU • Building Smart NLP + AI systems


