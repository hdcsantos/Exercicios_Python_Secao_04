print("Salário líquido")

ht = float(input("Informe o valor da hora trabalhada R$: "))
h = float(input("Informe o numero de horas trabalhadas no mês H: "))

bruto = h * ht

liquido = bruto + (bruto * 0.10)

print(f"O valor de hora/trabalho X horas, com a dicional de 10% é de R$ {liquido}")
