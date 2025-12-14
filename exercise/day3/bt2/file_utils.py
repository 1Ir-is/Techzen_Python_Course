from typing import List, Optional

class Student:
    def __init__(self, name: str, age: int, score: float) -> None:
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self) -> bool:
        return self.score >= 5.0

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.score}"

def load_students_from_file(filename: str) -> List[Student]:
    students: List[Student] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    print(f"Bo qua dong: {line}")
                    continue
                name = parts[0]
                try:
                    age = int(parts[1])
                    score = float(parts[2])
                except ValueError:
                    print(f"Khong parse age/score, bo qua: {line}")
                    continue
                students.append(Student(name, age, score))
    except FileNotFoundError:
        print("File tim khong thay")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    return students

def calc_avg_score(students: List[Student]) -> float:
    if not students:
        return 0.0
    return sum(s.score for s in students) / len(students)

def find_top_student(students: List[Student]) -> Optional[Student]:
    if not students:
        return None
    top = students[0]
    for s in students[1:]:
        if s.score > top.score:
            top = s
    return top

def filter_failed(students: List[Student]) -> List[Student]:
    return [s for s in students if not s.is_passed()]
