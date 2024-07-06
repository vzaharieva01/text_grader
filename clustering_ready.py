import re
from lemma_preprossesing import lemmatization, without_lema
from rule_based_tokenizer import tokenizer
from nltk.corpus import stopwords
#test = "This movie is interesting and fun to watch, but the actors play poorly. I liked it and i would reccomend it, the setting was beautiful. STill it was poorly written."
new = " Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism."
new1 = "The sign of a good movie is that it can toy with our emotions. This one did exactly that."
new2 = "The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half."
new3 = "While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying."
new4 = "This movie was great, and I suggest that you go see it before you judge."
def break_sentences(text):
    text = text.split('. ')
    new_text = []
    for sentence in text:
        new_text.append(sentence.replace('\n', ''))
    return new_text


def ready(text):
    ready_text = []
    for j in range(len(text)):
        lematized = lemmatization(text[j])
        new_sentence = tokenizer(lematized, 0, len(lematized)-1)
        for i in range(len(new_sentence)):
            ready_text.append(new_sentence[i])
    return ready_text
#print(ready(break_sentences(new)))

print(stopwords.words('english'))