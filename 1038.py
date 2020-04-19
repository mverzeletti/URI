def valor_lanche(codigo, valores):
    return valores[codigo]

dados = input()
dados = dados.split(' ')
codigo = int(dados[0])
quantidade = int(dados[1])
valores = {
            1: 4,
            2: 4.5,
            3: 5,
            4: 2,
            5: 1.5
        }
lanche = valor_lanche(codigo, valores)
total = quantidade * lanche
print('Total: R$ {0:.2f}'.format(total))