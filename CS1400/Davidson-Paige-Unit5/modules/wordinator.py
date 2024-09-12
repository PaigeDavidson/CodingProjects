# Paige Davidson
# CS1400 - MO1
# Assignment ??

class Wordinator:
    def __init__(self, word):
        self.__word = word

    def getWord(self):
        return self.__word

    def __lt__(self, other):
        return self.__word.lower() < other.getWord().lower()

    def __str__(self):
        return self.__word

    def __firstWord(self, wordinator1, wordinator2):
        self.__word = min(wordinator1.lower(), wordinator2.lower)

    def __add__(self, other):
        return self.__bigWord(self.__word, other.__word)

    def __bigWord(self, wordinator1, wordinator2):
        word = wordinator1 + wordinator2
        word = word.capitalize()
        return word

    def __mul__(self, factor):
        return self.__wordFactor(self.__word, factor)

    def __wordFactor(self, wordinator1, factor):
        word = wordinator1 * factor
        word = word.upper()
        return word

    def __truediv__(self, other):
        return self.__mixWords(self.__word, other.__word)

    def __mixWords(self, wordinator1, wordinator2):
        string = " "
        for i in range(0, min(len(wordinator1), len(wordinator2))):
            string = string + wordinator1[i] + wordinator2[i]
        if len(wordinator1) > len(wordinator2):
            end = wordinator1[len(wordinator2): len(wordinator1)]
            string = string + end
        else:
            end = wordinator2[len(wordinator1): len(wordinator2)]
            string = string + end
        return string.title()

    def __mod__(self, other):
        return self.__midWords(), other.__midWords()

    def __midWords(self):
        half = len(self.__word) // 4
        last = int(len(self.__word) * (3/4))
        first = self.__word[half + 1: last]
        return first

    def __sub__(self, other):
        return self.__switchCase(), other.__switchCase()

    def __switchCase(self):
        word = ""
        for i in self.__word:
            if i.islower():
                word += i.upper()
            else:
                word += i.lower()
        return word

    def backWordSlice(self):
        word = self.__word[:: -1]
        return word

    def backWordManual(self):
        word = ""
        for i in range(len(self.__word) - 1, -1, -1):
            word = word + self.__word[i]
        return word
