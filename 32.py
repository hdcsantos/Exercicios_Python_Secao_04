'''
print('Antecessor e Sucessor')
print('Informe um número inteiro: ')

nu = int(input())

# ant = nu - 1
# suc = nu + 1

soma = ((nu * 3) + 1) + (nu * 2) -1

print(f'O inteiro é {nu} e a soma do sucessor do seu triplo com o dobro do seu antecessor é {soma}')
'''

print('Antecessor e Sucessor')
print('Informe um número inteiro: ')

nu = int(input())
triplo = nu * 3
dobro = nu * 2

for i in range(triplo+1):
    i = i + 1
    r = triplo - i

    if r == -1:
        suc = i

for j in range(dobro):
    j = j + 1
    r2 = dobro - j

    if r2 == 1:
        ant = j

soma = suc + ant
print(f'O inteiro é {nu} e a soma do sucessor do seu triplo ({triplo}) com o dobro ({dobro}) do seu antecessor é igual a {soma}')

