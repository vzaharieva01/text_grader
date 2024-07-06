from lemma_preprossesing import lemmatization

tokenized_text = []
negation_list = ['not', 'never', 'neither', 'barely', 'hardly', ' scarcely', 'no']
#def negation_parser(tagget_text)
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




