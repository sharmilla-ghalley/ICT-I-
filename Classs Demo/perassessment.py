students_list = []  # creating an empty list
students_dict = {}  # creating an empty dictionary

# adding initial students
students_list.append("Xdorji")
students_list.append("Sangay")
students_list.append("Pema")
students_dict["Xdorji"] = {'age': 22, 'grade': 'A'}
students_dict["Sangay"] = {'age': 26, 'grade': 'B'}
students_dict["Pema"] = {'age': 27, 'grade': 'C'}

# add student
add_student = input("Enter the student name to add or press enter to skip: ")
add_age = input("Enter the age of the student: ")
add_grade = input("Enter the grade of the student: ")
if add_student:
    students_list.append(add_student)
    students_dict[add_student] = {"age": add_age, "grade": add_grade}
    print(f"Student added successfully! The age of '{add_student}' is {students_dict[add_student]['age']} and grade is {students_dict[add_student]['grade']}.")
else:
    print("No students are added any more")
print() # print a space.

# search student
search_name = input("Enter the name to search: ")
if search_name in students_list:
    print(f"Student found! The age of '{search_name}' is {students_dict[search_name]['age']} and grade is {students_dict[search_name]['grade']}.")
else:
    print("Student not found!")
print()# print a space.

# remove student
remove_student = input("Enter the student name to remove or press enter to skip: ")
if remove_student in students_list:
    students_list.remove(remove_student)
    del students_dict[remove_student]
    print("Student removed successfully!")
    print("Students left with details:", students_dict)
    print("List of students left:", students_list)
else:
    print("Student not found!")
print()# print a space