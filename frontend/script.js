async function predictMarks() {

    const study_hours =
        document.getElementById("study_hours").value;

    const attendance =
        document.getElementById("attendance").value;

    const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                study_hours: Number(study_hours),
                attendance: Number(attendance)
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerText =
        "Predicted Marks: " + data.predicted_marks;
}