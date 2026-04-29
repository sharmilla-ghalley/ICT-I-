

#write a function check_even_odd(num)that:
#1.Return "Even" if numbers is even. 2.Return"Odd" otherwise
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return"Odd"
number= int(input("enter a number to check:"))
print(f"The number is {check_even_odd(number)}.")

