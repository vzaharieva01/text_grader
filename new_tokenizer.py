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
test = "It is amazing.This is by far one of the best biographical films of recent times. I'll go so far as to put it up there with Ray and The Aviator. It is the story of a young, bi-racial boy who lives in a boarding house run by the amazing Miss Rachael aka Nanny. You will fall in love with Nanny, a woman who gives all of herself to those around her. S. Epatha Merkerson brings the character to life beautifully, and the other cast members are do the same. If I were to praise each actor for the way they played their roles, I'd have to mention everyone in the entire cast. <br /><br />The music in this film perfectly blends with the story, almost dictates the way it goes. And what's more, this film is actually entertaining. It won't bore you at all, not even for a minute!I highly recommend this film to anyone wanting to spend an evening at home watching a very smart, very entertaining, quality film."
stop_words = ['me', 'my', 'myself', 'we','is' ,'our', 'ours','was', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'him', 'his', 'himself',  "she's", 'her', 'hers', 'herself', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'are', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def split_into_sentences(text):
    # Use regex to split text by period, exclamation point, or question mark
    sentences = re.split(r'(?<=[.!?,]) +| and ', text)
    
    # Strip leading and trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
   
    
    return sentences #list of simple sentences

#print(split_into_sentences(test))
def clean(text): # accepts sentence
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = text.lower()
    return text

def trim(text): #accepts sentence and returns list
    work_text = re.split(' ', text)
    #work_text.pop()
    new_text = []
    for word in work_text:
        if word not in stop_words: #kakwo e set
            new_text.append(word)
    return new_text


def text_tagger(text): #acepts list and returns list ot tagget tuples
    new_text = []
    tagged_text = pos_tag(text)
    for word, tag in tagged_text:
        if tag in part_speech_dict:
            new_text.append(tuple([word, part_speech_dict[tag]]))
    return new_text


part_speech_dict = {'JJ':'a', 'JJS':'a', 'JJR':'a', 'NN':'n', 'NNS':'n', 'NNP':'n','NNPS':'n','RB':'r', 'RBR':'r', 'RBS':'r','VB':'v', 'VBD':'v', 'VBG':'a','VBN':'v','VBP':'v', 'VBZ':'v'}
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

print(ready_tokenize(test))
def tokenizer(tagget_text):
    #current_token = []
    ending = len(tagget_text) - 1
    def make_token(current_position, next_position, tagget_text, end,current_token,tokens): # cur and next are numbers
        if current_position >= end:
            if current_token != ' ':
                tokens.append(current_token)
            return tokens
        #if current_position == end:
        #    if current_token != ' ':
        #        current_token = tokens.pop() + tagget_text[current_position][0]
        #        tokens.append(current_token)
        #    else:
        #        current_token += (tagget_text[current_position][0] + " ")
        #        tokens.append(current_token)
        #    return tokens
        
        if tagget_text[current_position][1] == 'a' and tagget_text[next_position][1] == 'a':
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end, current_token,tokens)
        
        if tagget_text[current_position][1] == 'a' and tagget_text[next_position][1] == 'n':
            current_token += (tagget_text[current_position][0] + " " + tagget_text[next_position][0])
            tokens.append(current_token)
            return make_token(next_position +1, next_position+2, tagget_text, end, ' ',tokens)
        
        if tagget_text[current_position][1] == 'a' and tagget_text[next_position][1] in ['v', 'r'] :
            current_token += (tagget_text[current_position][0] + " ",tokens)
            tokens.append(current_token)
            return make_token(next_position, next_position+1, tagget_text,end, ' ',tokens)
        
        if tagget_text[current_position][1] == 'r' and tagget_text[next_position][1] == 'r':
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end,current_token,tokens)
        
        if tagget_text[current_position][1] == 'r' and tagget_text[next_position][1] == 'v':
            current_token += (tagget_text[current_position][0] + " " + tagget_text[next_position][0])
            tokens.append(current_token)
            return make_token(next_position+1, next_position+2, tagget_text,end, ' ',tokens)
        
        if tagget_text[current_position][1] == 'r' and tagget_text[next_position][1] in ['n', 'a'] :
            current_token += (tagget_text[current_position][0] + " ")
            tokens.append(current_token)
            return make_token(next_position, next_position+1, tagget_text,end, ' ',tokens)
        
        if tagget_text[current_position][1] == 'v' and tagget_text[next_position][1] == 'v':
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end, current_token,tokens)
        
        if tagget_text[current_position][1] == 'v' and tagget_text[next_position][1] in ['n', 'r']:
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end, current_token,tokens)
        
        if tagget_text[current_position][1] == 'v' and tagget_text[next_position][1]  == 'a' :
            current_token += (tagget_text[current_position][0] + " ")
            tokens.append(current_token)
            return make_token(next_position, next_position+1, tagget_text,end, ' ',tokens)  
           
        if tagget_text[current_position][1] == 'n' and tagget_text[next_position][1] == 'n':
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end, current_token,tokens)
        
        if tagget_text[current_position][1] == 'n' and tagget_text[next_position][1] == 'a':
            current_token += (tagget_text[current_position][0] + " ")
            return make_token(next_position, next_position+1, tagget_text,end,current_token,tokens)
        
        if tagget_text[current_position][1] == 'n' and tagget_text[next_position][1]  == 'r' :
            current_token += (tagget_text[current_position][0] + " ")
            tokens.append(current_token)  
            return make_token(next_position, next_position+1, tagget_text,end, ' ',tokens)
        
        if tagget_text[current_position][1] == 'n' and tagget_text[next_position][1]  == 'v' :
            if next_position+1 < end and tagget_text[next_position+1][1] in ['r', 'a']:
                current_token += (tagget_text[next_position+1][0] + " " +tagget_text[current_position][0])     
                return make_token(next_position+2, next_position+3, tagget_text,end, current_token,tokens)     
            else:
                current_token += (tagget_text[current_position][0] + " ")
                return make_token(next_position, next_position+1, tagget_text,end, current_token,tokens)
    return make_token(0,1,tagget_text, ending, " ",[])
        
def ready(text):
    ready_to_tokenize_list = []
    split_sentences = split_into_sentences(text)
    for sentence in split_sentences:
        new_sentence = text_lema(text_tagger(trim(clean(sentence))))
        ready_to_tokenize_list += new_sentence
    return ready_to_tokenize_list

def full_sentence(sentence):
    new_sentence = ready_tokenize(sentence)
    new_sentence =tokenizer(new_sentence)
    return new_sentence
def full_text(text):
    new_text = []
    text = split_into_sentences(text)
    for sentence in text:
        new_sentence = full_sentence(sentence)
        new_text += new_sentence
    return new_text

print(full_text(test))



    

#print(ready_tokenize(test))
#print(trim(clean("The sign an both good movie")))
