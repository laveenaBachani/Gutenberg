import heapq
import re

def getTotalNumberOfWords(input):
    return len(input.split())

def getTotalUniqueWords(input):
    items=set()
    for words in input.split():
        items.add(words)
    print("Number of unique words: " , len(items))
    return items

def get20MostFrequentWords(text):
    map = {}
    str = ''
    for i in range(0,len(text)):
        if text[i] ==' ' or '\n' in text[i]:
            str = str.strip('\n')
            if str.strip(' ') != '' and str.strip('\n') != '':
                if str.lower() in map:
                    map[str.lower()] = map[str.lower()]+1
                else:
                    map[str.lower()] = 1
            str = ''
        str += text[i]

    heap = [(-value, key) for key, value in map.items()]
    largest = heapq.nsmallest(20, heap)
    largest = [(key, -value) for value, key in largest]
    return largest

def get20MostInterestingFrequentWords(text,num):
    with open("1-1000.txt",'r') as w:
        filterWords = w.read()
        filterWordsList = filterWords.split("\n")
        filterWordsList = filterWordsList[0:num]
        map = {}
        str = ''
        for i in range(0, len(text)):
            if text[i] == ' ' or '\n' in text[i]:
                str = str.strip('\n')
                str = str.strip(' ')
                if str.strip(' ') != '' and str.strip('\n') != '' and str.lower() not in filterWordsList:
                    if str.lower() in map:
                        map[str.lower()] = map[str.lower()] + 1
                    else:
                        map[str.lower()] = 1
                str = ''
            str += text[i]

        heap = [(-value, key) for key, value in map.items()]
        largest = heapq.nsmallest(20, heap)
        largest = [(key, -value) for value, key in largest]
        return largest

def get20LeastFrequentWords(text):
    map = {}
    str = ''
    for i in range(0, len(text)):
        if text[i] == ' ' or '\n' in text[i]:
            str = str.strip('\n')
            if str.strip(' ') != '' and str.strip('\n') != '' and (not str.strip(' ').isnumeric()):
                if str.lower() in map:
                    map[str.lower()] = map[str.lower()] + 1
                else:
                    map[str.lower()] = 1
            str = ''
        str += text[i]

    heap = [(value, key) for key, value in map.items()]
    smallest = heapq.nsmallest(1100, heap)
    smallest = [(key, value) for value, key in smallest]
    return smallest

def getFrequencyOfWord(text, word):
    freq = []
    words = text.split()
    count = 0
    for i in range(0,len(words)):
        if(words[i] == "CHAPTER"):
            freq.append(count)
            count = 0
        else:
            if(words[i].lower() == word.lower()):
                count+=1
    freq.append(count)
    freq.pop(0)
    return freq


def getChapterQuoteAppears(text,sentence):
    punctuations = '''()-[]{};:'"\,<>/@#$%^&*_~'''
    res = ""
    for char in text:
        if char not in punctuations:
            res = res + char;
    sentSplit= re.compile('[.*!]').split(res)
    chapChapter = 0
    for sent in sentSplit:
        sent.strip('\n');
        if "CHAPTER" in sent:
            chapChapter = chapChapter+1
        else:
            if sentence  in sent:
                return chapChapter
    return -1

