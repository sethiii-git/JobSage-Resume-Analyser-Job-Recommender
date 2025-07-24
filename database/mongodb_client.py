# database/mongodb_client.py

from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Load Mongo URI and DB name from .env
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "jobsage")

# Validate environment variable presence
if not MONGO_URI:
    raise ValueError("MONGO_URI not found in environment variables. Please check your .env file.")

# Initialize client
client = MongoClient(MONGO_URI)

# Access database
db = client[MONGO_DB_NAME]

# Collections
data_collection = db["user_data"]
feedback_collection = db["user_feedback"]

def save_resume_to_db(resume_dict):
    """Inserts a parsed resume dict into the database."""
    resume_dict["timestamp"] = datetime.utcnow()
    result = data_collection.insert_one(resume_dict)
    return str(result.inserted_id)

def save_feedback_to_db(feedback_dict):
    """Inserts feedback data into the feedback collection."""
    feedback_dict["timestamp"] = datetime.utcnow()
    result = feedback_collection.insert_one(feedback_dict)
    return str(result.inserted_id)
