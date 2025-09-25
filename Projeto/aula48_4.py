"""
Cares with changeable data
= - value copied (unchangeable)
= - points to the same value in memory (changeable)
"""

lista_a = ['Wesley', 'Pimenta', 'Boaes']
lista_b = lista_a # Here I am pointing lista_b to the same place of lista_a
lista_a[0] = 'anything' # Now I am changing the index 0 value
print('Lista B:',lista_b) # With this, I point to the changed place

lista_c = ['Wesley', 'Pimenta', 'Boaes']
lista_d = lista_c.copy() # Now I am copying the value to lista_d
lista_c[0] = 'another thing'
print('Lista C:',lista_c)
print('Lista D:',lista_d)