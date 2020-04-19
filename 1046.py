i, t = [int(i) for i in input().split(" ")]

if i == t:
    print("O JOGO DUROU 24 HORA(S)")

else:
    if t > i:
        print("O JOGO DUROU {:.0f} HORA(S)".format(t - i))
    
    else:
        print("O JOGO DUROU {:.0f} HORA(S)".format(24 - i + t))