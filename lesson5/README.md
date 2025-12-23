# Todo API (DB version)

## 1. Cài môi trường venv và cài đặt dependencies

```powershell
# create venv
python -m venv .venv
# activate (PowerShell)
.\.venv\Scripts\Activate.ps1
# install
pip install -r requirements.txt
```

## 2. Khởi tạo biến môi trường

**Copy file mẫu `.env.example` thành `.env` và cập nhật thông tin kết nối:**

**Nội dung file `env.example`:**
```
POSTGRES_DB=techzen_academy
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_postgres_password_here
TZ=Asia/Ho_Chi_Minh
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
DATABASE_URL=postgresql+psycopg2://postgres:your_postgres_password_here@127.0.0.1:55432/techzen_academy
```
> Sau khi copy thành `.env`, chỉnh lại `POSTGRES_PASSWORD` cho đúng mật khẩu

## 3. Chạy Docker Compose (PostgreSQL)

```powershell
# from repo root
docker-compose up -d
```

## 4. Chạy Alembic migrations

```powershell
# ensure .venv active and alembic installed
alembic upgrade head
```

## 5. Seed sample data

```powershell
python -m scripts.seed_todo_data
```

## 6. Chạy app

```powershell
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

---

## Note

Laptop của em sử dụng **Python version 3.14** nên khi chạy app thì bị lỗi version với `pydantic` và `fastapi`.  
Để chạy được ứng dụng này trên Python 3.14, em đã cài các phiên bản mới nhất của hai package như sau:

```bash
pip install --upgrade "fastapi>=0.111.0" "pydantic>=2.6.4"
```
