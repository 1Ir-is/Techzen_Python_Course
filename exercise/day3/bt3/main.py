# python
from datetime import datetime
from task_service import load_tasks, save_tasks, add_task, mark_task_done
from typing import List

TASK_FILE = "tasks.txt"

def print_all(tasks: List, ) -> None:
    if not tasks:
        print("Không có task.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def print_overdue(tasks: List) -> None:
    now = datetime.now()
    overdue = [t for t in tasks if t.is_overdue(now)]
    if not overdue:
        print("Không có task quá hạn.")
        return
    for i, t in enumerate(overdue, start=1):
        print(f"{i}. {t}")

def main() -> None:
    try:
        tasks = load_tasks(TASK_FILE)
    except FileNotFoundError:
        print("File không tồn tại. Tạo file mới khi lưu.")
        tasks = []
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return

    while True:
        print("\n1. Xem tất cả task")
        print("2. Xem các task quá hạn")
        print("3. Thêm task mới")
        print("4. Đánh dấu task là done")
        print("5. Thoát")
        choice = input("Chọn: ").strip()

        if choice == "1":
            print_all(tasks)

        elif choice == "2":
            print_overdue(tasks)

        elif choice == "3":
            desc = input("Mô tả: ").strip()
            due_str = input("Ngày hạn (YYYY-MM-DD): ").strip()
            if not add_task(tasks, desc, due_str):
                print("Ngày không đúng định dạng. Không thêm.")
            else:
                try:
                    save_tasks(TASK_FILE, tasks)
                    print("Đã thêm và lưu vào file.")
                except Exception as e:
                    print(f"Lỗi khi lưu file: {e}")

        elif choice == "4":
            if not tasks:
                print("Không có task để đánh dấu.")
                continue
            print_all(tasks)
            try:
                idx = int(input("Nhập số thứ tự task cần đánh dấu: ").strip()) - 1
            except ValueError:
                print("Giá trị nhập không hợp lệ.")
                continue
            if mark_task_done(tasks, idx):
                try:
                    save_tasks(TASK_FILE, tasks)
                    print("Đã đánh dấu done và lưu file.")
                except Exception as e:
                    print(f"Lỗi khi lưu file: {e}")
            else:
                print("Số thứ tự không hợp lệ.")

        elif choice == "5":
            print("Thoát.")
            break

        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
