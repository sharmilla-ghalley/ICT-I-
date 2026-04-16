#count down timer. write a program using while loop that prints numbers from 10 to 1nand then print "Time up!"
i = 10

while i >= 1:
    print(i)
    i -= 1  # Subtract 1 from i(count)each time

print("Time's up!")

#Sum until Zero: Write a program that keeps taking integer input from the user and add them to a total. Stop when the user enters 0. Finally ,print the total sum
i = 0
while True:
        number = int(input("Enter an integer (enter 0 to stop): "))
        
        if number == 0:
            break
        i+=number      
    
print(f"The total sum is:", i)

#crate a program where the correct user name is "admin" and password is "1234" 
#the user gets only three Attempt. i correct, print"login successful" otherwise print"login failed"
correct_user = "admin"
correct_password = "1234"
attempts = 3

for i in range(attempts):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    
    if username == correct_user and password == correct_password:
      print("Login successful")
      break
    else:
        print(f"wrong credentials! attempts left:{attempts -i-1}")

    if i==attempts-1:
        print("Account locked!")
    
