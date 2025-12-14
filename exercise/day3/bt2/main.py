from file_utils import calc_avg_score, find_top_student, filter_failed, load_students_from_file

def main() -> None:
    filename = input("Nhập tên file điểm sinh viên: ")
    try:
        students = load_students_from_file(filename)
    except FileNotFoundError:
        print("File không tồn tại")
        return
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return

    avg = calc_avg_score(students)
    top = find_top_student(students)
    failed = filter_failed(students)

    print(f"\nDiem trung binh: {avg:.2f}")
    if top:
        print("Sinh vien co diem cao nhat:")
        print(f"- {top}")
    else:
        print("Khong co sinh vien trong file.")

    print("\nDanh sach sinh vien bi rot:")
    if not failed:
        print("Khong co sinh vien nao bi rot.")
    else:
        for s in failed:
            print(f"- {s}")

if __name__ == "__main__":
    main()