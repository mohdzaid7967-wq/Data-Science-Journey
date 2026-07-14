'''
Question 1: Student Marks

Create a dictionary of student names and marks. Print the student with the highest marks.
'''

student = {
    "Zaid" : 92,
    "Ali" : 99,
    "Hammad" : 88
}

top_student = max(student, key=student.get)

print("Student with the highest marks:", top_student)
print("Marks:", student[top_student])