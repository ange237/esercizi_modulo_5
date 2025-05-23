import pandas as pd


def separatore():
    print("=============================================================================================================================")
    print("=============================================================================================================================")

"""Esercizio 3: Unione di dati clienti e ordini con diverse politiche di join
Crea un DataFrame clienti con le colonne 'ID Cliente', 'Nome', 'Città' per alcuni clienti. Assicurati che l'ID Cliente sia l'indice.
Crea un secondo DataFrame ordini con le colonne 'ID Ordine', 'ID Cliente', 'Importo'. Assicurati che alcuni 'ID Cliente' nel DataFrame 
ordini corrispondano a quelli nel DataFrame clienti, ma includi anche:
• Un 'ID Cliente' nel DataFrame clienti che NON abbia ordini nel DataFrame ordini.
• Un 'ID Cliente' nel DataFrame ordini che NON esista nel DataFrame clienti (simulando un errore o un cliente non registrato).
Utilizza i metodi di unione di pandas (join o merge) per combinare i due DataFrame in modo da ottenere:
• Un DataFrame che includa solo gli ordini per i quali esiste un cliente corrispondente nel DataFrame 
clienti (equivalente a una inner join basata sull'ID Cliente).
• Un DataFrame che includa tutti i clienti dal DataFrame clienti e i loro ordini corrispondenti, 
mostrando valori mancanti (NaN) per i clienti senza ordini (equivalente a una left join).
• Un DataFrame che includa tutti gli ordini e i dati del cliente corrispondente, mostrando valori mancanti per gli ordini 
senza un cliente registrato (equivalente a una right join)."""

id_cliente = ['cl345','cl456','cl509','cl098','cl879']
nome = ['ange bonheur','lorenzo pourpour','gabrielle grecco','mateo pirotta','keane reves']
citta = ['TORINO','MILANO','NAPOLI','GENOVA','TRIESTE']

ID_cliente= pd.Series(id_cliente,index = id_cliente,name ='ID Cliente')
nome_cliente = pd.Series(nome,index = id_cliente,name ='Nome' )
citta_cliente = pd.Series(citta,index = id_cliente,name ='Città' )
df_clienti = pd.concat([ID_cliente,nome_cliente,citta_cliente], axis = 1)
print(df_clienti)
separatore()
id_ordini = ['or456','or690','or510','or409','od900']
id_cliente = ['cl345','cl456','cl509','cl003','cl879']
importo = [900,300,500,400,400]

ID_Ordine = pd.Series(id_ordini,index = id_ordini , name ='ID Ordine')
ID_Cliente = pd.Series(id_cliente,index = id_ordini, name ='ID Cliente')
Importo = pd.Series(importo,index = id_ordini, name ='Importo')
df_ordini = pd.concat([ID_Cliente,ID_Ordine,Importo],axis = 1)
print(df_ordini)
separatore()

#DataFrame che includa solo gli ordini per i quali esiste un cliente corrispondente nel DataFrame 
#clienti (equivalente a una inner join basata sull'ID Cliente)
df_merge_inner = pd.merge(df_ordini, df_clienti, on='ID Cliente', how='inner')#Usi **merge** quando vuoi unire due DataFrame 
#su una colonna in comune (come una chiave in un database), anche se gli indici sono diversi
print(df_merge_inner)
separatore()

#Un DataFrame che includa tutti i clienti dal DataFrame clienti e i loro ordini corrispondenti, 
#mostrando valori mancanti (NaN) per i clienti senza ordini (equivalente a una left join)
df_merge_left = pd.merge(df_ordini, df_clienti, on='ID Cliente', how='left')
print(df_merge_left)
separatore()

#Un DataFrame che includa tutti gli ordini e i dati del cliente corrispondente, mostrando valori mancanti per gli ordini 
#senza un cliente registrato (equivalente a una right join)
df_merge_right = pd.merge(df_ordini, df_clienti, on='ID Cliente', how='right')
print(df_merge_right)
separatore()