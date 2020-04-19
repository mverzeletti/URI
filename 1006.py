# -*- coding: utf-8 -*-

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    peso_a = 2
    peso_b = 3
    peso_c = 5
    peso_total = peso_a + peso_b + peso_c

    X = (round(a, 1) * (peso_a / peso_total)) + (round(b, 1) * (peso_b / peso_total)) + (round(c, 1) * (peso_c / peso_total))

    print('MEDIA = {0:.1f}'.format(X))

if __name__ == "__main__":
    main()