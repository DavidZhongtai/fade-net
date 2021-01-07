import nltk

from bs4 import BeautifulSoup
from nltk.corpus import stopwords

def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

#Removing the square brackets
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

# Removing URL's
def remove_urls (text):
    return re.sub(r'http\S+', '', text)

def stopword_declare():
    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation)
    stop.update(punctuation)

#def remove_stopwords(text):



def main():
    print("test in cmdI")

main()
