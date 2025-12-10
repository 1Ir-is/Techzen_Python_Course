try:
    s = input("Enter a string: ")
except ValueError:
    s = " "

count = 0
for char in s:
    if char == 'a':
        count += 1
print("Number of 'a' in the string: ", count)