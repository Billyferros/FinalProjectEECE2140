from CorrectionSuggestions import replaceTransSuggestions
from CorrectionSuggestions import letterCorrections
from CorrectionSuggestions import remLetterSuggest



class wordFixer:
    '''Corrects text file by replacing misspelled words with corrections'''

    @staticmethod
    def autocorrect_file(textFile, correctWords, incorrectWord, ind):
        '''
        corrects an incorrect word in the input file

        :param textFile: string input file with incorrect words
        :param correctWords: list of correction options
        :param incorrectWord: string word that needs to be corrected
        :param ind: index of the word in the list that will replace incorrect word

        :return: text file with correction
        '''

        #If second to last index is selected, do not change
        if ind == len(correctWords) - 2:
            return
        #If last index is selected, prompt the user to enter their own correction
        if ind == len(correctWords) - 1:
            file = open(textFile, "r+")
            line = file.readlines()
            for i in range(len(correctWords)):
                if ind == i:
                    correction = input("Please enter the word you meant to write: ")

        else:
            file = open(textFile, "r+")
            line = file.readlines()
            for i in range(len(correctWords)):
                if ind == i:
                    correction = correctWords[i]

        # replace incorrect word with correct word
        for words in line:
            if incorrectWord in words:
                correctedLine = words.replace(incorrectWord, correction)
                line = correctedLine



        file.truncate(0)
        file.seek(0)
        file.writelines(line)


class DisplayTextFile:
    '''Show entire text file'''

    def __init__(self, file):
        self.file = file

    def showFile(self):
        '''
        Shows contents of text file
        :return: The text file
        '''
        with open(self.file, encoding='utf8') as textFile:
            text = textFile.read()
        print(text)
        return ''


class punctuation_Remover:
    '''Remove punctuation'''
    def __init__(self, file):
        self.file = file

    @staticmethod
    def punct_remove(text):
        '''

        :param text: file of words
        :return: text of words with no special characters or punctuation
        '''
        for i in '.,;:"/?()[]{}<>-_!':
            text = text.replace(i, "")
        return text


class prepareText:
    '''Prepare text by removing punctuation, equalising all words to similar format'''
    def __init__(self, file):
        self.file = file

    @staticmethod
    def modifyText(file):
        '''
        Remove punctuationm make all characters lower ans split the text

        :param file: name of text file
        :return: list of modified text
        '''
        # opens file and removes punctuation and makes all characters lower
        with open(file, encoding='utf8') as text:
            modified_text = text.read()
        modified_text = punctuation_Remover.punct_remove(modified_text)
        modified_text = modified_text.lower()
        modified_text = modified_text.strip()
        modified_text = modified_text.split()
        return modified_text


class textCorrector:
    ''' Uses suggestion test methods from autocorrect classes to fix misspelled words at user's discretion '''

    def __init__(self, file):
        self.file = file

    def find_incorrect_words(self):
        '''
        searches for incorrectly spelled words and prints incorrect word with suggestions
        :return: none
        '''

        EnglishDict = {}
        # creates super dictionary
        with open('words.txt', encoding='utf8') as english_words:
            for word in english_words:
                word = word.strip()
                word = word.lower()
                EnglishDict[word] = word

        # opens file and removes punctuation and makes all characters lower
        user_text = prepareText.modifyText(self.file)

        wrong_words = []
        #form a list of all misspelled words in the text file
        for word in user_text:
            if word not in EnglishDict:
                wrong_words.append(word)

        #Iterate through list and correct misspelled words
        for word in wrong_words:
            alphabet = replaceTransSuggestions(word, EnglishDict)
            alphabet1 = letterCorrections(word, EnglishDict)
            alphabet2 = remLetterSuggest(word, EnglishDict)
            print(f'"{word}" is a potential spelling mistake. Did you mean: ')
            trans = replaceTransSuggestions.transposeTest(alphabet)  #possible suggestions found through transpose func
            vow = replaceTransSuggestions.replaceEachVowelTest(alphabet) #possible suggestions found through vowel func
            adj = replaceTransSuggestions.adjKeyboardTest(alphabet) #possible suggestions found through adjacent keyboard test
            remL = remLetterSuggest.removeLastLetter_Test(alphabet2)  #possible suggestions found through removing last letter func
            remF = remLetterSuggest.removeFirstLetter_Test(alphabet2)  #possible suggestions found through removing first letter func
            remFL = remLetterSuggest.removeFirstandLastLetter_Test(alphabet2) #Suggestions removing both first and last letter func
            dub = letterCorrections.doubleLetterTest(alphabet1)  #possible suggestions found through double func
            singl = letterCorrections.singleLetterTest(alphabet1)  #possible suggestions found through adding double func

            #create complete list of possible corrections
            corrections = [*vow, *trans, *adj, *remFL, *dub, *remL, *remF, *singl, 'Do not change', 'Enter my own correction']

            #prompt the user with list of possible corrections and ask
            #them to enter their input by index of correction
            for i in range(len(corrections)):
                print(f'\t{i}: {corrections[i]}')
            index = int(input("Which correction would you like to choose?\n"
                          "Enter the number associated with the correction"))
            while index > len(corrections) - 1:
                print("Invalid entry. Try again.")
                index = int(input("Which correction would you like to choose?\n"
                              "Enter the number associated with the correction "))

            #Add corrections to misspelled words in the text file
            wordFixer.autocorrect_file(self.file, corrections, word, index)

        #Display the correct text
        print("The corrected text is:")
        corrected_file = DisplayTextFile(self.file)
        print(DisplayTextFile.showFile(corrected_file))
        return ''