"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade
"""

if __name__ == '__main__':
    # Get the number of students
    n = int(input())

    # Create a nested list to store names and grades
    student_list = []

    # Input student names and grades
    for _ in range(n):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Find the second lowest grade
    scores = set(student[1] for student in student_list)
    second_lowest = sorted(scores)[1]

    # Filter students with the second lowest grade
    second_lowest_students = [student[0] for student in student_list if student[1] == second_lowest]

    # Print the names alphabetically
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
