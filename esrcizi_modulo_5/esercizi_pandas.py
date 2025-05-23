import pandas as pd
import yfinance as yf
import json

"""Ecco come creare una Series da una lista Python Si ottiene così una singola lista con gli indici numerici 
impostati per default, a partire da 0"""
data = ['Jeff Russell','Jane Boorman','Tom Heints']
emps_names = pd.Series(data)
print(emps_names)

#È possibile creare una Series con indici definiti dall’utente come segue
data = ['Jeff Russell','Jane Boorman','Tom Heints']
emps_names = pd.Series(data,index=[9001,9002,9003])
print(emps_names)

#Per accedere a un elemento di una Series si specifica il nome della Series seguito dall’indice
#dell’elemento tra parentesi quadre, come mostrato qui
print(emps_names[9001])


#In alternativa, è possibile utilizzare la proprietà loc dell’oggetto Series:
print(emps_names.loc[9001])

"""Sebbene si utilizzino indici personalizzati in questo oggetto Series, è comunque possibile
accedere ai suoi elementi in base alla posizione (ovvero, utilizzare l’indicizzazione
basata su posizioni intere) tramite la proprietà iloc. Qui, ad esempio, si stampa il primo
elemento della Series"""
print(emps_names.iloc[0])

#È possibile accedere a più elementi in base ai loro indici con un’operazione di slicing,
print(emps_names.loc[9001:9002])

"""Si noti che lo slicing con loc include l’endpoint destro (in questo caso, l’indice 9002),
mentre di solito la sintassi dello slicing di Python non lo fa"""

"""È possibile combinare più Series per formare un DataFrame. Proviamo a creare un’altra
Series e a combinarla con la Series emps_names"""


"""Per creare la nuova Series, si chiama il costruttore Series() , passando i seguenti
argomenti: la lista da convertire in serie, gli indici della Series e il nome della Series.
È necessario assegnare un nome alle Series prima di concatenarle in un DataFrame, perché
i loro nomi diventeranno i nomi delle colonne corrispondenti del DataFrame.Poiché
la Series emps_names non è stata nominata al momento della creazione, la si nomina qui
impostando la proprietà name su 'names'.Successivamente, è possibile concatenarla
con i campi emps_emails della Series . Si specifica axis=1 per concatenare lungo le colonne"""
data = ['jeff.russell','jane.boorman','tom.heints']
emps_emails = pd.Series(data,index=[9001,9002,9003], name = 'emails')
emps_names.name = 'names'
df = pd.concat([emps_names,emps_emails], axis=1)
print(df)

print("==============================================================================================")

"""provate a creare un DataFrame da tre Series. Per farlo, è necessario creare un’altra Series (ad esempio, emps_phones)"""
data = ['323-465','323-679','323-980']
emps_num = pd.Series(data,index=[9001,9002,9003],name = 'phone')
df = pd.concat([emps_names,emps_emails,emps_num], axis = 1)
print(df)

"""Si è visto come creare un DataFrame pandas combinando più oggetti Series. È possibile
creare un DataFrame anche caricando i dati da un database, da un file CSV, da una richiesta
API o da un’altra fonte esterna, utilizzando uno dei metodi reader della libreria
pandas. I reader consentono di leggere diversi tipi di dati, come JSON ed Excel, in un
DataFrame."""


#Quindi richiedete i dati delle azioni, come mostrato qui:
"""In questo script, si invia una richiesta all’API per ottenere i dati sulle quotazioni di un
determinato ticker e si utilizza il metodo history() di yfinance per specificare che si
desidera ottenere i dati per un periodo di cinque giorni . I dati risultanti, memorizzati
nella variabile hist, sono già sotto forma di DataFrame pandas. Non è necessario creare
esplicitamente il DataFrame; yfinance lo fa per voi dietro le quinte. Dopo aver ottenuto.il DataFrame, si rimuovono alcune colonne e si passa all’indicizzazione numerica ,
ottenendo la struttura mostrata nelle Figure mostrate in precedenza."""
tkr = yf.Ticker('TSLA')
hist = tkr.history(period="5d")
hist = hist.drop("Dividends", axis = 1)
hist = hist.drop("Stock Splits", axis = 1)
hist = hist.reset_index()

#Per impostare l’indice sulla colonna Date, come mostrato nella seconda figura, è necessario
#eseguire la seguente riga di codice
hist = hist.set_index('Date')

"""Proviamo ora a convertire un documento JSON in un oggetto pandas. Il dataset campione
utilizzato contiene i dati salariali mensili di tre dipendenti identificati dai loro ID
nella colonna Empno"""


"""Si utilizza il metodo reader di pandas read_json() per passare una stringa JSON in un
DataFrame . Per semplicità, questo esempio utilizza una stringa JSON ottenuta da una
lista di json.dumps().In alternativa, è possibile passare al reader un oggetto path che
punta a un file JSON di interesse o a un URL di un’API HTTP che pubblica dati in formato JSON.Infine, si imposta la colonna Empno 
come indice del DataFrame , sostituendo
così l’indice numerico predefinito"""
data = [
{"Empno":9001,"Salary":3000},
{"Empno":9002,"Salary":2800},
{"Empno":9003,"Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
print(salary)


"""Un’altra pratica comune è quella di creare DataFrame pandas dalle strutture di dati
standard di Python introdotte nel capitolo precedente. Ad esempio, ecco come creare un
DataFrame da una lista di liste"""

"""Innanzitutto, si inizializza una lista di liste con i dati da inviare al DataFrame . Ogni
lista annidata diventerà una riga del DataFrame. Quindi si crea esplicitamente il Data-
Frame, definendo le colonne da utilizzare . Successivamente, si utilizza un dizionario,
column_types, per modificare i tipi di dati impostati per le colonne per impostazione
predefinita . Questo passo è facoltativo, ma può essere fondamentale se si intende unire
il DataFrame a un altro. Questo perché è possibile unire due DataFrame solo su colonne.dello stesso tipo di dati. 
Infine, si imposta la colonna Empno come indice del DataFrame.
Il DataFrame risultante avrà il seguente aspetto"""
data = [['9001','Jeff Russell', 'sales'],
['9002','Jane Boorman', 'sales'],
['9003','Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')
print(emps)