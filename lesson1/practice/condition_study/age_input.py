try:
    age = int(input("Nhap tuoi: "))

    if age < 0:
        print("Tuoi khong hop le")
    elif age <= 11:
        print("Tuoi ban nhap la tre con!")
    elif age <= 17:
        print("Tuoi ban nhap la thieu nien!")
    elif age <= 30:
        print("Tuoi ban nhap la thanh nien!")
    else:
        print("Tuoi ban nhap la nguoi gia!")
except ValueError:
    print("Vui long nhap mot so nguyen hop le!")