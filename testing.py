import re
import nltk
from nltk.corpus import stopwords # какво е това
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text)
    text.lower()
    return text

def trim(text):
    work_text = re.split(' ', text)
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

tokenized_text = []
negation_list = ['not', 'never', 'neither', 'barely', 'hardly', ' scarcely', 'no']
#def negation_parser(tagget_text)

#def adjective_parser(text):
   # for tuple in text:


def find_closest_noun(tagget_text, current):
    if current < len(tagget_text)-1:
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS', 'PRP']:
            return tagget_text[current+1][0]
        else:
            find_closest_noun(tagget_text, current+1)
    else:
        return None
    
def find_closest_verb(tagget_text, current):
    if current < len(tagget_text)-1:
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']:
            return tagget_text[current+1][0]
        else:
            find_closest_verb(tagget_text, current+1)
    else:
        return None

list_assosiated_adjectives = []
list_assosiated_adverbs = []

def tokenizer (tagget_text, current, end):
    if current == end:
        return tokenized_text
    if tagget_text[current][1] in ['NN', 'NNS', 'NNP','NNPS', 'PRP']: #noun
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS']: #noun
            tokenized_text.append(tagget_text[current][0]+ " " +tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['RB', 'RBR', 'RBS']:#adverb
            pass
        if tagget_text[current+1][1] in ['JJ', 'JJS', 'JJR']:#adjective
            tokenized_text.append(tagget_text[current][0] + " " + tagget_text[current+1][0])
            list_assosiated_adjectives.append(tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] and (current +1 < end) and (tagget_text[current+2][1] in ['RB', 'RBR', 'RBS']) : # verb and abverb
            tokenized_text.append(tagget_text[current+2][0] + " " + tagget_text[current][0])
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] and  (current+1 < end) and (tagget_text[current+2][1] in ['JJ', 'JJS', 'JJR']) : # verb and adjective
            tokenized_text.append(tagget_text[current+2][0] + " " + tagget_text[current][0])
            list_assosiated_adjectives.append(tagget_text[current+2][1])
        elif tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] :
            tokenized_text.append(tagget_text[current][0] + " " + tagget_text[current+1][0])
    
    if tagget_text[current][0] in list_assosiated_adjectives:
        return tokenizer(tagget_text, current+1,end)

    if (tagget_text[current][1] in ['JJ', 'JJS', 'JJR']): #adjective
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS']: #noun
            tokenized_text.append(tagget_text[current][0]+ " " + tagget_text[current+1][0])
            list_assosiated_adjectives.append(tagget_text[current][0])
        if tagget_text[current+1][1] in ['RB', 'RBR', 'RBS']:#adverb
            if find_closest_noun(tagget_text,current) == None:
                pass
            else:
                tokenized_text.append(tagget_text[current][0]+ ' ' + find_closest_noun(tagget_text,current))
                list_assosiated_adjectives.append(tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['JJ', 'JJS', 'JJR']:#adjective
            if find_closest_noun(tagget_text,current) == None:
                pass
            else:
                tokenized_text.append(tagget_text[current][0]+ ' ' + find_closest_noun(tagget_text,current))
                list_assosiated_adjectives.append(tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] : #verb
            pass
    
    if tagget_text[current][0] in list_assosiated_adverbs:
        return tokenizer(tagget_text, current+1,end)

    if tagget_text[current][1] in ['RB', 'RBR', 'RBS']: #adverb
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS']: #noun
            pass
        if tagget_text[current+1][1] in ['RB', 'RBR', 'RBS']:#adverb
            if find_closest_verb(tagget_text,current) == None:
                pass
            else:
                tokenized_text.append(tagget_text[current][0]+ ' ' + find_closest_verb(tagget_text,current))
                list_assosiated_adverbs.append(tagget_text[current][0])
        if tagget_text[current+1][1] in ['JJ', 'JJS', 'JJR']:#adjective
            pass
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] : #verb
            tokenized_text.append(tagget_text[current][0]+ " " +tagget_text[current+1][0])
            list_assosiated_adverbs.append(tagget_text[current][0])

    if tagget_text[current][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ']: #verb
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS']: #noun
            tokenized_text.append(tagget_text[current][0]+ " " + tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['RB', 'RBR', 'RBS']:#adverb
            tokenized_text.append(tagget_text[current][0]+ " " + tagget_text[current+1][0])
            list_assosiated_adverbs.append(tagget_text[current+1][0])
        if tagget_text[current+1][1] in ['JJ', 'JJS', 'JJR']:#adjective
            tokenized_text.append(tagget_text[current][0] + " " + tagget_text[current+1][0])
            list_assosiated_adjectives.append(tagget_text[current+1][1])
        elif tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] : #verb
            tokenized_text.append(tagget_text[current][0] + " " + tagget_text[current+1][0])
    return tokenizer(tagget_text, current+1, end)


print(lemmatization("Movie sounds boring"))
print(lemmatization("He plays terribly"))
print(lemmatization("Ne plays terribly"))
print(lemmatization("Flower smells bad"))
print(lemmatization("Flower smells bad"))
print(lemmatization("Meghan plays amazing"))
print(lemmatization("movie is terrifying"))