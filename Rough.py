import re
import math


#Preprocessing Documents

def token(text):
    # for removing punctuation from sentencesc
    text = re.sub(r'(\d+)', r'', text)
    text = text.replace('\n', '')
    text = text.replace(u',', '')
    text = text.replace(u'"', '')
    text = text.replace(u'(', '')
    text = text.replace(u')', '')
    text = text.replace(u'"', '')
    text = text.replace(u':', '')
    text = text.replace(u"'", '')
    text = text.replace(u"’", '')
    text = text.replace(u"‘", '')
    text = text.replace(u"‘‘", '')
    text = text.replace(u"’’", '')
    text = text.replace(u"''", '')
    text = text.replace(u".", '')
    text = text.replace(u'?', u'।')

    sentences = text.split(u"।")
    # print(sentences)
    tokens = []
    for each in sentences:
        word_list = each.split()
        tokens = tokens + word_list

    # print(tokens)
    stop_removed_tokens = []
    f = open("stopwords.txt", encoding="utf8")
    stopwords = [x.strip() for x in f.readlines()]
    tokens = [i for i in tokens if i not in stopwords]
    return tokens


# for reading input file
text1 = open("bankingSystem200.txt", encoding="utf8").read()
# for reading input file
text2 = open("bankingRefrence200.txt", encoding="utf8").read()
text1Tokens= token(text1)
text2Tokens=token(text2)
#print(set(text1Tokens))
#print(set(text2Tokens))

#overlapping Word calculation
def overlapping(input1,input2):
    count=0
    for word1 in input1:
        for word2 in input2:
            if(word2==word1):
                count=count+1
                break
    return count


#print(overlapping(text1Tokens,text2Tokens))
#rint(len(text2Tokens))


#recall calculation
def recall(overWord,refSumLen):
    return overWord/refSumLen

#precision calculation

def precision(overWord,sysSumLen):
    return overWord/sysSumLen


#fmeasure calculation

def fmasure(recall,precision):
    temp=(2*recall*precision)/(recall+precision)
    return temp


r=recall(overlapping(text1Tokens,text2Tokens),len(text2Tokens))
p=precision(overlapping(text1Tokens,text2Tokens),len(text1Tokens))
print("ROUGUE-1 recall" +" "+str(r))
print("ROUGUE-1 precision" +" "+str(p))
print("ROUGUE-1 fmeasure" +" "+str(fmasure(r,p)))




