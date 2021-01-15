import nltk
import re
import csv
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import pandas as pd


def main(file1, file2):
    print("test in cmdI")

def _clean_html_(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

#Removing the square brackets
def _remove_between_square_brackets_(text):
    return re.sub('\[[^]]*\]', '', text)

# Removing URL's
def _remove_urls_(text):
    return re.sub(r'http\S+', '', text)

def _stopword_declare_():
    stop = set(stopwords.words('english'))
    punctuation = list(re.punctuation)
    stop.update(punctuation)

#def remove_stopwords(text):

def _transfertoCSV_(filePath, outputPath):
    input_file = filePath
    output_file = outputPath
    num_columns = 1


    file = open(input_file, 'r', encoding = "utf-8")

    # Read the file
    new_text = file.read()

    # Create a list to keep all the words in file
    words = new_text.splitlines()
    line_break = 0

    # Add all the words in file to list
    '''for x in range(0, len(new_text)):
        for word in new_text[x].split():
            words.append(word + ',')'''

    # Write words into csv file
    f = open(output_file,'w')
    for x in range(0, len(words)):
        if (line_break == num_columns):
            f.write('\n')
            f.write(words[x])
            line_break = 1
        else:
            f.write(words[x])
            line_break += 1
    f.close()
    
def _assignheader_(input_file):

    #skip line assignments with bad lines 
    df = pd.read_csv(input_file, header = None, error_bad_lines=False) 

    #assign label header 
    df.to_csv(input_file, header = ['bodytext'], index = False)

'''label can be one of two values: 
    1: Fake News 
    0: True News '''
def _assignLabels_(input_file, label):
    df = pd.read_csv(input_file)

    #columnar assignment 
    df["label"] = label
    df.to_csv(input_file, index = False)

#assigns values to the news 
def _combineCSV_(file_1, file_2): 
    file1 = csv.reader(open(file_1))
    file2 = csv.reader(open(file_2))

    f = open("dataset.csv", "w")
    writer = csv.writer(f)

    for row in file_1:
        writer.writerow(row)
    for row in file_2:
        writer.writerow(row)
    f.close()

#call main class 

main()

