# -*- coding: utf-8 -*-

def main():
    funcionario = int(input())
    horas = int(input())
    valor_hora = float(input())
    salario = horas * round(valor_hora, 2)

    print('NUMBER = '+str(funcionario))
    print('SALARY = U$ {0:.2f}'.format(salario))


if __name__ == "__main__":
    main()