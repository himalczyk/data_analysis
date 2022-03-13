from config import filename
from file_filter import File

file = File(filename)

short_description = file.extract_column_from_df(file.read_file(file.prepare_file_to_read()), 'Short description')
filtered_short_desc_by_keyword = file.filter_data_by_column_and_keyword(short_description, 'Email')
filtered_short_desc = file.filter_data_by_column(short_description)

description = file.extract_column_from_df(file.read_file(file.prepare_file_to_read()), 'Description')
filtered_description_by_keyword = file.filter_data_by_column_and_keyword(description, 'Outlook')
filtered_description = file.filter_data_by_column(description)