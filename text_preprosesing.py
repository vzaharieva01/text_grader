import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer

test = """Something inetersting. This movie sounds amazing.The flower smells bad
This is hard. Dress looks nice. Go to the store. Give up. Beacuse you want to. It was quite good. Very nice. 
This movie sucks. Movie sounds boring. nice movie. It went away silently. He does it with style!"""

def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text)
    
    return text

def trim(text):
    work_text = re.split(' ', text)
    #проблем с остването на '' при clean
    for word in work_text:
        if (word in set(stopwords.words('english'))) and (word != 'not'): #kakwo e set
            work_text.remove(word)
    return work_text


#pos_dict = {'a':wordnet.ADJ, 'v':wordnet.VERB, 'n':wordnet.NOUN, 'r':wordnet.ADV}
#def lemmatization_tagger(text):
#    new_text = []
#    tagged_text = pos_tag(text)
#    for word, tag in tagged_text:
#        new_text.append(tuple([word, pos_dict.get(tag[0])]))
#    return new_text
#wnl = WordNetLemmatizer()
#def text_lema(text):
#    new_text = []
#    for tuple in text:
#        if tuple[1] in pos_dict:
#            new_word = wnl.lemmatize(tuple[0], tuple[1])
#        if tuple[1] not in pos_dict:
#            new_word - wnl.lemmatize(tuple[0])
#        new_text.append(new_word)
#    return new_text


def text_tagger(text):
    new_text = []
    tagged_text = pos_tag(text)
    for word, tag in tagged_text:
        new_text.append(tuple([word, tag]))
    return new_text



part_speech_list = ['CC','DT' 'EX', 'FW' 'IN', 'JJ', 'JJS', 'JJR', 'MD', 'NN', 'NNS', 'NNP','NNPS', 'PPS','PDT','POS','RB', 'RBR', 'RBS','VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']
def part_speech_clear(text):
    for tupple in text:
        if tupple[1] not in part_speech_list:
            text.remove(tupple)
    return text



ps = PorterStemmer()
def text_stem(text):
    new_text = []
    for tuple in text:
        new_text.append((ps.stem(tuple[0]), tuple[1] ))
    return new_text

def ready_to_tokenize(text):
    text = clean(text)
    text = trim(text)
    text = text_tagger(text)
    text = part_speech_clear(text)
    text = text_stem(text)
    return text

print(ready_to_tokenize(test))







#print(tokenizer(ready_to_tokenize(test)))
