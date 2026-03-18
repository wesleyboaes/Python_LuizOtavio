# Exercises
# Create functions that double, triple and quadruple numbers received as a parameter

# def double(number):
#     return number * 2

# def triple(number):
#     return number * 3

# def quadruple(number):
#     return number * 4

# print(double(3))
# print(triple(3))
# print(quadruple(3))

def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(5))
print(quadruple(5))