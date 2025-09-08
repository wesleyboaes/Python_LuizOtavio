# Logical Operators
# and (e) or (ou) not (não)
# and - All the conditions must be true.
# If any value is considered false, the entire expression will be evaluated at that value.
# Are considered falsy (that you've seen): 0 | 0.0 | '' | False
# There is also the None type, witch is used to represent a non-value.

# entry = input('[E]nter [L]eft: ')
# typed_password = input('Password: ')
# permitted_password = '123456'


# if (entry == 'E' or entry == 'e') and typed_password == permitted_password:
#     print('Enter')
# else:
#     print('Left')

# Short Circuit Evaluation => Checks up to the first FALSE value.
# If all values are TRUE, the last one is returned.
password = input('Password: ') or 'No password'
print(password)