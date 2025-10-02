"""
Make a program that asks the user to type an integer, 
informs whether the number is even or odd. If the user 
do not type an integer, tell them that is not an integer.
"""

# number = input('Enter an integer: ')

# if number.isdigit():
#     int_number = int(number)
#     if int_number % 2 == 0:
#         print('It is even!')
#     else:
#         print('It is odd!')
# else:
#     print('It is not an integer!')

"""
Make a program that asks the user for the time and, based 
on the time specified, displays the appropriate greeting.
E.g. Good Morning 0-11, Good Afternoon 12-17, Good Evening
18-23.
"""

# hour = input('Type the hour as an integer: ')

# try:
#     int_hour = int(hour)
#     if int_hour >= 0 and int_hour <= 11:
#         print('Good morning!')
#     elif int_hour >= 12  and int_hour <= 17:
#         print('Good afternoon!')
#     elif int_hour >= 18 and int_hour <= 23:
#         print('Good evening!')
#     else:
#         print('It is not a valid hour!')
# except:
#     print('It is not an integer!')

"""
Make a program that asks the first name of the user. If the
name has 4 letters or less, write "Your name is short";
If has between 5 and 6 letters, write "Your name is normal";
more than 6 letters, write "Your name is too long".
"""

# first_name = input('Enter your first name: ')
# letters = len(first_name)

# if letters <= 4:
#     print('Your name is short!')
# elif letters > 6:
#     print('Your name is too long')
# else:
#     print("Your name is normal")