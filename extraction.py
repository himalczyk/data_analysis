from config import filename
from file_filter import File

file = File(filename)

column = file.extract_column_from_df(file.read_file(file.prepare_file_to_read()), 'Short description')
filtered_column_by_keyword = file.filter_data_by_column_and_keyword(column, 'Email')
filtered_column = file.filter_data_by_column(column)