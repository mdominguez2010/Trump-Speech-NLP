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

def clean(speech):
    """
    Takes a speech as an argument and cleans it so it's ready to be pre-processed
    """
    # Initiate clean_corpus
    
    # Removes meaningless intro    
    speech = speech[5:] 

    for i in range(len(speech)):
        # Removes 'meaningless text hear (min:sec)\n' at the beginning of each paragraph
        speech[i] = speech[i][speech[i].find('\n') + 1:] 
        # Replaces brackets with paranthesis
        speech[i] = speech[i].replace('[', '(') 
        speech[i] = speech[i].replace(']', ')')
        # Removes meaningless text in parantheses
        speech[i] = re.sub(r'\([^)]*\)', '', speech[i]) 
        
    # Join all of the paragraphs into on huge string
    speech = ','.join(speech) 
        
    return speech

# Tokenize corpus and preprocess text

def preprocess(clean_speech):
    """
    Takes in a speech, tokenizes and breaks it out into sentences, lemmatizes and removes stop words and punctuation for each speech
    """
    
    # Create our list of punctuation marks
    punctuations = '!"#$%&\'()’*+,-./:”;<=>?@[\\]^_`{|}~'

    # Create our list of stopwords
    stop_words = spacy.lang.en.stop_words.STOP_WORDS
    
    # Establish weird words in our corpus to be filtered out
    weird_words = ['abc', 'c', 'o', 'n']
    
    # Etablish new sentence list
    sentence_list = []
    
    # Tokenizer
    tokenizer = spacy.load('en_core_web_sm')
    speech_tokens = tokenizer(clean_speech)

    for sentence in speech_tokens.sents:
        
        # Lemmatizing each token and converting each token into lowercase
        sentence = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in sentence]
        
        # Remove stop words, weird words and punctuations
        sentence = [word for word in sentence if word not in stop_words and word not in punctuations \
                    and word not in weird_words]

        # Remove numbers
        sentence = [word for word in sentence if word.isalpha()]
        
        # Join all words in sentence
        sentence = ','.join(sentence)
        
        # Append to new list
        sentence_list.append(sentence)
    
    return sentence_list