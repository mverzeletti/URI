lados = [float(i) for i in input().split(" ")]
ordem = sorted(lados, reverse=True)
quadrados = [i ** 2 for i in ordem]

if ordem[2] + ordem[1] > ordem[0]:
   
    if quadrados[0] == quadrados[1] + quadrados[2]:
        print("TRIANGULO RETANGULO")

    elif quadrados[0] > quadrados[1] + quadrados[2]:
        print("TRIANGULO OBTUSANGULO")
    
    else:
        print("TRIANGULO ACUTANGULO")

    if ordem[0] == ordem[1] and ordem[1] == ordem[2]:
        print("TRIANGULO EQUILATERO")
    
    elif ordem[0] == ordem[1] or ordem[1] == ordem[2]:
        print("TRIANGULO ISOSCELES")
    
    else:
        pass

else:
    print("NAO FORMA TRIANGULO")