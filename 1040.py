notas = [float(i) for i in input().split(' ') ]
pesos = 2, 3, 4 ,1
total = sum([notas[i] * pesos[i] for i in range(len(notas))])
media = total / sum(pesos)

print('Media: {:.1f}'.format(media))

if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    nova_media = (exame + media) / 2
    if nova_media >= 5:
        print('Aluno aprovado.')
    
    else:
        print('Aluno reprovado.')
    
    print('Media final: {:.1f}'.format(nova_media))
