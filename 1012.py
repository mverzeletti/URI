# -*- coding: utf-8 -*-

def main():
    dados = str(input())
    pi =  3.14159
    dados = dados.split(' ')
    a = round(float(dados[0]), 2)
    b = round(float(dados[1]), 2)
    c = round(float(dados[2]), 2)
    triangulo = (a * c) / 2
    circulo = pi * (c ** 2)
    trapezio = ((a + b) * c) / 2
    quadrado = b ** 2
    retangulo = a * b

    print('TRIANGULO: {0:.3f}'.format(triangulo))
    print('CIRCULO: {0:.3f}'.format(circulo))
    print('TRAPEZIO: {0:.3f}'.format(trapezio))
    print('QUADRADO: {0:.3f}'.format(quadrado))
    print('RETANGULO: {0:.3f}'.format(retangulo))


if __name__ == "__main__":
    main()