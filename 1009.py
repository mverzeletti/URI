# -*- coding: utf-8 -*-

def main():
    vendedor = str(input())
    salario = float(input())
    venda = float(input())
    comissao = 0.15
    total = round(salario, 2) + (comissao * round(venda, 2))

    print('TOTAL = R$ {0:.2f}'.format(total))


if __name__ == "__main__":
    main()