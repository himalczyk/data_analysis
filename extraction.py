from config import filename
from file_filter import File

file = File(filename)

column = file.extract_column_from_df(file.read_file(file.prepare_file_to_read()), 'Short description')
filtered = file.filter_data(column, 'Email')
print(filtered)