from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize
exampple_sen = "This is an example showing off stopword"
stop_words = set(stopwords.words("english"))
#print(stop_words)
words = word_tokenize(exampple_sen)
filtered_sentence = []
##for w in words:
    #if w not in stop_words :
        #filtered_sentence.append(w)
#print(filtered_sentence)
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
