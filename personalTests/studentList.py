'''
Q. WAP to take input of a given number of students in your class and arrange them
in A-Z
'''

# defining an empty student list which will contain all the names
studentList=[]
studentCount=int(input("Enter the number of students: "))
rollNumber=0
#studentNames=str(input("Enter the name of student: "))

for i in range (studentCount):
    studentList.append(input("Enter name of the students in any order: "))




studentList.sort()

print(*studentList, sep="\n")
