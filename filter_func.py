import pandas as pd

def filter_data(column, keyword_to_search: str):
    
    text=[]
    
    for row in column:
        text.append(row.split())
        
    for sentence in text:
        if keyword_to_search in sentence:
            print(sentence)
        else:
            print(False)
            
    return text