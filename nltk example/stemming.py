from nltk.stem import PorterStemmer
from nltk.tokenize import  word_tokenize

ps =  PorterStemmer()
example_words = ["pythom","pythoner","pythoned","pythonly"]
#for w in example_words :
    #print(ps.stem(w))

new_text = "It is very important pythonly when you are in python. All pythoners haave pythoned. "
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
