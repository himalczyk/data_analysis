import pandas as pd
from config import filename

file = f'report_files/{filename}.xlsx'

df = pd.read_excel(file)
# print(df)

cols = df[['Short description', 'Description', 'Template']]

print(df['Short description'])

filter_short_desc = df['Short description']
filter_desc = df['Description']

# comprehend = [row for row in filter_short_desc if row]

text = []

for row in filter_short_desc:
    text.append(row.split())
    
for sentence in text:
    if 'Email' in sentence:
        print(sentence)
    else:
        print(False)
        