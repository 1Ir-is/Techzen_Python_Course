nums = [5, -2, 8, -1, 0, 3, -10]

non_negative = [n for n in nums if n >= 0]
print("Danh sách sau khi xóa số âm:", non_negative)

# Duyet copy
for x in nums[:]:
    if x < 0:
        nums.remove(x)

print("Danh sách sau khi xóa số âm (duyệt bản sao):", nums)