nome = 'Wesley Boaes'
altura = 1.73
peso = 96
imc = peso / (altura ** 2)

print(nome, 'tem', str(altura) + 'm', 'de altura, pesa', peso, 'quilos e seu IMC é', imc)

"f-strings"
linha = f'{nome} tem {altura:.2f}m de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha)

# Wesley Boaes tem 1.73m de altura, pesa 96 quilos e seu IMC é 32.075912994086