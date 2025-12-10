try:
    n = int(input("Nhap n: "))
    if n < 0:
        print("So khong hop le! ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Vui long nhap mot so nguyen hop le!")