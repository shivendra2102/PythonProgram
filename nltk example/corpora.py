from  nltk.corpus import gutenberg
from nltk.tokenize import  sent_tokenize
smaple = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(smaple)
print(tok[5:15])
  