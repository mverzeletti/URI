def delta(a, b, c):

    return (b ** 2) - (4 * a * c)

def bhaskara(a, b, d):

    return (-b + d) / (2 * a)

dados = input()
dados = dados.split(' ')
a = round(float(dados[0]), 2)
b = round(float(dados[1]), 2)
c = round(float(dados[2]), 2)
d = delta(a, b, c)
raiz_d = d ** .5

if a == 0 or d < 0:
    print('Impossivel calcular')
else:
    r1 = bhaskara(a, b, raiz_d)
    r2 = bhaskara(a, b, -raiz_d)
    print('R1 = {0:.5f}'.format(r1))
    print('R2 = {0:.5f}'.format(r2))
