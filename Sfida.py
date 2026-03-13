import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dati_sfida = {
    'Store': ['Milano_A', 'Milano_B', 'Milano_A', 'Milano_C', 'Milano_B', 'Milano_A'],
    'Date': ['2026-02-01', '2026-01-15', '02/02/2026', '2026-02-20', '2026-02-05', '2026-01-20'],
    'Category': [' Tech ', 'Office', 'Tech', ' Furniture ', 'office', 'TECH'],
    'Revenue': ['1.500,00 €', '800,00 €', '1.200,00 €', '2.100,00 €', '450,00 €', '900,00 €']
}

df = pd.DataFrame(dati_sfida)
df['Category']=df['Category'].str.strip() \
                             .str.capitalize()

df['Revenue']=df['Revenue'].str.replace('.','',regex=False) \
                           .str.replace(',', '.',regex=False) \
                           .str.replace('€', '').astype(float)

df['Date']=pd.to_datetime(df['Date'], dayfirst=True,format='mixed')


risultato = df[(df['Date'].dt.month==2)] \
            .groupby('Category')['Revenue'] \
            .sum() \
            .idxmax()

print(risultato)
print(df)

# Quale categoria ha incassato di più a febbraio?


# 1. Prepariamo i dati per il grafico (ci fermiamo al sum e resettiamo l'index)

df_grafico = df[df['Date'].dt.month == 2].groupby('Category')['Revenue'].sum().reset_index()

# 2. Usiamo .idxmax() per identificare il vincitore da stampare o mettere nel titolo
vincitore_idx = df_grafico['Revenue'].idxmax()
nome_vincitore = df_grafico.loc[vincitore_idx, 'Category']

# 3. Creazione del grafico
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

ax = sns.barplot(x='Category', y='Revenue', data=df_grafico, palette='viridis')

# Aggiungiamo il titolo dinamico usando "vincitore"
plt.title(f'Incassi Febbraio - Top Category: {nome_vincitore}', fontsize=14)
plt.ylabel('Totale Revenue (€)')
plt.xlabel('Categoria')

# Mostriamo il grafico
plt.show()
