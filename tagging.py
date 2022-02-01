import nltk
nltk.download('punkt')
from extraction import filtered

pos_tagged_tokens = []

for sentence in filtered:
    tokens = nltk.word_tokenize(sentence)
    pos_tagged_tokens.append(nltk.pos_tag(tokens))
    
print(pos_tagged_tokens)
    