#list
name=input("Enter your name:")
for i in name:
    print(i)

li=["python programming", "python fundamentals", "python interview questions"]
for x in li: #element
    print(x)
#range
lenli=len(li)#lenli return no of items in list(3) stored in variable
for x in range(lenli): #value of each variable that takes value of each index
    print(li[x])

#tuple
my_tuple=tuple(li)
for x in my_tuple:
    print(x)

lenmy_tuple=len(my_tuple)
for x in range(lenmy_tuple):
    print(my_tuple[x])

#set
my_set={type(li)}
my_set = set(li)
for x in my_set:
    print(x)

#lenset=len(my_set)
#for x in range(lenset):
    #print(my_set[x])#error as set is unordered 