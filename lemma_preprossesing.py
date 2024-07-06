import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

#test = "This movie sounds amazing and I reccomend watching it, it is very fun."

def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text)
    text.lower()
    return text
#mahni poqsnitelnite
def trim(text):
    work_text = re.split(' ', text)
    #work_text.pop()#проблем с остването на '' при clean
    for word in work_text:
        if (word in set(stopwords.words('english'))) and (word != 'not'): #kakwo e set
            work_text.remove(word)
    return work_text

def text_tagger(text):
    new_text = []
    tagged_text = pos_tag(text)
    for word, tag in tagged_text:
        new_text.append(tuple([word, tag]))
    return new_text


part_speech_dict = {'JJ':'a', 'JJS':'a', 'JJR':'a', 'NN':'n', 'NNS':'n', 'NNP':'n','NNPS':'n','RB':'r', 'RBR':'r', 'RBS':'r','VB':'v', 'VBD':'v', 'VBG':'v','VBN':'v','VBP':'v', 'VBZ':'v'}
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
wnl = WordNetLemmatizer()
def text_lema(text):
    new_text = []
    for tuple in text:
        if tuple[1] in part_speech_dict.keys():
            new_word = wnl.lemmatize(tuple[0], part_speech_dict[tuple[1]])
        if tuple[1] not in part_speech_dict.keys():
            new_word = wnl.lemmatize(tuple[0])
        new_text.append((new_word, tuple[1]))
    return new_text


def lemmatization(text):
    return text_lema(text_tagger(trim(clean(text))))

def without_lema(text):
    return text_tagger(trim(clean(text)))


print(lemmatization("Theater was sold"))

#part_speech_list = ['DT', 'JJ', 'JJS', 'JJR', 'NN', 'NNS', 'NNP','NNPS','PDT','RB', 'RBR', 'RBS','VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']



