from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")

class StudentData(BaseModel):
    study_hours: float
    attendance: float

@app.get("/")
def home():
    return {"message": "Student Performance Predictor API"}

@app.post("/predict")
def predict(data: StudentData):
    prediction = model.predict(
        np.array([[data.study_hours, data.attendance]])
    )

    return {
       "predicted_score": round(float(prediction[0]), 2)
    }