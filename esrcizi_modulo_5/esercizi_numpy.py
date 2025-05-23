import numpy as np

jeff_salary = [2700,3000,3000] #lista degli stipendi di jeff
nick_salary = [2600,2800,2800] #lista degli stipendi di nick
tom_salary = [2300,2500,2500] #lista degli stipendi di tom
base_salary = np.array([jeff_salary, nick_salary, tom_salary])
print(base_salary) # ogni riga rappresenta uno dipendente. si crea una matrice di numeri

jeff_bonus = [500,400,400] #lista dei bonus di jeff
nick_bonus = [600,300,400] #lista dei bonus di nick
tom_bonus = [200,500,400] #lista dei bonus di tom
bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])

salary_bonus = base_salary + bonus
print(type(salary_bonus))
print(salary_bonus)

#il valore massimo nell’array salary
print(salary_bonus.max())

"""Specificando axis = 1, si dà istruzione a amax() di cercare orizzontalmente tra le colonne
il massimo nell’array salary_bonus, applicando così la funzione a ogni riga. Questo
calcola l’importo massimo mensile pagato a ciascun dipendente negli ultimi tre mesi"""
print(np.amax(salary_bonus, axis = 1))

print("===================================================================================================")

"""Allo stesso modo, è possibile calcolare l’importo massimo pagato ogni mese a qualsiasi
dipendente modificando il parametro axis in 0"""
print(np.amax(salary_bonus, axis = 0))

"""Provate! Ad esempio, cercate di trovare la media degli importi massimi pagati ogni mese a tutti i dipendenti"""
importi_max_ogni_mese = np.amax(salary_bonus, axis = 0)# importi massimi ogni mese per tutti i dipendenti.
media_max = np.average(importi_max_ogni_mese)
print(media_max)
