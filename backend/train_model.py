from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

data = {
    "study_hours": [1,2,3,4,5,6,7,8],
    "attendance": [50,55,60,65,70,75,80,90],
    "quiz_score": [30,35,40,50,60,70,80,90],
    "assignment_score": [40,45,50,55,65,75,85,95],
    "midterm_score": [35,40,45,55,65,75,85,95],
    "projects_completed": [0,1,1,2,2,3,4,5],
    "marks": [35,40,45,55,65,75,85,95]
}

df = pd.DataFrame(data)

X = df[[
    "study_hours",
    "attendance",
    "quiz_score",
    "assignment_score",
    "midterm_score",
    "projects_completed"
]]

y = df["marks"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully")