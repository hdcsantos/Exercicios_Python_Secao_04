print("Altura do degrau!")

d = float(input("Informe a altura do degrau (cm): "))
alt = float(input("Informe a altura que deseja alcançar (m): "))


# conversao = alt * 100

obj = (alt * 100) / d

print(f'Para atigir a altura de {alt} metro(s), é preciso subir {round(obj)} degrau(s)!')
