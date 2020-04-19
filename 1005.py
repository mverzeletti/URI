# -*- coding: utf-8 -*-

def main():
    a = float(input())
    b = float(input())
    peso_a = 3.5
    peso_b = 7.5
    peso_total = peso_a + peso_b

    X = (round(a, 1) * (peso_a / peso_total)) + (round(b, 1) * (peso_b / peso_total))

    print('MEDIA = {0:.5f}'.format(X))

if __name__ == "__main__":
    main()