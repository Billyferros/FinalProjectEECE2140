class letterCorrections:
    '''
    Performs corrections tests on possible missing letter or unintended
    double letters.
    '''


    def __init__(self, wrongWord, everyWords):
        self.wrongWord = wrongWord
        self.everyWord = everyWords


    def singleLetterTest(self):
        '''
        checks if adding duplicate letter will correct word
        :return: list of possible corrections for misspelled word
        '''

        suggest_List = []
        singLet_List = []

        temporary = self.wrongWord
        #add letter at possible missing letter
        for i in range(len(temporary)):
            corrected_word = temporary[:i] + temporary[i] + temporary[i:]
            singLet_List.append(corrected_word)

        # confirm if word exists
        for word in singLet_List:
            if word in self.everyWord:
                suggest_List.append(word)

        suggestions = []
        # checks to see if changes are real words and returns list of ones that are
        for i in suggest_List:
            if i not in suggestions:
                suggestions.append(i)
        if len(suggestions) > 0:
            return suggestions
        else:
            return ''





    def doubleLetterTest(self):
        '''
        Examines word to test if a double letter mistake is present
        :return: list of possible corrections for misspelled word
        '''

        suggest_List = []
        dubLet_List = []

        #alters word so that one of the same consequtive letters is removed
        temp_wrong_word = self.wrongWord
        wrong_word = list(temp_wrong_word)

        i = 1
        while i < len(wrong_word):

            if wrong_word[i] == wrong_word[i - 1]:
                del wrong_word[i]
                dubLet_List.append(wrong_word[:])

            i += 1

        corrections = []


        # puts the word back into a list
        for word in dubLet_List:
            correction = ''
            for chr in word:
                correction += chr
            corrections.append(correction)

        # confirm word exists
        for word in corrections:
            if word in self.everyWord:
                suggest_List.append(word)

        suggestions = []
        # checks to see if double remove words are real and adds that to suggestions
        for i in suggest_List:
            if i not in suggestions:
                suggestions.append(i)
        if len(suggestions) > 0:
            return suggestions
        else:
            return ''
