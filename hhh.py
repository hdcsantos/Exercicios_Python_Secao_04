texto = input("Digite um texto: ")  # Suponha que o usuário digitou a frase do exemplo

nv = 0
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letra in texto:
    if letra in vogais:
        nv += 1

print(f"Frequência relativa = {nv} / {len(texto)}")
