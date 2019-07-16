print("Converter segundos em H,M,S")

seg = int(input("Informe um valor em segundos: "))
min = seg / 60
h = seg / 3600

print(type(h))
print(f"{seg} segundos, equivalem a {h} hora(s) e {int(min)} minuto(s)")
