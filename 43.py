'''
def trunc(num, digits):
    sp = str(num).split('.')
    return '.'.join([sp[0], sp[:digits]])
'''

print("Ajuda a vendedores")

vt = float(input("Informe o valor total R$: "))
v_desconto = vt - (vt * 0.10)
v_parcelas = vt / 3
c_1 = v_desconto * 0.05
c_2 = vt * 0.05

print(f"O valor total a pagar com desconto de 10% é de R$ {round(v_desconto, 2)}; "
      f"\nO valor parcelado fica em R$ {round(v_parcelas, 2)} x 3;"
      f"\nA sua comissão (5%) em venda a vista, em cima do valor total com desconto de 10% é de R$ {round(c_1, 2)}; "
      f"\nA sua comissão (5%) em venda parcelada, em cima do valor total de parcelas é de R$ {round(c_2, 2)}")
