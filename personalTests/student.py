
sCount=int(input("Enter total number of students: "))
print("Total students are: ",sCount)

studentName=[]
def studentEntry():
    studentName=[input("Enter the student name: ")]
    
for i in range(sCount):
    studentEntry()
    return studentName

print(studentName)

