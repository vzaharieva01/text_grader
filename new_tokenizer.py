import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.corpus import wordnet
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
test = "Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half."

#def words_around_commas(text):
    # Find all occurrences of words around commas
#    matches = re.findall(r'(\b\w+\b)\s*,\s*(\b\w+\b)', text)
#    for tuple in matches:
#        if pos_tag(tuple[0]) == pos_tag(tuple[1]):
#            matches.remove(tuple)
#    for tuple



def split_into_sentences(text):
    # Use regex to split text by period, exclamation point, or question mark
    sentences = re.split(r'(?<=[.!?,]) +', text)
    
    # Strip leading and trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return sentences #list of simple sentences

#print(split_into_sentences(test))

def clean(text): # accepts sentence
    text = re.sub('[^A-Za-z]+', ' ', text)
    #text.lower()
    return text

def trim(text): #accepts sentence and returns list
    work_text = re.split(' ', text)
    work_text.pop()
    new_text = []
    for word in work_text:
        if (word not in set(stopwords.words('english'))) or (word == 'not'): #kakwo e set
            new_text.append(word)
    return new_text


def text_tagger(text): #acepts list and returns list ot tagget tuples
    new_text = []
    tagged_text = pos_tag(text)
    for word, tag in tagged_text:
        if tag in part_speech_dict:
            new_text.append(tuple([word, part_speech_dict[tag]]))
    return new_text


part_speech_dict = {'JJ':'a', 'JJS':'a', 'JJR':'a', 'NN':'n', 'NNS':'n', 'NNP':'n','NNPS':'n','RB':'r', 'RBR':'r', 'RBS':'r','VB':'v', 'VBD':'v', 'VBG':'v','VBN':'v','VBP':'v', 'VBZ':'v'}
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
wnl = WordNetLemmatizer() #accepts list of tagget tuples and returns them lemmatized
def text_lema(text):
    new_text = []
    for tuple in text:
        if tuple[1] in part_speech_dict.keys():
            new_word = wnl.lemmatize(tuple[0], part_speech_dict[tuple[1]])
        if tuple[1] not in part_speech_dict.keys():
            new_word = wnl.lemmatize(tuple[0])
        new_text.append((new_word, tuple[1]))
    return new_text

def ready_tokenize(sentence):
    return text_lema(text_tagger(trim(clean(sentence))))

tokens = []
def tokenize(tagget_text, start, end): # accepts list of tagget lemmatized tuples
    current_token = ()
    def make_token(current_position, next_position, tagget_text): # cur and next are tuples
        if current_position[0]:
            pass
    

def ready(text):
    ready_to_tokenize_list = []
    split_sentences = split_into_sentences(text)
    for sentence in split_sentences:
        new_sentence = text_lema(text_tagger(trim(clean(sentence))))
        ready_to_tokenize_list += new_sentence
    return ready_to_tokenize_list


print(ready_tokenize(test))
#print(trim(clean("The sign an both good movie")))
