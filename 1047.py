ih, im, th, tm = [int(i) for i in input().split(" ")]

if ih == th:
    if im == tm:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

    elif im > tm:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(24 - ih + th - 1, tm - im + 60))

    else:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(th - ih, tm - im))

elif ih > th:
    if tm >= im:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(24 - ih + th, tm - im))

    else:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(24 - ih + th - 1, tm - im + 60))

else:
    if tm >= im:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(th - ih, tm - im))

    else:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(th - ih - 1, tm - im + 60))