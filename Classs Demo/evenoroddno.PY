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

# b. Function to calculate total
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

# c. Function to calculate average
def calculate_average(total):
    return total / 3

# d. Function to check pass/fail
def check_result(average):
    if average >= 50:
        return "Congratulations!You are Pass"
    else:
        return "You failed this semster try again"

#write a function check_even_odd(num)that:
#1.Return "Even" if numbers is even. 2.Return"Odd" otherwise
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return"Odd"
number= int(input("enter a numberto check:"))
print(f"The number is {check_even_odd(number)},")

