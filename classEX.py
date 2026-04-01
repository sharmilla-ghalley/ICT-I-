
student_name = input("Enter Student Name: ")
days_borrowed = int(input("Enter number of days the book was borrowed: "))
days_late = int(input("Enter number of days late (0 if returned on time): "))

fine_per_day = 0

if days_late == 0:
    fine_per_day = 0
elif 1 <= days_late <= 5:
    fine_per_day = 5
elif 6 <= days_late <= 10:
    fine_per_day = 10
else: 
    fine_per_day = 20

total_fine = days_late * fine_per_day

warning_message = ""
if days_borrowed > 30:
    warning_message = "Library privileges may be restricted"

print("LIBRARY REPORT")
print(f"Student Name: {student_name}")
print(f"Days Borrowed:{days_borrowed}")
print(f"Days Late:{days_late}")
print(f"Total Fine:Nu. {total_fine}")

if warning_message:
    print(f"WARNING:{warning_message}")