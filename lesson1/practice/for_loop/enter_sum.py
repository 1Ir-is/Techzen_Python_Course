n = 0

while n < 0:
    try:
        n = int(input("Nhap n: "))
        if n >= 0:
            break
        print("Vui long nhap mot so nguyen khong am!")
    except ValueError:
        print("Invalid input. Vui long nhap mot so nguyen!")

total = 0
for i in range(1, n + 1):
    total += i

print("Tong cua cac so tu 1 den", n, "la:", total)
