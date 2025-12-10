def factorial(n):
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return kq

n = int(input("Nhập n: "))
S = 0
for i in range(n):
    S += 1 / factorial(2*i + 1)
print("Tổng S =", S)