for i in range(1,4):#outer loop iterates from 1 to 3
    for j in range(i):#inner loop iterates from 0 to i-1
        print(f"Outer Loop iteration {i}, inner loop iteration{j+1}")

for i in range(4):#number of row
    for j in range(i):#no of columns
        print("*", end ="")
    print()