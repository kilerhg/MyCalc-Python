# Neste arquivo irá todas as funções necessarias para o funcionamento da calculadora

# Operações Aritmeticas

def soma(*numeros):
    s = 0
    for x in numeros:
        s += x
    return s


def subtrair(*numeros):
    s = 0
    for x in numeros:
        s -= x
    return s


def multiplicar(*numeros):
    m = 0
    for x in numeros:
        m *= x
    return m


def dividir(*numeros):
    d = 0
    for x in numeros:
        d /= x
    return d


def potencia(numero, grau=2):
    r = numero ** grau
    return r


def raiz(numero, grau=2):
    r = numero ** (1/grau)
    return r

# Verificadores / Conversores / Funções Extras


def inverte_sinal(numero):
    if verifica_numero(numero):
        numero = float(br_to_us(numero))
        numero *= -1
    return numero


def verifica_numero(numero):
    r = bool()
    numero = br_to_us(numero)
    try:
        numero = float(numero)
        r = True
    except:
        r = False
    return r


def br_to_us(numero):
    try:
        numero = str(numero).strip().replace(',', '.', 1)
    except:
        pass
    return numero


def us_to_br(numero):
    try:
        numero = str(numero).strip().replace('.',',',1)
    except:
        pass
    return numero
