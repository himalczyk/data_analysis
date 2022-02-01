import pandas as pd


class File():
    
    def __init__(self, filename):
        self.filename = filename
        
    def prepare_file_to_read(self):
        
        """[Creates the path to the given filename in constructor]

        Returns:
            [String]: [Path to file to read from dataframe]
        """
        
        file = f'report_files/{self.filename}.xlsx'
        
        return file
        
    def read_file(self, file):
        
        """[Read the file using pandas. Creates a dataframe]

        Returns:
            [<class 'pandas.core.series.Series'> dataframe]: [Dataframe object from Pandas]
        """
        
        df = pd.read_excel(file)
        
        return df
    
    def extract_column_from_df(self, df, column_name):
        
        """[Extracts a column from a given created dataframe]

        Returns:
            [<class 'pandas.core.series.Series'>]: [Column extracted from dataframe]
        """
        
        column = df[column_name]
        
        return column
    
    def filter_data_by_column(self, column):
        
        """[Extract every rows value basing on column given]

        Returns:
            [List]: [List with sentences]
        """
        
        text=[]
        
        for row in column:
            text.append(row)
            
        return text

    def filter_data_by_column_and_keyword(self, column, keyword_to_search: str):
        
        """[Filters data by given column and keyword to extract sentence]

        Returns:
            [List]: [List of found sentences with given keyword]
        """
        
        text=[]
        
        for row in column:
            text.append(row)
            
        extracted_keywords = []
            
        for sentence in text:
            if keyword_to_search in sentence:
                extracted_keywords.append(sentence)
                
        return extracted_keywords

