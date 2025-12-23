from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.todo import Todo


SAMPLE = [
    {"title": "Buy milk", "description": "2 liters", "priority": 2, "done": False},
    {"title": "Read book", "description": "Read FastAPI docs", "priority": 3, "done": False},
    {"title": "Exercise", "description": "30 minutes run", "priority": 4, "done": False},
    {"title": "Pay bills", "description": "Electricity and internet", "priority": 1, "done": False},
    {"title": "Call mom", "description": "Weekly call", "priority": 5, "done": False},
]


def seed():
    db: Session = SessionLocal()
    try:
        count = db.query(Todo).count()
        if count == 0:
            for item in SAMPLE:
                todo = Todo(**item)
                db.add(todo)
            db.commit()
            print("Seeded sample todos")
        else:
            print("DB not empty, skipped seeding. Count:", count)
    finally:
        db.close()


if __name__ == '__main__':
    seed()
