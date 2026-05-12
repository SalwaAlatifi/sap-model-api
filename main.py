from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("sap_model.pkl")

features = [
    "semester",
    "prev_sgpa",
    "avg_midterm",
    "avg_quiz",
    "avg_assignment",
    "attendance_rate",
    "num_courses",
    "avg_difficulty",
    "is_barred"
]

students_db = {
    "S1001": {
        "semester": 3,
        "prev_sgpa": 4.2,
        "avg_midterm": 25.5,
        "avg_quiz": 13.2,
        "avg_assignment": 14.0,
        "attendance_rate": 91.5,
        "num_courses": 5,
        "avg_difficulty": 3.4,
        "is_barred": 0
    },
    "S1002": {
        "semester": 5,
        "prev_sgpa": 2.8,
        "avg_midterm": 18.0,
        "avg_quiz": 9.5,
        "avg_assignment": 10.0,
        "attendance_rate": 70.0,
        "num_courses": 6,
        "avg_difficulty": 4.1,
        "is_barred": 1
    },
    "S1003": {
        "semester": 2,
        "prev_sgpa": 4.8,
        "avg_midterm": 28.0,
        "avg_quiz": 14.5,
        "avg_assignment": 15.0,
        "attendance_rate": 98.0,
        "num_courses": 4,
        "avg_difficulty": 2.9,
        "is_barred": 0
    }
}


@app.get("/")
def home():
    return {"message": "SAP Prediction API is running"}


@app.get("/predict/student/{student_id}")
def predict_student(student_id: str):

    if student_id not in students_db:
        return {"error": "Student not found"}

    student_data = students_db[student_id]

    input_data = pd.DataFrame([student_data])
    input_data = input_data[features]

    prediction = model.predict(input_data)[0]

    return {
        "student_id": student_id,
        "predicted_sgpa": round(float(prediction), 2),
        "input_data": student_data
    }