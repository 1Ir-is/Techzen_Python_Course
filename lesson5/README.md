# Todo API (DB version)


1. Cài môi trường venv và cài đặt dependencies

```powershell
# create venv
python -m venv .venv
# activate (PowerShell)
.\.venv\Scripts\Activate.ps1
# install
pip install -r requirements.txt
```

2. Chạy Docker Compose (PostgreSQL)

```powershell
# from repo root
docker-compose up -d
```

3. Chạy Alembic migrations

```powershell
# ensure .venv active and alembic installed
alembic upgrade head
```

4. Seed sample data

```powershell
python -m scripts.seed_todo_data
```

5. Chạy app

```powershell
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Note
Laptop của em sử dụng **Python version 3.14** nên khi chạy app thì bị lỗi version với `pydantic` và `fastapi`.  
Để chạy được ứng dụng này trên Python 3.14, em đã cài các phiên bản mới nhất của hai package như sau:

```bash
pip install --upgrade "fastapi>=0.111.0" "pydantic>=2.6.4"
```
