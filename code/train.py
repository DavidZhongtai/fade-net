import pandas as pd
import numpy as np
import re
import nltk
import sys
from nltk.corpus import stopwords

from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten
from keras.layers import GlobalMaxPooling1D
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer

def main():
    X_train, X_test, y_train, y_test = splitData()

    tokenizer = Tokenizer(num_words = 10000)
    tokenizer.fit_on_texts(X_train)

    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)

main()

def splitData():

    df = pd.read_csv("data.csv")

    y = df.label

    X_train, X_test, y_train, y_test = train_test_split(df['body'], y, test_size = 0.20, random_state = 63)

    return X_train, X_test, y_train, y_test
