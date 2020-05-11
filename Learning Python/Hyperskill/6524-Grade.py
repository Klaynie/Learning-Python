student_score = int(input())
maximum_score = int(input())

ranges = [59, 60, 70, 80, 90]
grades = ['F', 'D', 'C', 'B', 'A']

relative_score = student_score / maximum_score * 100

if relative_score >= ranges[4]:
    print(grades[4])
elif relative_score >= ranges[3]:
    print(grades[3])
elif relative_score >= ranges[2]:
    print(grades[2])
elif relative_score >= ranges[1]:
    print(grades[1])
else:
    print(grades[0])