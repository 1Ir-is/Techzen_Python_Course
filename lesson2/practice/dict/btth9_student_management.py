from typing import Any

students: dict[str, dict[str, Any]] = {
    "SV01": {"name": "Nguyen Van A", "age": 20},
    "SV02": {"name": "Tran Thi B", "age": 21},
}

students["SV03"] = {"name": "Huynh Minh Huy", "age": 20}

if "SV01" in students and "age" in students["SV01"]:
    students["SV01"]["age"] += 1

for student_id, info in students.items():
    name = info.get("name", "Unknown")
    age = info.get("age", 0)
    print(f"ID: {student_id}, Name: {name}, Age: {age}")