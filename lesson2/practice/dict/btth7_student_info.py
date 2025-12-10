from typing import Any

student: dict[str, Any] = {
    "name": "Nguyen Van A",
    "age": 20,
    "scores": [7.5, 8.0, 6.5, 9.0],
}

print("Name: ", student.get("name"))
print("Age: ", student.get("age"))

scores = student.get("scores", [])
avg_score = sum(scores) / len(scores)
student["avg_score"] = avg_score

print("Average Score: ", student.get("avg_score"))