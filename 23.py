students=["chandan","darshan","puni"]
marks=[25,98,100]
students_marks={}
for index, students in enumerate(students):
    students_marks[students]=marks[index]
print(students_marks)


students=["chandan","darshan","puni"]
marks=[25,98,100]
students_marks={}
for i in range(len(students)):
    students_marks[students[i]]=marks[i]
    print(students_marks)



    students=["chandan","darshan","puni"]
marks=[25,98,100]
students_marks={}
for i in range(len(students)):
    students_marks[students[1]]=marks[i]
    print(students_marks)