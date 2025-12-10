nested_list = [[1, 2, 3], [4, 5], [6]]

flat_list = []

for sub in nested_list:
    for item in sub:
        flat_list.append(item)

print("Danh sách phẳng:", flat_list)
