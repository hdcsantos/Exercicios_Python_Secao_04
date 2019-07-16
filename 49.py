print("Experiência biológica")

h = int(input("Informe a hora do inicio da experiência: "))
minu = int(input("Informe o minuto do inicio da experiência: "))
seg = int(input("Informe o segundo do inicio da experiência: "))
seg_termino = int(input("Informe quantos segundos irá durar o experimento: "))

hora_p_segundo = h * 3600
if (30 - minu) > 0:
    # Pegando a parte inteira do resultado do cálculo
    nova_hora = (hora_p_segundo + seg_termino) // 3600
else:
    # Pegando a parte inteira do resultado do cálculo de soma de mais uma hora
    nova_hora = (hora_p_segundo + seg_termino + 3600) // 3600
    
min_p_segundo = minu * 60
# Pegando a parte inteira do resultado do cálculo e depois o resto
novo_min = ((min_p_segundo + seg_termino) // 60) % 60

print(f"De acordo com o tempo de duração do experimento em segundos, "
      f"\nhorário de término do experimento será em: {nova_hora}:{novo_min}:{seg} Horas")

'''

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")
'''
