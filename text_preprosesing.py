import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer

test = "This projects are amazing and very interesting, but it is also hard to write and doing it has been really tiring and I was very sleepy, amazingly!"

def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    return text

def trim(text):
    work_text = re.split(' ', text)
    work_text.pop()#проблем с остването на '' при clean
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


def text_tagger(text):
    new_text = []
    tagged_text = pos_tag(text)
    for word, tag in tagged_text:
        new_text.append(tuple([word, tag]))
    return new_text

#print(text_tagger(trim(clean(test))))
#print(pos_tag(trim(clean(test))))

part_speech_list = ['CC', 'EX', 'FW' 'IN', 'JJ', 'JJS', 'JJR', 'MD', 'NN', 'NNS', 'NNP','NNPS', 'PPS','PDP','POS','PRP','RB', 'RBR', 'RBS','VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']
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


#print(text_lemmatization(ready_to_tokenize(test)))

def tokenizer(text):
    new_text=[]
    for i in range(len(text)-1):
        bigram = text[i][0]+ " " +text[i+1][0]
        part_speech = text[i][1]+ " " +text[i+1][1]
        new_text.append((bigram, part_speech))
    return new_text




#print(tokenizer(ready_to_tokenize(test)))
