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
    sentSplit= re.compile('[.?!]').split(res)
    chapChapter = 0
    for sent in sentSplit:
        sent.strip('\n');
        if "CHAPTER" in sent:
            chapChapter = chapChapter+1
        else:
            if sentence  in sent:
                return chapChapter
    return -1

def generateSentence(s,firstWord):
    punctuations = '''()-[]{};:'"\,<>/@#$%^&*_~'''
    resstr = firstWord;
    resList = [firstWord]
    res = ""
    for char in s:
        if char not in punctuations:
            res = res + char;

    sentSplit = re.compile("[.?!]").split(res)
    sentSplitforinter = sentSplit
    map = {}
    for i in range(0,19):
        for sent in range(0,len(sentSplitforinter)):
            list = sentSplitforinter[sent].split()
            for k in range(0, len(list)):
                if(firstWord.lower() in list[k].strip('\n').lower()):
                    if(k!=len(list)-1):
                        if list[k+1].strip(' ') != '' and list[k+1].strip('\n') != '' and (not list[k+1].strip(' ').isnumeric()):
                            if list[k+1] in map:
                                print(list[k+1])
                                map[list[k+1]] +=1
                            else:
                                map[list[k+1]] = 1

        sent = 0
        max = 0
        keyWord = ""
        for key,value in map.items():
            if(value>max and key not in resList):
                max = value
                keyWord = key
        resstr +=" "+keyWord
        resList.append(keyWord)
        firstWord = keyWord
        map = {}
    return resstr

def getAutocompleteSentence(text, IncompleteSent):
    punctuations = '''()-[]{};:'"\,<>/@#$%^&*_~'''
    res = ""
    for char in text:
        if char not in punctuations:
            res = res + char
    sentSplit = re.compile("[.?!]").split(res)
    t =Trie()
    for sent in sentSplit:
        t.insert(sent.lower())
    str = ""
    mathed = []
    last = t.search(mathed,str,IncompleteSent)
    if not last:
        return mathed
    else:
        mathed = t.expand(mathed,IncompleteSent,last)
        return mathed








class TrieNode :
    # Trie node class
    def __init__(self):
        self.children = [None] * 27

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False



class Trie:
# Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            if('\n' not in key[level] and '|' not in key[level] and not key[level].isnumeric()):
                if(key[level] in ' '):
                    index = 26
                else:
                    index = self._charToIndex(key[level])
                if not pCrawl.children[index]:
                    pCrawl.children[index] = self.getNode()
                pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self,res,s, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            if key[level] == ' ':
                index = 26
            else:
                index = self._charToIndex(key[level])
            if index == 26:
                if not pCrawl.children[26]:
                    return None
                s+= chr(32)
            else:
                if not pCrawl.children[index]:
                    return None
                s += chr(97 + index)
            pCrawl = pCrawl.children[index]
        return pCrawl

    def expand(self,res,s,last):
        for i in range(0,27):
            if(last.children[i] !=None):
                if i == 26:
                    s +=' '
                else:
                    num = i+97
                    s += chr(num)
                self.expand(res,s,last.children[i])
        if(last.isEndOfWord):
            res.append(s)

        return res;