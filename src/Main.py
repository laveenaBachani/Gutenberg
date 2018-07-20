import Utility
import string
def main():
    File_name = "Book.txt"
    with open(File_name, "r")as book:
        s = book.read()
        translator = str.maketrans('', '', string.punctuation)
        text = s.translate(translator)
        # print("getTotalNumberOfWords" ,Utility.getTotalNumberOfWords(text))
        # print("getTotalUniqueWords", Utility.getTotalUniqueWords(text))
        # print("get20MostFrequentWords",Utility.get20MostFrequentWords(text))
        # num = 100
        # print("get20MostInterestingFrequentWords ",Utility.get20MostInterestingFrequentWords(text,num))
        print("get20LeastFrequentWords ", Utility.get20LeastFrequentWords(text))


if __name__ == "__main__":
    main()