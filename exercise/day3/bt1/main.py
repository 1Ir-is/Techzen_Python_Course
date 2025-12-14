from file_utils import read_file_content, count_word_frequency

def main() -> None:
    filename = input("Nhập tên file cần phân tích: ")
    try:
        content = read_file_content(filename)
    except FileNotFoundError:
        print("File không tồn tại")
        return
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return

    freq = count_word_frequency(content)
    total_words = sum(freq.values())
    print(f"Tổng số từ: {total_words}")

if __name__ == "__main__":
    main()
