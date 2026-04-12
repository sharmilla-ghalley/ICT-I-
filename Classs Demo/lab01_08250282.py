# Lab task on student information management system
students_list=[] #This list is to initialze the students name.
#The name is a key and the other dictionary (age + grade) is a value.
students_dict = {} #This dictionary contains complete student information inclusively age and grade.

#Helping one student by taking their input.
student_name=input("Enter the name of the student:")# Enter the name
student_age=input("Enter the age of the student:")# Enter the age
student_grade=input("Enter the grade of the student:")# Enter grade

#store student data
students_list.append(student_name) # add name to list
students_dict[student_name] = {"age": student_age, "grade":student_grade} #name=key and Age and Grade= value
print("Student's information has been added successfully!")#Feedback to user.

#Displaying all stored student information.
print("Student Details:") #Display student details.
for key, value in students_dict.items(): 
    # key = student name
    # value = dictionary containing age and grade
    print("Name:", key)
    print("Age:", value["age"])
    print("Grade:", value["grade"])

# searching students.
Search_name=input("Enter the name of the student you to search for:") #Search student 
#Check records
if Search_name in students_dict: #check name in the dict{}
    print("Student Found!")# if found print found
    print("Name:", Search_name)  #saerch name
    print("Age:", students_dict[Search_name]["age"])#access dict{} key name to access to get value
    print("Grade:", students_dict[Search_name]["grade"]) # access dict{} key name to access to get value
else:
    print("Student's detail not found!") #In case it's not found it will print out not found.

# Removinga student record.
remove_name=input("Enter the name of the student you want to remove:") #Allow the user the remove the student details
#removing the student's details from list and dictionary incase it's present.
if remove_name in students_dict: # Allows user to check of the entered name exist as a key in the dict{} before the removal process.
    students_list.remove(remove_name)# Ensure removal of the studnt's name if it is in the name list.
    del students_dict[remove_name]#  Allows the permanent deletion of the students record from the dictionary.
    print("Student's details removed successfully!")# If the record is found it will remove the studnt's detail from all data structure.
else:
    print("Student's details not found!") #If the record or data not found it will print out not found