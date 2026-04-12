# Lab task on student information management system
students_list=[] #This list is to initialze the students name.
#The name is a key and the other dictionary (age + grade) is a value.
students_dict = {} #This dictionary contains complete student information inclusively age and grade.

#Helping one student by taking their input.
student_name=input("Enter the name of the student:")#user the enter the name oof the required students.
student_age=input("Enter the age of the student:")#user can enter the age of the student
student_grade=input("Enter the grade of the student:")#Now user can enter the grade of the student.

#storing the data(name,age and grade) of the student.
students_list.append(student_name) # this is a procees to add the name of the students to the list.
students_dict[student_name] = {"age": student_age, "grade":student_grade} #name=key and Age and Grade= value
print("Student's information has been added successfully!")#Enabling the user to know whether the saving of data was successful or not.

#Displaying all stored student information.
print("Student Details:") #Allowing the users to view the sored student information.
for key, value in students_dict.items(): ## This loop goes through every student in the dictionary, separating their name (key) from their age and grade (value) to show them one by one.
    # key = student name
    # value = dictionary containing age and grade
    print("Name:", key)
    print("Age:", value["age"])
    print("Grade:", value["grade"])

# Find student.
Search_name=input("Enter the name of the student you to search for:") #Allow user to find the student 
#Checking the presence of the student in the records.
if Search_name in students_dict: #check if the name entered is in the dict{} as a key
    print("Student Found!")# If it's there then it will print the data(name, age and grade) 
    print("Name:", Search_name)  # Display the name that was searched
    print("Age:", students_dict[Search_name]["age"])#Access to Dict{} using the key(name) to get the value(age) and print it.
    print("Grade:", students_dict[Search_name]["grade"]) # Access the dict{} through the key(name) to get accessed to value(grade)
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
    print("Student's details not found!") #If the record or data not found it will print out not found.