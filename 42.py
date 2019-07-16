print("Salário base")

sb = float(input("Informe o valor do salário base R$: "))

sb = sb + (sb * 0.05)

sr = sb - (sb * 0.07)

print(f"O valor do salario a receber \njá com o adicional de 5% e desconto de 7% é de R$ {sr}")
