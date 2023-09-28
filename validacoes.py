import re



def validar_nome(nome):
    if re.match('^[A-Za-zÀ-ÿ ]*$', nome):
        palavras = nome.split()
        for i in range(len(palavras)):
            if len(palavras[i]) > 2:
                palavras[i] = palavras[i].title()

        nome = ' '.join(palavras)
        return nome
    else:
        print('Nome inválido. Por favor, insira um nome válido.')
        return False


def validar_cpf(cpf):
    # Remova pontos e traços do CPF e verifique se sobram apenas dígitos
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False

    # Verifique se todos os dígitos são iguais (um CPF inválido)
    if len(set(cpf)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    total = 0
    for i, digito in enumerate(cpf[:9]):
        total += int(digito) * (10 - i)
    resto = total % 11
    if resto < 2:
        digito_esperado1 = 0
    else:
        digito_esperado1 = 11 - resto

    # Calcula o segundo dígito verificador
    total = 0
    for i, digito in enumerate(cpf[:10]):
        total += int(digito) * (11 - i)
    resto = total % 11
    if resto < 2:
        digito_esperado2 = 0
    else:
        digito_esperado2 = 11 - resto

    # Verifique se os dígitos verificadores calculados correspondem aos dígitos reais
    return int(cpf[9]) == digito_esperado1 and int(cpf[10]) == digito_esperado2


def validar_email(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return email
    else:
        print('E-mail inválido. Por favor, insira um e-mail válido.')
        return False
