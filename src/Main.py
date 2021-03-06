import Utility
import string
import difflib
def main():
    File_name = "Book.txt"
    with open(File_name, "r")as book:
        s = book.read()
        translator = str.maketrans('', '', string.punctuation)
        text = s.translate(translator)
        print("getTotalNumberOfWords" ,Utility.getTotalNumberOfWords(text))
        print("getTotalUniqueWords", Utility.getTotalUniqueWords(text))
        print("get20MostFrequentWords",Utility.get20MostFrequentWords(text))
        num = 100
        print("get20MostInterestingFrequentWords ",Utility.get20MostInterestingFrequentWords(text,num))
        print("get20LeastFrequentWords ", Utility.get20LeastFrequentWords(text))
        word = "Age could not wither it, nor custom stale Its infinite variety"
        print("getFrequencyOfWord ", Utility.getFrequencyOfWord(text,word))
        sentence = "blooming and fragrant"
        print("getChapterQuoteAppears ",Utility.getChapterQuoteAppears(s,sentence))
        firstWord = 'the'
        print("generateSentence", Utility.generateSentence(s,firstWord))
        Incompletesentence = "gentlemen"
        print("getAutocompleteSentence", Utility.getAutocompleteSentence(s, Incompletesentence))
        quote = "O the days of Qun Bess, were merry ol times!"
        print("findClosestMatchingQuote ",Utility.findClosestMatchingQuote(s,quote))

if __name__ == "__main__":
    main()