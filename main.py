from flask import Flask, request, jsonify
from flask_cors import CORS
from api.resume_parser import ResumeParser
from api.scorer import get_resume_score
from database.mongodb_client import save_resume_to_db
from database.mongodb_client import save_feedback_to_db
from api.skill_recommender import recommend_skills_and_courses
from api.job_recommender import recommend_jobs,fetch_jobs_from_remotive
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend (Streamlit or other)

@app.route("/")
def home():
    return "✅ JobSage Resume Analyzer Backend is Live!"

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    resume_file = request.files['resume']
    if not resume_file:
        return jsonify({"error": "Empty file"}), 400

    # Parse resume
    parser = ResumeParser(resume_file)
    parsed_data = parser.get_extracted_data()

    # Score resume
    resume_text = parser._ResumeParser__text  # Access internal clean text
    score = get_resume_score(resume_text)

    # Save to DB
    save_resume_to_db({
        "name": parsed_data.get("name"),
        "email": parsed_data.get("email"),
        "mobile": parsed_data.get("mobile_number"),
        "skills": parsed_data.get("skills", []),
        "degree": parsed_data.get("degree", []),
        "score": score,
        "page_count": parsed_data.get("no_of_pages", 1),
        "resume_text": resume_text
    })

    return jsonify({
        "message": "Resume processed successfully",
        "parsed_data": parsed_data,
        "score": score
    })

@app.route("/recommend_skills", methods=["POST"])
def recommend_skills():
    data = request.json
    resume_text = data.get("resume_text", "")
    target_role = data.get("target_role", "")

    if not resume_text:
        return jsonify({"error": "No resume text provided"}), 400

    result = recommend_skills_and_courses(resume_text,target_role)
    return jsonify(result)
    #skills = data.get("skills", [])
    #target_role = data.get("target_role", "")
    
    #if not skills or not target_role:
        #return jsonify({"error": "Missing skills or target_role"}), 400

    #recommendations = recommend_skills_and_courses(skills, target_role)
    #return jsonify(recommendations)

@app.route("/recommend_jobs", methods=["POST"])
def recommend_jobs_route():
    data = request.json
    skills = data.get("skills", [])
    target_role=data.get("target_role","")
    if not skills or not target_role:
        return jsonify({"error": "No skills provided"}), 400
    
    resume_text = " ".join(skills)
    job_recommendations = fetch_jobs_from_remotive(target_role,skills)
    return jsonify(job_recommendations)

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    data = request.json
    required_fields = ["feed_name", "feed_email", "feed_score", "comments"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing one or more required fields"}), 400

    feedback = {
        "feed_name": data["feed_name"],
        "feed_email": data["feed_email"],
        "feed_score": data["feed_score"],
        "comments": data["comments"]
    }

    inserted_id = save_feedback_to_db(feedback)
    return jsonify({
        "message": "Feedback submitted successfully",
        "feedback_id": str(inserted_id)
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "ok", "service": "resume_analyzer"})

if __name__ == '__main__':
    app.run(debug=True)
