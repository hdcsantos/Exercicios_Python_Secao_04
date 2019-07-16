print('Precificação para cercar terreno')

p = float(input('Preço do metro de tela: '))
c = float(input('Comprimento do terreno em m: '))
lg = float(input('Largura do terreno em m: '))

# m2 = c * lg
# pt = p * m2

mt = c * 2 + lg * 2
pt = p * mt

print(f'Custo para cercar o terreno com tela vai ser de {pt} reais')