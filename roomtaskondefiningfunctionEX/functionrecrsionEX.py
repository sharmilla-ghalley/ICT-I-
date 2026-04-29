def sum(n):
    if n==1: #base condition
        return 1
    else: #recursive call
        return n+sum(n-1)

n= int(input("Enter a number:"))
print("Sum of numbers from 1 to", n, "is:", sum(n))

 #eg 2
def fact(n):
    #base condition
    if n==0:
       return 1

#recursive call
    else:
        return n*fact(n-1)
print("Factorial of 5:", fact(5))