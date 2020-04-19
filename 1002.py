# -*- coding: utf-8 -*-

def main():
    n = float(input())
    pi = 3.14159
    A = round(pi * (round(n, 2) ** 2), 4)

    print('A={0:.4f}'.format(A))

if __name__ == "__main__":
    main()