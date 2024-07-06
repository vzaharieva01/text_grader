import re
import nltk
import os
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.corpus import wordnet
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
from nltk.stem import WordNetLemmatizer


def clean(text): # accepts text
    text = re.sub('[^A-Za-z]+', ' ', text)
    #text.lower()
    return text

def trim(text): #accepts text and returns list
    work_text = re.split(' ', text)
    work_text.pop()
    new_text = []
    for word in work_text:
        if (word not in set(stopwords.words('english'))) or (word == 'not'): #kakwo e set
            new_text.append(word)
    return new_text


part_speech_dict = {'JJ':'a', 'JJS':'a', 'JJR':'a', 'NN':'n', 'NNS':'n', 'NNP':'n','NNPS':'n','RB':'r', 'RBR':'r', 'RBS':'r','VB':'v', 'VBD':'v', 'VBG':'v','VBN':'v','VBP':'v', 'VBZ':'v'}
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
wnl = WordNetLemmatizer() #accepts list of tagget tuples and returns them lemmatized
def text_lema(text):
    new_text = []
    for word in text:
        if pos_tag(word) in part_speech_dict.keys():
            new_word = wnl.lemmatize(word, pos_tag(word))
        if pos_tag(word) not in part_speech_dict.keys():
            pass
        new_text.append(new_word)
    return new_text

def single_tokenize(text):
    return text_lema(trim(clean(text)))

def create_new_files(folder_path):
    for filename in os.listdir(folder_path):
         if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                new_content = single_tokenize(content)
                new_filename = "tokenized_" + filename
                new_file_path = os.path.join(folder_path, new_filename)
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(content)
create_new_files('home/acllmdb/test/neg')
