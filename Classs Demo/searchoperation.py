detail = open("student.txt", "w")
detail.write("Sarmilla:08250282\n")
detail.write("Sonia:08250283\n")
detail.write("Solta:08250284\n")
detail.write("DharMith:08250285\n")
detail.write("Allay:08250286\n")
detail.close()

print("Dummy file 'student.txt' created successfully!")


with open("student.txt", "r") as f:
    students = f.readlines()
search_name = input("Enter student name to search: ")

found = False
for line in students:
    if search_name.lower() in line.lower():  
        print("Student found")
        found = True
        break

if not found:
    print("Student not found in the file.")