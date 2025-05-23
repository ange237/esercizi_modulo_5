import pandas as pd
from textblob import TextBlob
import re
"""Esercizio 5: Concetti di pipeline per l'analisi di feedback testuali
Considera di dover analizzare un set di feedback testuali 
inviati dai partecipanti a un evento (ad esempio, un file di testo semplice o un elenco di commenti).
Identifica e descrivi brevemente quali passaggi della pipeline di elaborazione dati (Acquisizione, Pulizia, 
Trasformazione, Analisi, Immagazzinamento) sarebbero necessari per:
• Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi all'inizio/fine dei commenti.
• Convertire tutti i commenti in minuscolo per garantire uniformità.
• Estrarre le parole chiave principali da ciascun commento.
• Determinare se il sentiment generale (positivo, negativo, neutro) di ciascun commento.
• Calcolare il sentiment medio complessivo per tutti i feedback.
• Salvare i risultati dell'analisi (sentiment per commento, sentiment medio) in un formato strutturato.
Per ogni passaggio, menziona brevemente quali librerie o tecniche Python viste (anche concettualmente, come l'elaborazione 
del linguaggio naturale - NLP42... o l'analisi del sentiment44...) potrebbero essere utili."""


"""1)pulizia:per pulire i nostri dati come Rimuovere caratteri speciali, punteggiatura extra o spazi bianchi 
all'inizio/fine dei commenti si potrebbe usare usare le espressioni regolari,sostituendo ognuno di questi caratteri indesiderati con 
caratteri speciali , importando la libreria re e si usa anche la funzione str.strip() per togliere i carratteri bianchi all'inizio e fine 
"""

"""2)trasformazione:per convertire tutti i commenti in minuscolo per avere un set uniforme,si potrebbe usare la funzione str.lower()
su ogni riga """

"""3)Estrarre le parole chiave principali da ciascun commento si puo usare la tokenizzazione e le stopwords con textblob"""

"""4)per determinare se il sentiment generale (positivo, negativo, neutro) di ciascun commento si usa l'analisi del sentiment tramitela libreria
textblob che ritorna per ogni commento la sua polarità"""

"""5)per Calcolare il sentiment medio complessivo per tutti i feedback si usa la libreria textbob per calcolare il sentiment
di ogni commento e poi si fa la media matematica dei sentiment"""

"""6)per salvare i risultati dell'analisi (sentiment per commento, sentiment medio) in un formato strutturato si può usare un file csv oppure un 
file di testo classico"""

#funzione per pulire il commento
def pulisci_testo(testo):
    testo = testo.strip() # rimuove spazi all'inizio e alla fine
    testo = re.sub(r'[^\w\s]', '', testo) # rimuove punteggiatura
    return testo

#funzione per trasformare in minuscolo:
def normalizza_testo(testo):
    return testo.lower()

#funzione per estrarre le parole chiavi di un commento
def estrai_keywords(testo):
    blob = TextBlob(testo)
    return blob.noun_phrases

#funzione per analizzare il sentiment di un commento:
def calcola_sentiment(testo):
    blob = TextBlob(testo)
    return float(blob.sentiment.polarity)

#commenti in iglese perche textblob non supporta bene l'italiano
commenti = [
    "it was very good!",
    "really boring.",
    "very good, i liked it.",
    "i found nothing interessting.",
    "very good organasation!"
]

commenti_puliti = []
commenti_normalizzati = []
keywords_estratte = []
valori_sentiment = []

for commento in commenti:
    pulito = pulisci_testo(commento)
    normalizzato = normalizza_testo(pulito)
    keywords = estrai_keywords(normalizzato)
    sentiment = calcola_sentiment(normalizzato)
    
    commenti_puliti.append(pulito)
    commenti_normalizzati.append(normalizzato)
    keywords_estratte.append(", ".join(keywords))
    valori_sentiment.append(sentiment)


#si calcola il sentiment medio usando solo la lista valori_sentiment:
sentiment_medio = sum(valori_sentiment) / len(valori_sentiment)

#si crea il dataframe 
df = pd.DataFrame({
    "Commento originale": commenti,
    "Commento pulito": commenti_puliti,
    "Minuscolo": commenti_normalizzati,
    "Parole chiave": keywords_estratte,
    "Sentiment": valori_sentiment,
    "Media": ["", "", "", "", sentiment_medio]
})


#si salva su un file csv:
df.to_csv("analisi_feedback.csv", index=False)