from config import filename
from filter_func import File

# file = f'report_files/{filename}.xlsx'

# df = pd.read_excel(file)
# # print(df)

# cols = df[['Short description', 'Description', 'Template']]

# filter_short_desc = df['Short description']
# filter_desc = df['Description']

file = File(filename)

column = file.extract_column_from_df(file.read_file(file.prepare_file_to_read()), 'Short description')
filtered = file.filter_data(column, 'Email')
print(filtered)