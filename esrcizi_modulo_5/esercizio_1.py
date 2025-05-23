import numpy as np

def separatore():
    print("=============================================================================================================================")
    print("=============================================================================================================================")
"""Immagina di avere i dati di vendita trimestrali per tre diverse regioni (Nord, Centro, Sud) su un periodo di quattro trimestri.
 Crea un array NumPy 2D che rappresenti queste vendite. 
 Ad esempio: vendite_regionali = np.array([[v_n_t1, v_n_t2, v_n_t3, v_n_t4], [v_c_t1, ..., v_c_t4], [v_s_t1, ..., v_s_t4]]).
Utilizza le funzioni statistiche di NumPy per:
• Calcolare le vendite totali per ogni regione nell'anno (np.sum() sull'asse appropriato).
• Trovare il trimestre con le vendite massime per ogni regione (np.amax() sull'asse appropriato).
• Calcolare le vendite medie per trimestre a livello complessivo (media sull'intero array).
• Identificare le vendite minime registrate in qualsiasi trimestre e qualsiasi regione (np.amin() sull'intero array, 
concettualmente simile a np.max/np.amax)."""

nord = [200,450,300,320]
centro = [160,180,500,160]
sud = [400,600,650,600]
vendite_regionali = np.array([nord,centro,sud])
print(vendite_regionali)
separatore()

#vendite totali per ogni regione nell'anno (np.sum() sull'asse appropriato)
vendite_totali_per_regioni = np.sum(vendite_regionali, axis = 1) # lungo le righe
print(vendite_totali_per_regioni)
separatore()

#Trovare il trimestre con le vendite massime per ogni regione (np.amax() sull'asse appropriato).
trimestre_vendite_max = np.amax(vendite_regionali,axis = 1) # lungo le righe
print(trimestre_vendite_max)
separatore()

# Calcolare le vendite medie per trimestre a livello complessivo (media sull'intero array)
vendite_medie_complessivo = np.average(vendite_regionali)
print(vendite_medie_complessivo)
separatore()

#Identificare le vendite minime registrate in qualsiasi trimestre e qualsiasi regione (np.amin() sull'intero array, 
#concettualmente simile a np.max/np.amax)
vendite_mininne_complessivo = np.min(vendite_regionali)
print(vendite_mininne_complessivo)