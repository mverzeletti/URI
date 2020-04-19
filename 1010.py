# -*- coding: utf-8 -*-

def main():
    peca1 = str(input())
    peca2 = str(input())
    peca1 = peca1.split(' ')
    peca2 = peca2.split(' ')
    total = (int(peca1[1]) * float(peca1[2])) + (int(peca2[1]) * float(peca2[2]))

    print('VALOR A PAGAR: R$ {0:.2f}'.format(total))


if __name__ == "__main__":
    main()