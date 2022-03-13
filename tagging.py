import nltk
import os.path
import os
nltk.download('punkt')
from extraction import filtered_short_desc_by_keyword, filtered_short_desc, filtered_description_by_keyword, filtered_description

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
        
        versioning = 0
        directory_len = len(os.listdir('verbs')) +1
        
        for version in range(directory_len):
            if os.path.exists(f'nouns/extracted_verbs_{versioning}.txt'):
                versioning += 1
                continue
            else:
                with open(f'nouns/extracted_verbs_{versioning}.txt', 'w+') as file:
                    for i in verbs:
                        file.write(i + '\n')
                
    def extract_tagged_nouns(self, data_to_extract):
        
        nouns = []
        
        for list in data_to_extract:
            for item in list:
                if 'N' in item[1]:
                    nouns.append(item[0])
                    
        return nouns
    
    def save_extracted_nouns_to_file(self, nouns):
        
        versioning = 0
        directory_len = len(os.listdir('nouns')) +1
        
        for version in range(directory_len):
            if os.path.exists(f'nouns/extracted_nouns_{versioning}.txt'):
                versioning += 1
                continue
            else:
                with open(f'nouns/extracted_nouns_{versioning}.txt', 'w+') as file:
                    for i in nouns:
                        file.write(i + '\n')
    
tag_short_desc = Tagging(filtered_short_desc)

tag_column = tag_short_desc.tag_data()
extract_verbs = tag_short_desc.extract_tagged_verbs(tag_column)
print(extract_verbs)
extract_nouns = tag_short_desc.extract_tagged_nouns(tag_column)
tag_short_desc.save_extracted_nouns_to_file(extract_verbs)
tag_short_desc.save_extracted_verbs_to_file(extract_nouns)

# tag_description = Tagging(filtered_description)
# tag_column = tag_description.tag_data()
# extract_verbs = tag_description.extract_tagged_verbs(tag_column)
# extract_nouns = tag_description.extract_tagged_nouns(tag_column)
# tag_description.save_extracted_nouns_to_file(extract_verbs)
# tag_description.save_extracted_verbs_to_file(extract_nouns)
