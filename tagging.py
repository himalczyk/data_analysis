import nltk
nltk.download('punkt')
from extraction import filtered_columnb_by_keyword, filtered_column

class Tagging():
    
    def __init__(self, data_to_tag):
        self.data_to_tag = data_to_tag
        
    def tag_data(self):
        
        pos_tagged_tokens = []
        
        for sentence in self.data_to_tag:
            tokens = nltk.word_tokenize(sentence)
            pos_tagged_tokens.append(nltk.pos_tag(tokens))
            
        return pos_tagged_tokens
    
tag = Tagging(filtered_column)

tag_column = tag.tag_data()
print(tag_column)
            

# pos_tagged_tokens_by_keyword = []

# for sentence in filtered_columnb_by_keyword:
#     tokens = nltk.word_tokenize(sentence)
#     pos_tagged_tokens_by_keyword.append(nltk.pos_tag(tokens))
    
# print(pos_tagged_tokens_by_keyword)

# pos_tagged_tokens_by_column = []

# for sentence in filtered_column:
#     tokens = nltk.word_tokenize(sentence)
#     pos_tagged_tokens_by_column.append(nltk.pos_tag(tokens))
    
# print(pos_tagged_tokens_by_column)