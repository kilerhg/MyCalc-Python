# Neste arquivo irá todas as funções necessarias para o funcionamento da calculadora

# Operações Aritmeticas

def soma(numero1,numero2):
    s = 0
    s = numero1 + numero2
    return formatar_saida(s)


def subtrair(numero1,numero2):
    s = 0
    s = numero1 - numero2
    return formatar_saida(s)


def multiplicar(numero1,numero2):
    m = 0
    m = numero1 * numero2
    return formatar_saida(m)


def dividir(numero1 , numero2):
    d = 0
    if numero1 == 0 or numero2 == 0:
        pass
    else:
        d = numero1 / numero2
    return formatar_saida(d)


def potencia(numero, grau=2):
    r = numero ** grau
    return formatar_saida(r)


def raiz(numero, grau=2):
    r = numero ** (1/grau)
    return formatar_saida(r)

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


def float_vazio(numero):
    numero = str(numero)
    finalnumero = numero[-2:]
    if finalnumero == '.0':
        numero = numero[:-2]
    return numero


def int_str(numero):
    return str(numero)


def str_int(numero):
    if verifica_numero(numero):
        numero = br_to_us(numero)
        valor = float(numero)
    return valor


def formatar_saida(numero):
    numero = str(numero).strip()
    numero = float_vazio(numero)
    numero = us_to_br(numero)
    return numero


def formatar_entrada(numero):
    if verifica_numero(numero):
        numero = br_to_us(numero)
        numero = float(numero)
    return numero


def receber_valores(ui,n1=0,n2=0):
    if n1 == 0 and n2 == 0:
        n1 = ui.txt1.text()
    if n1 == '': n1 = 0
    if n2 == '': n2 = 0
    if verifica_numero(n1) == True and verifica_numero(n2) == True:
        n1 = br_to_us(n1)
        n2 = br_to_us(n2)
        n1 = float(n1)
        n2 = float(n2)
    return n1,n2


def calculo(n1,n2,operador='+'):
    if operador == '+':
        resultado = soma(n1,n2)
    elif operador == '-':
        resultado = subtrair(n1,n2)
    elif operador == '*':
        resultado = multiplicar(n1,n2)
    elif operador == '/':
        resultado = dividir(n1,n2)
    return resultado