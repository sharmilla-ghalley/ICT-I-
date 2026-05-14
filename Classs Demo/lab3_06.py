# Lab03_6.py - File Handling Assignment
# Purpose: Read student data and find students with EVEN ID numbers (Group 6)

# Open the students.txt file in read mode so we can get the data
file = open("students.txt", "r")

# Read all the lines from the file into a list called 'lines'
lines = file.readlines()

# Close the file because we are done reading it
file.close() 


# Create an empty list to store the students we find that match Group 6
selected_students = []

# Get the first line of the file (the header) - it tells us what each column means
# The header is something like: "Serial Number,Student Name,Student ID"
header = lines[0].strip()
print(f"File Header: {header}\n")
# Start from line 1 (skip line 0 because that is the header row)
for line in lines[1:]:

    # Skip empty lines (lines with no data at all)
    if not line.strip():
        continue

    # Split each line using comma (,) as a separator
    # Example: "1,Sonam Tobgay,8250284" → ["1", "Sonam Tobgay", "8250284"]
    data = line.strip().split(",")

    # Check if we have exactly 3 parts (Serial, Name, ID)
    # If not, skip this line because the data format is wrong
    if len(data) != 3:
        continue

    # Unpack the three parts into separate variables
    serial, name, student_id = data

    # Print the student details neatly
    print(f"Serial: {serial}, Name: {name}, ID: {student_id}")
        # Try to convert the student ID from text to a number so we can do math with it
    try:
        sid = int(student_id)
    except ValueError:
        # If the conversion fails (e.g., ID is not a number), skip this student
        continue

    # Check if the ID number is EVEN (Group 6 rule)
    # If a number divided by 2 has no remainder (% 2 == 0), it is even
    if sid % 2 == 0:
        # This student belongs to Group 6, so add them to our list
        selected_students.append((serial, name, student_id))

# Sort the students by their ID from smallest to largest
# This helps us find the first and last students
selected_students.sort(key=lambda x: int(x[2]))

# Print a nice title
print("Group 6 Selection: Even Student IDs")
print("=" * 60)

# Show how many students are in Group 6
print(f"\nTotal number of students assigned to Group 6: {len(selected_students)}")

# If we found any students, show their information
if selected_students:
    # Show the names of all the students in Group 6
    print("\nNames of selected students:")
    for s in selected_students:
        print(f"  - {s[1]}")

 # Show the first student (the one with the lowest ID number)
    print(f"\nFirst Student according to the Student ID:")
    print(f"  {selected_students[0][1]} ({selected_students[0][2]})")

    # Show the last student (the one with the highest ID number)
    print(f"\nLast Student according to the Student ID:")
    print(f"  {selected_students[-1][1]} ({selected_students[-1][2]})")
else:
    # If no students found
    print("No students match Group 6 criteria.") 
