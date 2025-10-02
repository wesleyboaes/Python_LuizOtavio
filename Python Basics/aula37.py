"""
Assignment operators
= += -= *= /= //= **= %=
"""
counter = 0

while counter <= 100:
    counter += 1

    if counter == 6:
        print('Where is six?')
        continue
    
    if counter >= 10 and counter <= 20:
        continue

    print(counter)

    if counter == 40:
        break

print('It is over!')
