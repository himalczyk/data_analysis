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
    
    def extract_tagged_verbs(self, data_to_extract):
        
        verbs = []
        
        for list in data_to_extract:
            for item in list:
                if 'V' in item[1]:
                    verbs.append(item[0])
                    
        return verbs
    
    def save_extracted_verbs_to_file(self, verbs):
        
        with open('verbs/extracted_verbs.txt', 'w+') as file:
            for i in verbs:
                file.write(i + '\n')
                
    def extract_tagged_nouns(self, data_to_extract):
        
        nouns = []
        
        for list in data_to_extract:
            for item in list:
                if 'N' in item[1]:
                    nouns.append(item[0])
                    
        return nouns
    
    def save_extracted_nouns_to_file(self, verbs):
    
        with open('nouns/extracted_nouns.txt', 'w+') as file:
            for i in verbs:
                file.write(i + '\n')
    
tag = Tagging(filtered_column)

tag_column = tag.tag_data()
extract_verbs = tag.extract_tagged_verbs(tag_column)
print(extract_verbs)
extract_nouns = tag.extract_tagged_nouns(tag_column)
tag.save_extracted_nouns_to_file(extract_verbs)
tag.save_extracted_verbs_to_file(extract_nouns)