#def tokenizer(text):
#    new_text=[]
#    for i in range(len(text)-1):
#        bigram = text[i][0]+ " " +text[i+1][0]
#        part_speech = text[i][1]+ " " +text[i+1][1]
#        new_text.append((bigram, part_speech))
#    return new_text
test = [('Beautifully', 'RB'), ('do', 'VBN'), ('Movie', 'NNP'), ('sound', 'VBZ'), ('amazing', 'JJ')]
tokenized_text = []
start_index = 0 
end_index = len(test) - 1
def tokenizer (tagget_text, current, end):
    if tagget_text[current][1] in ['NN', 'NNS', 'NNP','NNPS']:
        if tagget_text[current+1][1] in ['NN', 'NNS', 'NNP','NNPS']:
            tokenized_text.append(tagget_text[current][1]+tagget_text[current+1][1])
        if tagget_text[current+1][1] in ['RB', 'RBR', 'RBS']:
            tokenized_text.append(tagget_text[current][1])
        if tagget_text[current+1][1] in ['JJ', 'JJS', 'JJR']:
            tokenized_text.append(tagget_text[current+1][1])
        if tagget_text[current+1][1] in ['VB', 'VBD', 'VBG','VBN','VBP', 'VBZ'] and tagget_text[current+2][1] in ['RB', 'RBR', 'RBS'] :
            tokenized_text.append(tagget_text[current+2][1] + tagget_text[current][1])
    