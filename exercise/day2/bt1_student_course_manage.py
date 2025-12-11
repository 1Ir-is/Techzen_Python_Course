# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

# Set các môn học hiện có
courses = {"math", "python"}

# Cau a: In ra danh sach hoc vien theo format
print("Danh sach hoc vien:")
for student_id, name, age in students:
    print(f"{student_id} - {name} ({age})")
print()


# Cau b: Tạo một list mới `python_scores` chỉ chứa tuple `(student_id, name, python_score)`
python_scores = []
for student_id, name, age in students:
    py_score = scores.get(student_id, {}).get("python", 0)
    python_scores.append((student_id, name, py_score))

print ("Diem mon Python cua tung hoc vien:")
for student_id, name, py_score in python_scores:
    print(f"{student_id} - {name}: {py_score}")
print()


#Cau c: Tìm học viên có điểm Python cao nhất từ `python_scores` và in ra: `Top Python: <name> - <score>`
if python_scores:
    top_student_id, top_name, top_score = python_scores[0]
    for student_id, name, py_score in python_scores:
        if py_score > top_score:
            top_student_id, top_name, top_score = student_id, name, py_score
    print(f"Top Python: {top_name} - {top_score}")
else:
    print("Khong co du lieu.") 

print()   


#Cau d: Thêm môn mới `"database"` vào `courses` (dùng set) và gán tạm điểm `database = 0` cho tất cả sinh viên trong `scores`
courses.add("database")
for student_id in scores:
    scores[student_id]["database"] = 0

print("Danh sach mon hoc hien co:", courses)
print("Diem cua tung hoc vien sau khi them mon 'database':")
for student_id, name, age in students:
    student_scores = scores.get(student_id, {})
    print(f"{student_id} - {name}: {student_scores}")