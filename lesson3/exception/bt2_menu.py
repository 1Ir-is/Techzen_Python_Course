while True:
    try:
        print("Menu:")
        print("1. Xin chao!")
        print("2. Tinh chi so BMI")
        print("3. Thoat")
        choice = input("Chon mot option (1-3): ")

        if choice == "1":
            print("Xin chao!")
            continue
        elif choice == "2":
            print("Tinh chi so BMI")
            continue
        if choice == "3":
            print("Thoat chuong trinh.")
            break
    except ValueError:
        print("Lua chon khong hop le. Vui long chon lai.")