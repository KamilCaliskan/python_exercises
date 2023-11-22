if name == 'main':
# Input the number of students
n = int(input("Enter the number of students: ").strip())

# Create a list to store student information
students = []

# Input student names and grades
for _ in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append([name, grade])

# Find the second lowest grade
grades = set([student[1] for student in students])
second_lowest_grade = sorted(grades)[1]

# Find students with the second lowest grade
students_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_grade]

# Print the names in alphabetical order
students_with_second_lowest.sort()
for student in students_with_second_lowest:
    print(student)
