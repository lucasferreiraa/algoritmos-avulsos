lista = [3,1,5,4,2]

for i in range(len(lista)):
	menor = i
	for j in range(i+1, len(lista)):
		if (lista[j] < lista[menor]):
			lista[j], lista[menor] = lista[menor], lista[j]
