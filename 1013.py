# -*- coding: utf-8 -*-

def maior (a, b):

    x = (a + b + abs(a - b)) / 2

    return int(x)

def main():
    dados = str(input())
    dados = dados.split(' ')
    a = int(dados[0])
    b = int(dados[1])
    c = int(dados[2])
    maior1 = maior(a, b)
    maior2 = maior(maior1, c)

    print(str(maior2)+' eh o maior')


if __name__ == "__main__":
    main()