# python
from datetime import datetime

class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status.lower() if status else "todo"

    def is_overdue(self, now: datetime) -> bool:
        return self.status != "done" and self.due_date < now

    def __str__(self) -> str:
        tag = "[DONE]" if self.status == "done" else "[TODO]"
        return f"{tag} {self.description} (Hạn: {self.due_date.strftime('%Y-%m-%d')})"
