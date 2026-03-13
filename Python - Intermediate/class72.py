# Functions exercises
# Create a function that multiplies all unnamed arguments received
# Return the total to a variable and shows the variable value
# Create a function that says if the number is even or odd and return it

def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

def even_odd(x):
    if x % 2 == 0:
        return x,'is even'
    return x,'is odd'
    
numbers = 1,2,3,4,5,6
print(*even_odd(multiply(*numbers)))