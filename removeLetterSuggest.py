class remLetterSuggest:
    '''
    Suggests possible corrections by removing first or last or both
    characters of the incorrect word
    '''

    def __init__(self, wrongWord, everyWords):
        self.wrongWord = wrongWord
        self.everyWord = everyWords


    def removeFirstLetter_Test(self):
        '''
        delete first letter of incorrect word and check if it exists

        :return: list of possible corrections for misspelled word
        '''

        # slice so that first letter of word is removed
        test_word = self.wrongWord[1:]
        corrected_words = []

        # if word exists in english language, add to list of corrections
        if test_word in self.everyWord:
            corrected_words.append(test_word)
            if len(corrected_words) > 0:
                return corrected_words
            else:
                return ''
        return ''

    def removeLastLetter_Test(self):
        '''
        delete first last letter of incorrect word and check if it exists
        :return: list of possible corrections for misspelled word
        '''

        # slice so that last letter is removed
        test_word = self.wrongWord[:-1]
        corrected_words = []

        # if word exists in english language, add to list of corrections
        if test_word in self.everyWord:
            corrected_words.append(test_word)
        if len(corrected_words) > 0:
            return corrected_words
        else:
            return ''

    def removeFirstandLastLetter_Test(self):
        '''
        delete first and last letter of incorrect word and check if it exists

        :return: list of possible corrections for misspelled word
        '''

        #slice so first and last letters are removed
        test_word = self.wrongWord[1:-1]
        corrected_words = []

        # if word exists in english language, add to list of corrections
        if test_word in self.everyWord:
            corrected_words.append(test_word)
        if len(corrected_words) > 0:
            return corrected_words
        else:
            return ''




