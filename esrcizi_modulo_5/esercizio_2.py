import pandas as pd

def separatore():
    print("=============================================================================================================================")
    print("=============================================================================================================================")

"""Crea tre Series pandas distinte: una per i nomi dei prodotti (nomi_prodotti), una per i codici prodotto (codici_prodotti), 
e una per le quantità disponibili in magazzino (quantita_disponibili).
Utilizza i codici prodotto come indici per le Series (index=[codice1, codice2, ...]).
Combina queste tre Series in un unico DataFrame chiamato inventario_prodotti, assicurandoti che i nomi delle colonne siano chiari 
(es. 'Nome Prodotto', 'Quantità').
Accedi e stampa la quantità disponibile per un prodotto specifico utilizzando il suo codice prodotto (indice) 
e anche utilizzando la sua posizione."""

nomi = ['latte','birra','pane','mozzarella','carotte']
codici = ['la165','bi234','pa123','mo567','ca675']
qta = [20,30,46,78,90]

nomi_prodotti = pd.Series(nomi,index = codici,name ='Nome Prodotto')
codici_prodotti = pd.Series(codici,name = 'Codice')
qta_prodotti = pd.Series(qta,index = codici,name = 'Quantità')

print(nomi_prodotti)
separatore()
print(codici_prodotti)
separatore()
print(qta_prodotti)
separatore()

df = pd.concat([nomi_prodotti,qta_prodotti], axis = 1)#lungo le righe
print(df)
separatore()

print(df.loc['mo567'])#loc : usando l'indice definito
separatore()
print(df.iloc[3])# iloc usando la posizione.


