name=input("Enter your name:")
greet=lambda x: print("Hello", x)
greet(name)

#use case of lamda
even_odd= lambda x: "even" if x%2==0 else"Odd"
num=int(input("Enter a number:"))
print(even_odd(num))

#return multiple result
arith=lambda x,y:(x+y, x-y, x*y, x/y)
num1=int (input("Enter first number:"))
num2=int(input("ENter the second number:"))
print(arith(num1,num2))

#filter()
mylist=[1,2,3,4,5,6]
even=filter(lambda x: x% 2==0, mylist)
print(list(even))

