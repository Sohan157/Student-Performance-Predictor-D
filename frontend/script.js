// script.js

async function predictStudent() {

  const data = {
    study_hours: parseFloat(document.getElementById("study_hours").value),
    attendance: parseFloat(document.getElementById("attendance").value),
    quiz_score: parseFloat(document.getElementById("quiz_score").value),
    assignment_score: parseFloat(document.getElementById("assignment_score").value),
    midterm_score: parseFloat(document.getElementById("midterm_score").value),
    projects_completed: parseFloat(document.getElementById("projects_completed").value)
  };

  const response = await fetch("https://student-performance-predictor-d.onrender.com/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();

  document.getElementById("result").innerText =
    "Predicted Score: " + result.predicted_score;
}