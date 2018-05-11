import re
import math
# for reading input file
text=open("hindi1.txt", encoding="utf8").read()
sentences=text.split(u"।")
#print(sentences)
#count=0
#for i in sentences:
    #count +=1
    #print(i)
   # print('\n')
#print(count)
#sentenceGraph= [][]
sentToken= [] #each sentence containg token
for sent in sentences:
    temp=sent.split()
    f = open("stopwords.txt", encoding="utf8")
    stopwords = [x.strip() for x in f.readlines()]
    token = [i for i in temp if i not in stopwords]
    sentToken.append(token)
#print(sentToken)
#retuen weight of two sentences
def weight(i,j):
    sent1=sentToken[i]
    sent2=sentToken[j]
    return len(list(set(sent1).intersection(sent2)))

sentLen=len(sentences)

sentencesGraph= [[0 for x in range(sentLen)] for y in range(sentLen)]
for i in range(0,sentLen):
    for j in range(0,sentLen):
        if i!=j:
            sentencesGraph[i][j] = weight(i, j)
        else:
            sentencesGraph[i][j]=0


senSimlariy= []
sum=0
for i in range(0,sentLen):
    for j in range(0,sentLen):
        sum +=sentencesGraph[i][j]
    senSimlariy.append(sum)
    sum=0
print(senSimlariy)



