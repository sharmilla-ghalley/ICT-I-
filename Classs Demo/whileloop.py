no_of_students=int(input("Enter the number of students:"))
i=1
student_names={}
while i<=no_of_students:
    name=input("Enter the names of the student:")
    print("the name of the students{} is {}".format (i,name))
    i+=1
    student_names[1]=name
print(student_names)
