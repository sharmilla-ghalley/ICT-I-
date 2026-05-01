from functools import reduce
mylist= [1,2,3,4]
mul= reduce(lambda x,y: x*y, mylist)
print(mul)