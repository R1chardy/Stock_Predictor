import nltk
from nltk.corpus import stopwords
import string
import spacy

""" 
Primary Author: Brian Fu
Referenced Code and ideas from https://colab.research.google.com/drive/1jp8Oi2s13g2B34SPjX5074FDBlhmUdgn?usp=sharing
"""

def preprocess(input_text):
    """This function returns a tokenized list of the preprocessed text input using a bag of words model"""
    nlp = spacy.load("en_core_sci_md")
    nlp.add_pipe("negex")

    input_text = input_text.strip()
    doc = nlp(input_text)
    negation_list = [0]*len(doc)
    tokens = list()
    stop = set(stopwords.words('english')+list(string.punctuation))

    for ent in doc.ents:
        if ent._.negex:
            index = ent.start
            while index < ent.end:
                negation_list[index] = 1
                index += 1
            
    for i,token in enumerate(doc):
        if str(token).lower() not in stop:
            if negation_list[i] == 1:
                tokens.append(("NEGEX_"+str(token).lower()))
            else:
                tokens.append(str(token).lower())

    return tokens


