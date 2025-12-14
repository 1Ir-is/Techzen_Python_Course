from datetime import datetime
from typing import List
from models import Task

DATE_FMT = "%Y-%m-%d"

def load_tasks(filename: str) -> List[Task]:
    tasks: List[Task] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(";")]
            if len(parts) != 3:
                print(f"Cảnh báo: Dòng {line_no} sai định dạng, bỏ qua: {line}")
                continue
            desc, due_str, status = parts
            try:
                due = datetime.strptime(due_str, DATE_FMT)
            except ValueError:
                print(f"Cảnh báo: Ngày không đúng format ở dòng {line_no}, bỏ qua: {line}")
                continue
            tasks.append(Task(desc, due, status))
    return tasks

def save_tasks(filename: str, tasks: List[Task]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for t in tasks:
            line = f"{t.description};{t.due_date.strftime(DATE_FMT)};{t.status}\n"
            f.write(line)

def add_task(tasks: List[Task], description: str, due_str: str) -> bool:
    try:
        due = datetime.strptime(due_str, DATE_FMT)
    except ValueError:
        return False
    tasks.append(Task(description, due, "todo"))
    return True

def mark_task_done(tasks: List[Task], index: int) -> bool:
    if 0 <= index < len(tasks):
        tasks[index].status = "done"
        return True
    return False
