#Write a program using functions to:
#a.input marks of 3 subjects, b.create a function calculate_total(m1,m2,m3)
#c.create another function calculate_avergae(total)
#d.print result of stds according to the average (if average>=50: return pass, else return fail)

# a. Function to input marks (using main)
def get_marks():
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))
    return m1, m2, m3
m1,m2,m3=get_marks()
# b. Function to calculate total
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
total=calculate_total(m1, m2, m3)

# c. Function to calculate average
def calculate_average(total):
    return total / 3
average=calculate_average(total)

# d. Function to check pass/fail
def check_result(average):
    if average >= 50:
        return "Congratulation! You are pass"
    else:
        return "You have failed this semester try again"
    check_result(average)
print(f"Your result is {check_result(average)}")
