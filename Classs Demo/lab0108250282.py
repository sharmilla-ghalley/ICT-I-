#Student Information Management System.
students_list = [] #Initializing empty list to store only the names of students.

#The name is a key and the other dictionary (age + grade) is a value.
students_dict = {} #This dictionary contains complete student information inclusively age and grade.

#Helping one student by taking their input.
name = input("Enter student name: ") #You can enter the names of the student that you want to add.
age = input("Enter student age: ") #Enter the age of the student.
grade = input("Enter student grade: ") #Finally enter the grade of the student.

#Saving the student data.
students_list.append(name) # Adding the names of the student to the list.
students_dict[name] = {"age": age, "grade": grade} #Adding name as key and grade and age as value to dict{}

#Indicate to the user that the data was saved.
print("Student information has been added successfully!") #this line passes the message to user that the data is stored successfully.

#Displaying all stored student information.
print("Student Details:") #Allowing the users to view the sored student information.
for key, value in students_dict.items(): ## This loop goes through every student in the dictionary, separating their name (key) from their age and grade (value) to show them one by one.
    # key = student name
    # value = dictionary containing age and grade
    print("Name:", key)
    print("Age:", value["age"])
    print("Grade:", value["grade"])

# Find student.
search_name = input("Enter the name of the student to be searched: ") # Allowing the user to search for a student by their name

# Check whether or not student is in the records.
if search_name in students_dict: #Check if the name entered by the user exists as a key in our dict{}.
    print("Student Found!")# If found, it will display the student's name, age, and grade. 
    print("Name:", search_name) # # Display the student's name that was searched for
    print("Age:", students_dict[search_name]["age"])# Access the dict{} using the name to show the specific 'age' value
    print("Grade:", students_dict[search_name]["grade"]) # Access the dict{} using the name to pull out the specific 'grade' value
else:
    print("Student not found!") # If not found, it will display "student not found"

# Removinga student record.
remove_name = input("Name of student to remove: ")  #Allowing the user to remove a student from the system by entering their name.

# Remove student from list and dictionary, in case student exists.
if remove_name in students_dict: # Check if the student's name exists as a key in our dictionary before trying to delete
    students_list.remove(remove_name)# Remove the student's name from the list of names
    del students_dict[remove_name]# Permanently delete the student's entire record (age and grade) from the dictionary
    print("Student removed successfully!")# If found, it will remove the student's information from all data structures. 
else:
    print("Student not found!") #If not found, it will display "student not found".