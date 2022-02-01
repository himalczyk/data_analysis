import nltk
nltk.download('punkt')
from extraction import filtered_column_by_keyword, filtered_column

class Tagging():
    
    def __init__(self, data_to_tag):
        self.data_to_tag = data_to_tag
        
    def tag_data(self):
        
        pos_tagged_tokens = []
        
        for sentence in self.data_to_tag:
            tokens = nltk.word_tokenize(sentence)
            pos_tagged_tokens.append(nltk.pos_tag(tokens))
            
        return pos_tagged_tokens
    
tag = Tagging(filtered_column_by_keyword)

tag_column = tag.tag_data()
print(tag_column)