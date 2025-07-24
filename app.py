import streamlit as st
import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
FLASK_API_URL = os.getenv("FLASK_API_URL", "http://localhost:5000")

st.set_page_config(page_title="JobSage | Resume Analyzer", layout="wide")
st.title("Welcome to JobSage😸")
st.markdown("""
    <style>
    /* Make it adaptive to dark/light mode */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: transparent;
        color: inherit;
    }

    .block {
        background-color: rgba(255, 255, 255, 0.05); /* transparent for dark mode */
        padding: 2rem;
        margin-bottom: 2rem;
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .title {
        font-size: 1.8rem;
        font-weight: 700;
        color: inherit;
        margin-bottom: 1rem;
        border-left: 5px solid #1f77b4;
        padding-left: 1rem;
    }

    .stFileUploader {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 0.8rem;
        border: 1px dashed rgba(255,255,255,0.2);
    }

    .stMetric {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 0.6rem;
        padding: 1rem;
    }

    input[type="text"], .stTextInput input {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 0.5rem;
        padding: 0.6rem 1rem;
        font-size: 1rem;
        color: inherit;
    }

    button {
        background-color: #1f77b4 !important;
        color: white !important;
        padding: 0.5rem 1.5rem;
        border-radius: 0.4rem;
        font-weight: 600;
    }

    .stSpinner > div {
        color: #1f77b4;
    }

    a {
        color: #4da6ff;
        text-decoration: none;
        font-weight: 500;
    }

    a:hover {
        text-decoration: underline;
    }

    .job-card {
        background-color: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #00bcd4;
        padding: 1rem;
        border-radius: 0.6rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- Upload Resume ----------------
#st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="title">📄 Step 1: Upload Your Resume</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    st.success("📁 File uploaded successfully!")

    with st.spinner("Processing your resume..."):
        res = requests.post(
            url=f"{FLASK_API_URL}/upload_resume",
            files={"resume": uploaded_file}
        )

        if res.status_code == 200:
            response = res.json()
            parsed_data = response["parsed_data"]
            resume_score = response["score"]

            st.success("✅ Resume processed successfully!")
            # st.subheader("Your Basic Info")
            # st.json(parsed_data)
            st.subheader("Your Basic Info")
            # 👤 Name
            if parsed_data.get("name"):
                st.markdown(f"**👤 Name:** {parsed_data['name']}")

            # 📧 Email
            if parsed_data.get("email"):
                st.markdown(f"**📧 Email:** {parsed_data['email']}")

            # 📞 Phone
            if parsed_data.get("mobile_number"):
                st.markdown(f"**📞 Phone:** {parsed_data['mobile_number']}")
            
            # 🎓 Academic Qualification
            if parsed_data.get("degree"):
                st.markdown(f"**🎓 Academic Qualification(s):** {', '.join(parsed_data['degree']) if isinstance(parsed_data['degree'], list) else parsed_data['degree']}")


            # 🧠 Skills
            # if parsed_data.get("skills"):
            #     st.markdown(f"**🧠 Skills:** {', '.join(parsed_data['skills'])}")
            # if parsed_data.get("skills"):
            #     st.markdown("**🧠 Skills:**", unsafe_allow_html=True)

            #     skills_html = """
            #     <div style='display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; margin-bottom: 15px;'>
            #     """
            #     for skill in parsed_data["skills"]:
            #         skills_html += f"""
            #         <span style='
            #             background-color: #e0f7fa;
            #             color: #00796b;
            #             padding: 6px 12px;
            #             border-radius: 20px;
            #             font-size: 14px;
            #             font-weight: 500;
            #             font-family: "Segoe UI", sans-serif;
            #         '>{skill}</span>
            #         """
            #     skills_html += "</div>"

            #     st.markdown(skills_html, unsafe_allow_html=True)
            if parsed_data.get("skills"):
                st.markdown("**🧠 Skills:**", unsafe_allow_html=True)

                skills_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; margin-bottom: 15px;'>"
                for skill in parsed_data["skills"]:
                    skills_html += f"<span style='background-color: #e0f7fa; color: #00796b; padding: 6px 12px; border-radius: 20px; font-size: 14px; font-weight: 500; font-family: Segoe UI, sans-serif;'>{skill}</span>"
                skills_html += "</div>"

                st.markdown(skills_html, unsafe_allow_html=True)


            st.subheader("Resume Score")
            st.metric(label="Score", value=f'{resume_score}/100')
        else:
            st.error("❌ Failed to process resume")
            st.write("Server response:", res.text)

    # ----------- Role Selection -----------
    #st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown('<div class="title">🎯 Step 2: Select Your Target Role</div>', unsafe_allow_html=True)
    job_role = st.selectbox("Choose your target job role", [
        "Data Science", "Web Development", "Mobile App Development", "UI/UX Design",
        "DevOps", "Cloud Computing","Cybersecurity","Robotics","Game Development","Healthcare",
        "Accounting & Finance","Business Analysis","Digital Marketing","Sales","Teaching & Education"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------- Skill Recommendations -----------
    #st.markdown('<div class="block">', unsafe_allow_html=True)
    # 📚 Step 3: Skill Gap & Learning Resources
    st.markdown("### 📚 Step 3: Skill Gap & Learning Resources")

    if parsed_data:
        resume_text = " ".join(parsed_data.get("skills", []) + parsed_data.get("degree", []))

        with st.spinner("Analyzing your skill gap and fetching relevant courses..."):
            try:
                response = requests.post(
                    f"{FLASK_API_URL}/recommend_skills",
                    json={"resume_text": resume_text,
                          "target_role": job_role}
                )
                if response.status_code == 200:
                    skill_reco = response.json()
                    st.success("Recommended skills and courses generated!")

                    # st.subheader("🔧 Additional Skills You May Need:")
                    # missing_skills = skill_reco.get("missing_skills", [])

                    # if missing_skills:
                    #     st.write(", ".join(missing_skills))
                    # else:
                    #     st.write("✅ You already have all the major skills for this role!")
                    st.subheader("🔧 Additional Skills You May Need:")
                    missing_skills = skill_reco.get("missing_skills", [])

                    if missing_skills:
                        skills_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; margin-bottom: 15px;'>"
                        for skill in missing_skills:
                            skills_html += f"<span style='background-color: #fff3e0; color: #e65100; padding: 6px 12px; border-radius: 20px; font-size: 14px; font-weight: 500; font-family: Segoe UI, sans-serif;'>{skill}</span>"
                        skills_html += "</div>"

                        st.markdown(skills_html, unsafe_allow_html=True)
                    else:
                        st.markdown("🎉 You're all caught up! No missing skills detected.")

                    # st.subheader("🎓 Recommended Courses:")
                    # recommended_courses = skill_reco.get("recommended_courses", {})

                    # if recommended_courses:
                    #     for skill, course_list in recommended_courses.items():
                    #         st.markdown(f"**{skill}**")
                    #         for course_url in course_list:
                    #             st.markdown(f"- [Course Link]({course_url})")
                    # st.subheader("🎓 Recommended Courses:")

                    # recommended_courses = skill_reco.get("recommended_courses", {})

                    # if recommended_courses:
                    #     for skill, course_list in recommended_courses.items():
                    #         card_html = f"""
                    #         <div style='
                    #             background-color: #f9f9f9;
                    #             border: 1px solid #ddd;
                    #             border-radius: 12px;
                    #             padding: 16px;
                    #             margin-bottom: 15px;
                    #             box-shadow: 0 2px 5px rgba(0,0,0,0.06);
                    #         '>
                    #             <h4 style='
                    #                 color: #2c3e50;
                    #                 margin-bottom: 12px;
                    #                 font-family: "Segoe UI", sans-serif;
                    #             '>📌 {skill.title()}</h4>
                    #         """

                    #         for course_url in course_list:
                    #             card_html += f"""
                    #             <a href="{course_url}" target="_blank" style='
                    #                 display: inline-block;
                    #                 margin: 5px 0;
                    #                 padding: 8px 14px;
                    #                 background-color: #e3f2fd;
                    #                 color: #1565c0;
                    #                 border-radius: 8px;
                    #                 font-size: 14px;
                    #                 text-decoration: none;
                    #                 font-weight: 500;
                    #                 font-family: "Segoe UI", sans-serif;
                    #             '>🔗 View Course</a><br>
                    #             """

                    #         card_html += "</div>"

                    #         st.markdown(card_html, unsafe_allow_html=True)
                    st.subheader("🎓 Recommended Courses:")

                    recommended_courses = skill_reco.get("recommended_courses", {})

                    if recommended_courses:
                        courses_html = ""
                        for skill, course in recommended_courses.items():
                            courses_html += f"""<div style='background color=#e0f7fa; border: 1px solid #ddd; border-radius: 12px; padding: 16px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.06);'><h4 style='color: #dddddd; margin-bottom: 12px; font-family: "Segoe UI", sans-serif;'>📌 {skill.title()}</h4>"""
                            #for course_url in course_list:
                            courses_html += f"""<a href="{course}" target="_blank" style='display: inline-block; margin: 5px 0; padding: 8px 14px; background-color: #e3f2fd; color: #1565c0; border-radius: 8px; font-size: 14px; text-decoration: none; font-weight: 500; font-family: "Segoe UI", sans-serif;'>🔗 View Course</a><br>"""
                            courses_html += "</div>"
                        st.markdown(courses_html, unsafe_allow_html=True)

                    else:
                        st.write("⚠️ No course suggestions found for your missing skills.")

                else:
                    st.error("❌ Skill recommendation failed.")
            except Exception as e:
                st.error(f"⚠️ Error occurred: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)


    # ----------- Job Recommendations -----------
    #st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown('<div class="title">💼 Step 4: Job Opportunities</div>', unsafe_allow_html=True)

    location = st.text_input("🌍 Enter preferred job location", "India")
    if st.button("🔍 Show Job Recommendations"):
        with st.spinner("Finding relevant jobs..."):
            job_res = requests.post(f"{FLASK_API_URL}/recommend_jobs", json={
                "skills": parsed_data.get("skills", []),
                "target_role":job_role
            })

            if job_res.status_code == 200:
                jobs = job_res.json()
                if jobs:
                    for job in jobs:
                        st.markdown(f"""
                             <div class="job-card">
                            <strong>{job.get('title', 'No title')}</strong><br>
                            
                            📍 {job.get('company', 'Unknown')} — {job.get('location', 'N/A')}<br>
                            🔗 <a href="{job.get('url', '#')}" target="_blank">Apply Now</a>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("⚠️ No jobs found for your criteria.")
            else:
                st.error("❌ Failed to fetch jobs.")
    st.markdown('</div>', unsafe_allow_html=True)
