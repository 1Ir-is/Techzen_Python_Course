s = "hello world"

counter = {}

for char in s:
    counter[char] = counter.get(char, 0) + 1

print(counter)