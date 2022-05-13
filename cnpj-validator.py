def adiciona(soma, cnpj):
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    return cnpj + str(digito1)


def e_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True


def valida(cnpj_org):
    cnpj = (cnpj_org)[:-2]
    lista_verificadora = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = sum([lista_verificadora[i+1] * int(n) for i, n in enumerate(cnpj)])
    novo_cnpj = adiciona(soma, cnpj)
    soma = sum([lista_verificadora[i] * int(n) for i, n in enumerate(novo_cnpj)])
    novo_cnpj = adiciona(soma, novo_cnpj)

    if novo_cnpj != cnpj_org:
        print('Inválido')
    elif e_sequencia(cnpj_org):
        print('Sequências não são válidas')
    else:
        print('Válido')

# CNPJ somente numeros no formato string:
# valida('')
