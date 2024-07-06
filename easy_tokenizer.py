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
import json


def clean(text): # accepts text
    text = re.sub('[^A-Za-z]+', ' ', text)
    #text.lower()
    return text

def trim(text): #accepts text and returns list
    work_text = re.split(' ', text)
    #work_text.pop()
    new_text = []
    for word in work_text:
        if (word not in set(stopwords.words('english'))) or (word == 'not'): #kakwo e set
            new_text.append(word)
    return new_text

with open('sentiment_dictionary.json') as old_file:
    dict = json.load(old_file)

part_speech_dict = {'JJ':'a', 'JJS':'a', 'JJR':'a', 'NN':'n', 'NNS':'n', 'NNP':'n','NNPS':'n','RB':'r', 'RBR':'r', 'RBS':'r','VB':'v', 'VBD':'v', 'VBG':'v','VBN':'v','VBP':'v', 'VBZ':'v'}
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
wnl = WordNetLemmatizer() #accepts list of words and returns them lemmatized
def text_lema(text):
    new_text = []
    text = pos_tag(text)
    for word in text:
        part_of_speech = word[1]
        single_word = word[0]
        if part_of_speech in part_speech_dict.keys():
            new_word = wnl.lemmatize(single_word, part_speech_dict[part_of_speech])
            new_text.append(new_word)
            if new_word in dict:
                dict[new_word][1] += 1
            else:
                dict[new_word] = [0,1,0]
        
    return new_text

def single_tokenize(text):
    return text_lema(trim(clean(text)))
    

def create_new_files(folder_path, new_path):
    for filename in os.listdir(folder_path):
         if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                new_content = single_tokenize(content)
                new_filename = "tokenized_" + filename
                new_file_path = os.path.join(new_path,new_filename)
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(str(new_content))
create_new_files('./aclImdb/test/example', './test_neg')

with open("sentiment_dictionary.json", "w") as out_file:
    json.dump(dict, out_file)
