"""
Desempacotamento de listas
"""

lista = ['Luiz', 'Deriki', 'Maria',1,2,3,4,5,6,7,8,9,100]

n1 , n2 ,n3, *resto_lista_ate_9 , ultimo_valor = lista

print(n1)

print(n2)

print(n3)

print(resto_lista_ate_9)

print(ultimo_valor)
