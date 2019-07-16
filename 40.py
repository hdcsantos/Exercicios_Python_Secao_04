print("Salário líquido")
print("A empresa paga R$ 30,00 por dia de trabalho e desconta 8% de IR. "
      "\nInforme a qtd de dias que o encanadou trabalhou: ")

dias = int(input())

liquido = dias * 30
desconto = liquido - float(liquido) * 0.08

print(f"O valor liquido, já com desconto, na quatidade de dias informado é de R$ {desconto}")

