"""
args - Arguments not named
* - *args (pack and unpack)
"""
# Remember of unpacking
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# print(soma(x, y))

def soma(*args): # It packs what I send to the function in a tuple
    total = 0
    for numeros in args:
        # print('Total', total, numeros)
        total += numeros
        # print('Total', total)
    # print('Total da soma =',total)
    return total

soma1_5 = soma(1, 2, 3, 4, 5)
print(soma1_5)

print(sum((1, 2, 3, 4, 5))) # The 'sum' function takes at most 2 arguments, so we use a tuple in this example

numeros = 10, 20, 30, 40, 50 # tuple
print(numeros) # It is packaged
print(*numeros) #It is unpackaged / It unpacks the tuple to send as parameters to functions
print(sum(numeros)) # Since 'numeros' is packaged, we can use at the function 'sum'