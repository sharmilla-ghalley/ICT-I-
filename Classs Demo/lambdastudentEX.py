#implement create a lambda function for the following: 
#a. check whether a number is positive, negative or zero. let user input using if and else.

number= int(input("Enter a number:"))
check=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(check(number))


