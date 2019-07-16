from datetime import date

print("Idade da pessoa")

idade = int(input("Qual sua idade? "))
ano_corrente = date.today()
ano_nascimento = ano_corrente.year - idade

print(f"Você nasceu no ano de {ano_nascimento}")            

'''
from datetime import date
now = date.today()
print (now.year)
print (now.month)
print (now.day)
#print (now.hour)
#print (now.minute)
#print (now.second)           
'''
