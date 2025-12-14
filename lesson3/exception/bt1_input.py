while True:
    try:
        s = input("Nhap so: ")
        n = int(s)
        if n > 0:
            print(f"Ban da nhap: {n}")
            break
        print("Vui long nhap so nguyen duong.")
    except ValueError:
        print("Nhap khong hop le. Vui long nhap mot so nguyen.")