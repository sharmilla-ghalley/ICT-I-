#Design a Pattern Using Recursion.Create a recursive function that:Calls itself with a smaller 
# value(n-1) until it reaches 1
#After returning from recursion, prints stars in increasing order
#Eg:  for n = 4:
#*
#*  *
#*  *  *
#*  *  *  *

def draw_pattern(n):
    # Base Case: Stop when n is 0
    if n == 0:
        return
    
    # Recursive Call: Move toward the base case (n-1)
    draw_pattern(n - 1)
    
    # After returning from recursion, print the stars
    print("* " * n)

# Example Usage
n = 4
draw_pattern(n)