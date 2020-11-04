import re
import pickle
import string
import numpy as np
import pandas as pd

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from spacy import displacy, lemmatizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Clean text so it's ready for preprocessing

def clean(corpus):
    """
    Takes a corpus of speeches as an argument and cleans it so it's ready to be pre-processed
    """

    clean_corpus = [] # Initiate clean_corpus
    
    for speech in corpus:
        
        speech = speech[5:] # Removes meaningless intro

        for i in range(len(speech)):
            speech[i] = speech[i][speech[i].find('\n') + 1:] # Removes 'meaningless text hear (min:sec)\n' at the beginning of each paragraph
            speech[i] = speech[i].replace('[', '(') # Replaces brackets with paranthesis
            speech[i] = speech[i].replace(']', ')')
            speech[i] = re.sub(r"\([^)]*\)", '', speech[i]) # Removes meaningless text in parantheses

        speech = ','.join(speech) # Join all of the paragraphs into on huge string
        
        clean_corpus.append(speech)
        
    return clean_corpus

# Preprocess corpus

# Create tokenized corpus and preprocess text

def preprocess(corpus):
    """
    Takes in a corpus of speech strings, tokenizes, lemmatizes and removes stop words and punctuation for each speech
    """
    # Instantiate spacy
    nlp = spacy.load('en_core_web_sm')
    # Create our list of punctuation marks
    punctuations = '!"#$%&\'()’*+,-./:”;<=>?@[\\]^_`{|}~'

    # Create our list of stopwords
    stop_words = spacy.lang.en.stop_words.STOP_WORDS
    
    # Establish weird words in our corpus to be filtered out
    weird_words = ['abc', 'c', 'o', 'n']
    
    # Establish new_corpus
    new_corpus = []
    
    # Loop through each speech in the corpus and preprocess
    for speech in corpus:
        
        # Tokenize speech
        speech_tokens = nlp(speech)
        
        # Lemmatizing each token and converting each token into lowercase
        speech_tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in speech_tokens]

        # Remove stop words, weird words and punctuations
        speech_tokens = [word for word in speech_tokens if word not in stop_words and word not in punctuations \
                         and word not in weird_words]

        # Remove numbers
        speech_tokens = [word for word in speech_tokens if word.isalpha()]
                
        # Join it all into one string
        speech_tokens = ','.join(speech_tokens)
        
        # Append to new_corpus
        new_corpus.append(speech_tokens)
    
    return new_corpus