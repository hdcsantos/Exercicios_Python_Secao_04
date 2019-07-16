'''
print('Antecessor e Sucessor')
print('Informe um número inteiro: ')

nu = int(input())

ant = nu - 1
suc = nu + 1

print(f'O antecessor e o sucessor de {nu} são respectivamente {ant} e {suc}')

'''

print('Antecessor e Sucessor')
print('Informe um número inteiro: ')

nu = int(input())

for i in range(nu+1):
    i = i + 1
    r = nu - i

    if r == 1:
        ant = i
    elif r == -1:
        suc = i

print(f'O antecessor e o sucessor de {nu} são respectivamente {ant} e {suc}')

