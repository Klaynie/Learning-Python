def average_mark(*marks):
    total = 0
    for mark in marks:
        total += mark
    return round(total / len(marks), 1)

print(average_mark(3, 4, 5, 3))