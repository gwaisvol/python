"""El enunciado brinda la siguiente tupla de ejemplo"""
tupla = (8, 15, 4, 39, 5, 89, 87,  19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
"""1.Se solicita imprimir el último elemento de la tupla"""
ultimo_elemento=len(tupla)-1
print(tupla[ultimo_elemento])
"""2.El número de ítems de tupla"""
lenght=len(tupla)
print(lenght)
"""3. La posición donde se encuentra el ítem 87 de tupla"""
index=tupla.index(87)
print(index)
"""4. Una lista con los últimos tres ítems de tupla"""
lista=[tupla[ultimo_elemento-2],tupla[ultimo_elemento-1],tupla[ultimo_elemento]]
print(lista[0],lista[1],lista[2])
"""5. Un ítem que haya en la posición 8 de tupla"""
print(tupla[8])
"""6. El número de veces que el ítem 7 aparece en tupla"""
item_7=tupla[7]
repeticiones_item_7=tupla.count(item_7);
print(repeticiones_item_7)