import pandas as pd

def separatore():
    print("=============================================================================================================================")
    print("=============================================================================================================================")


"""Esercizio 4: Aggregazione e riepilogo di dati di recensioni di film con groupby()
Immagina di avere un DataFrame recensioni_film con le colonne 'ID Film', 'Titolo Film', 'Punteggio' (su una scala da 1 a 5).
Utilizza la funzione groupby() di pandas per:
• Calcolare il punteggio medio per ciascun film.
• Contare il numero totale di recensioni per ciascun film (size() o count() su una colonna).
• Identificare il punteggio massimo e minimo ricevuto da ciascun film."""


dati ={
    'ID_Film ':['fi456','fi980','fi005','fi503','fi994','fi456','fi456','fi005','fi503','fi503','fi994'],
    'Titolo_Film':['dune 2','bomboclast','planet of apes','warfare','the batman','dune 2','dune 2','planet of apes','warfare','warfare','the batman'],
    'Punteggio':[1,4,4,5,2,5,5,2.5,1,0,4]
}

df = pd.DataFrame(dati)
print(df)
separatore()

#Calcolare il punteggio medio per ciascun film.
df_punteggio_medio_film = df.groupby('Titolo_Film')['Punteggio'].mean()
print(df_punteggio_medio_film)
separatore()

#Contare il numero totale di recensioni per ciascun film (size() o count() su una colonna).
df_count_recensioni_film = df.groupby('Titolo_Film')['Punteggio'].count()
print(df_count_recensioni_film)
separatore()

#Identificare il punteggio massimo e minimo ricevuto da ciascun film.
df_max_and_min =df.groupby('Titolo_Film')['Punteggio'].agg(['max','min'])
print(df_max_and_min)