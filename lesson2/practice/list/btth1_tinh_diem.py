scores = [7.5, 8.0, 6.5, 9.0, 8.5]

total = 0.0
max_score = scores[0]
min_score = scores[0]
for score in scores:
    total += score
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score
average_score = total/len(scores)

print("Diem trung binh: ", average_score)
print("Diem cao nhat: ", max_score)
print("Diem thap nhat: ", min_score)


# builtin
avg_score = sum(scores)/len(scores)
max_score = max(scores)
min_score = min(scores)
print("Diem trung binh: ", avg_score)
print("Diem cao nhat: ", max_score)
print("Diem thap nhat: ", min_score)

