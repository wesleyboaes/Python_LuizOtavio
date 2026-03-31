# Lambda function in Python
# A lambda function is like any other function in Python. 
# However, they are anonymous functions that only have one line.
# That is, everything must be contained within a single expression.
# list = [
#     {'name': 'Wesley', 'last_name': 'Boaes'},
#     {'name': 'Maiara', 'last_name': 'Boaes'},
#     {'name': 'Sophia', 'last_name': 'Boaes'},
#     {'name': 'Theo', 'last_name': 'Boaes'},
# ]

# list = [4, 32, 1, 34, 5, 6, 6, 21]
# list.sort()
# # sorted(list)
# print(list)

# list.sort(reverse=True)
# print(list)

list = [
    {'name': 'Wesley', 'last_name': 'Boaes'},
    {'name': 'Maiara', 'last_name': 'Boaes'},
    {'name': 'Sophia', 'last_name': 'Boaes'},
    {'name': 'Theo', 'last_name': 'Boaes'},
]

def show_list(list):
    for item in list:
        print(item)
    print()

# def orderBy_name(item):
#     return item['name']
# list.sort(key=orderBy_name)
# list.sort(key=lambda item: item['name'])
l1 = sorted(list, key=lambda item: item['name']) # sorted() returns a shallow copy
l2 = sorted(list, key=lambda item: item['last_name'])

# def orderBy_last_name(item):
#     return item['last_name']
# list.sort(key=orderBy_last_name)
# list.sort(key=lambda item: item['last_name'])

show_list(l1)
show_list(l2)

# for item in list:
#     print(item)