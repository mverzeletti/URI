# -*- coding: utf-8 -*-

def modulo (a, b):

    return int(a % b)

def divisao (a, b):

    return int(a / b)

def main():
    valor = int(input())
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    print(valor)
    for i in cedulas:
        n = divisao(valor, i)
        valor = modulo(valor, i)
        print(str(n)+' nota(s) de R$ '+str(i)+',00')

if __name__ == "__main__":
    main()