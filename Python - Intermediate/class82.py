def execute(function, *args):
    return function(*args)

##################################

# def sum(x, y):
#     return x + y

##################################

# def create_multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply

##################################

# double = create_multiplier(2)
# print(double(3))
double = execute(
    lambda m: lambda n: m * n,
    2
)
print(double(3))

soma = execute(
        lambda x, y: x + y,
        2, 3
    )
print(soma)

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
