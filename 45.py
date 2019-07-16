print("Convertendo de Maiusculo para minúsculo usando a tabela ASCCII")

letra = input("Informe uma letra qualquer maiúscula: ")

# A função ord() devolve o código numérico do caractere passado como parâmetro
f = ord(letra)

letra = f + 32

# A função chr() devolve o caracter corresponde ao código numérico passado como parâmetro
lll = chr(letra)

print(f"A letra foi convertida: {lll}")
