""""
CPF = 168.995.350-09
"""""
cpf = '16899535009'


# Digito 1
y = 10
soma = 0
soma_total = 0
cont = 0

for x in cpf:
    if cont < 9:
        soma = int(x) * y
        y -= 1
        soma_total += soma
        cont += 1
    else:
        break

if 9 < (11 - (soma_total % 11)):
    digito1 = 0
else:
    digito1 = 11 - (soma_total % 11)


# Digito 2
y = 11
soma = 0
soma_total = 0
cont = 0

for x in cpf:
    if cont < 10:
        soma = int(x) * y
        y -= 1
        soma_total += soma
        cont += 1
    else:
        break

if 9 < (11 - (soma_total % 11)):
    digito2 = 0
else:
    digito2 = 11 - (soma_total % 11)



novo_cpf = (cpf[0:9] + str(digito1) + str(digito2))
if novo_cpf == cpf:
    print('Este cpf é válido')
else:
    print('Este cpf é inválido')

