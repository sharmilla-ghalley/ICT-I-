#1. write a recursive function fun1(x,y) such that:
#a.if x becomes 0, the function returns the value of y
#b. otherwise, the function calls itself by:
#1. deccreasing x by 1
#2. adding the current value of x to y
#Eg: when 1=5 and y=2, the function should compute:
#2+5+4+3+2+1=17

def fun1(x,y):
    if x==0:
        return y
    else:
        return fun1(x-1, x+y)
x=int(input("Enter a number for x:"))
y=int(input("Enter a number for y:"))

result=fun1(x,y)
print("The result of fun1 is:", result)
