import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

test = "Beautifully done. Movie sounds amazing."

def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text)
    text.lower()
    return text

def trim(text):
    work_text = re.split(' ', text)
    work_text.pop()#проблем с остването на '' при clean
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
#def tagger(text):
#    new_text = []
#    tagged_text = pos_tag(text)
#    for word, tag in tagged_text:
#        new_text.append(tuple([word, pos_dict.get(tag[0])]))
#    return new_text
part_speech_dict = {'DT': 'DT', 'ADJ':['JJ', 'JJS', 'JJR'], 'NOUN':['NN', 'NNS', 'NNP','NNPS'],'PDT':'PDT','ADV':['RB', 'RBR', 'RBS'],'VERB':['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']}
wnl = WordNetLemmatizer()
def text_lema(text):
    new_text = []
    for tuple in text:
        if tuple[1] in pos_dict:
            new_word = wnl.lemmatize(tuple[0], tuple[1])
        if tuple[1] not in pos_dict:
            new_word = wnl.lemmatize(tuple[0])
        new_text.append((new_word, tuple[1]))
    return new_text

print(text_tagger(trim(clean(test))))
#def lemmatization(text):
#    return text_lema(tagger(trim(clean(text))))

#print(lemmatization(test))


#def text_tagger(text):
#    new_text = []
#    tagged_text = pos_tag(text)
#    for word, tag in tagged_text:
#        new_text.append(tuple([word, tag]))
#    return new_text



#part_speech_list = ['DT', 'JJ', 'JJS', 'JJR', 'NN', 'NNS', 'NNP','NNPS','PDT','RB', 'RBR', 'RBS','VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']
#def part_speech_clear(text):
#    for tupple in text:
#        if tupple[1] not in part_speech_list:
#            text.remove(tupple)
#    return text

#def tagget(text):
#    return part_speech_clear(text_tagger(ready_to_tag(text)))

