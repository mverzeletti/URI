def inteiro(a, b):

    return int(a / b)

def resto(a, b):

    return round(a % b, 2)

def notas (valor, notas):
    print('NOTAS:')
    for i in notas:
        n = inteiro(valor, i)
        valor = resto(valor, i)
        print(str(n)+' nota(s) de R$ {0:.2f}'.format(i))
    return valor

def moedas(valor, moedas):
    print('MOEDAS:')
    for i in moedas:
        n = inteiro(valor, i)
        valor = resto(valor, i)
        print(str(n)+' moeda(s) de R$ {0:.2f}'.format(i))
    
    return valor

valor = round(float(input()), 2)
valor = notas(valor, [100, 50, 20, 10, 5, 2])
valor = moedas(valor, [1, .5, .25, .10, .05, .01])