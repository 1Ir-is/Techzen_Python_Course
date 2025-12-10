s = input("Nhập câu: ")

# Bỏ khoảng trắng thừa, đưa về 1 dấu cách giữa các từ
words = s.strip().split()
s1 = ' '.join(words)

# Viết hoa chữ cái đầu câu, còn lại viết thường
s1 = s1.capitalize()

# Đảm bảo kết thúc bằng 1 dấu "."
s1 = s1.rstrip('.')
s1 += '.'

print("Câu chuẩn hóa:", s1)