#deal with txt file

import codecs
import os
import math
import nltk
import operator
from nltk.tokenize import WordPunctTokenizer

def sep(text): #sep words
    pattern = r"""(?x)               # set flag to allow verbose regexps 
              (?:[A-Z]\.)+           # abbreviations
              |\d+(?:\.\d+)?%?       # numbers like currency and percentages 
              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
              |\.\.\.                # ellipsis 
              |(?:[.,;"'?():-_`])    # special characters
            """
    tx=nltk.regexp_tokenize(text, pattern)
    length=len(tx)
    for i in range(length):
        tx[i]=tx[i].lower()
    return tx

def deleteSw(ls, swlist):  # delete stopwords
    withoutswls = []
    for i in ls:
        if str(i) in swlist:
            continue
        else:
            withoutswls.append(str(i).lower())
    return withoutswls

def fp(filepath):  # iterate files, return list
    arr = []
    for root, dirs, files in os.walk(filepath):
        for fname in files:
            arr.append(root+"/"+fname)
    return arr

def read(path):  # read txt files, return list
    with codecs.open(path, 'r', 'utf-8') as f:
        data = f.read()
    return data

def readsw(path):  # read txt, return list
    f = open(path, encoding='utf-8')
    data = []
    for line in f.readlines():
        data.append(line)
    return data

def getSw(path):  # get stop words
    swls = []
    for i in readsw(path):
        outsw = str(i).replace('\n', '').lower()
        swls.append(outsw)
    return swls

def freqWord(wordlis):  # frequency, count, return dic
    freqword = {}
    for i in wordlis:
        if str(i) in freqword:
            count = freqword[str(i)]
            freqword[str(i)] = count+1
        else:
            freqword[str(i)] = 1
    return freqword

def corpus(filelist, swlist):  # words db
    alist = []
    for i in filelist:
        withoutswlist = deleteSw(sep(read(str(i))), swlist)
        alist.append(withoutswlist)
    return alist

def tf_idf(wordlis, filelist, corpuslist):  # TF-IDF, return dic
    outdic = {}
    tf = 0
    idf = 0
    dic = freqWord(wordlis)
    #outlis = []
    for i in set(wordlis):
        tf = dic[str(i)]/len(wordlis)    
        idf = math.log(len(filelist)/(wordinfilecount(str(i), corpuslist)+1))  
        tfidf = tf*idf  # calculate TF-IDF
        outdic[str(i)] = tfidf
    orderdic = sorted(outdic.items(), key=operator.itemgetter(1), reverse=True)  # order dic
    return orderdic

def wordinfilecount(word, corpuslist):  # files incl words count
    count = 0
    for i in corpuslist:
        for j in i:
            if word in set(j):
                count = count+1
            else:
                continue
    return count

def list_to_s(lis):  # list to str
    out = ''
    for i in lis:
        ech = str(i).replace("('", '').replace("',", '\t').replace(')', '')
        out = out+'\t'+ech+'\n'
    return out

def writeT(txt, path):  # write to txt
    f = codecs.open(path, 'a', 'utf-8')
    f.write(txt)
    f.close()
    return path

def main():
    swpath = r'/home/bunny/Documents/pm_plottu/text/stop_words.txt'
    swlist = getSw(swpath)  #get sw list
    print(swlist)
    filepath = r'/home/bunny/Documents/pm_plottu/text/words_db/a'
    filelist = fp(filepath)
    corpuslist = corpus(filelist, swlist)
    #print(corpuslist)
    outall = ''
    writeTpath = r'/home/bunny/Documents/pm_plottu/text/result/TFIDF.txt'
    for i in filelist:
        without_swlis = deleteSw(sep(read(str(i))), swlist)   # get list except for sw
        tfidfdic = tf_idf(without_swlis, filelist, corpuslist)        # calc TF-IDF
        titleary = str(i).split('/')
        title = str(titleary[-1]).replace('utf8.txt', '')
        echout = title+'\n'+list_to_s(tfidfdic)
        print(title+' done!')
        outall = outall+echout
    print(writeT(outall, writeTpath)+' done!')
main()

