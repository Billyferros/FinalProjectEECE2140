from itertools import permutations as perms


class replaceTransSuggestions:
    '''
    corrects words by checking permutations of the word and replacing vowels of the
    word with other vowels
    '''

    def __init__(self, wrongWord, everyWord):
        self.wrongWord = wrongWord
        self.everyWord = everyWord

    def transposeTest(self):
        '''
        Checks for all transpositions of incorrectly spelled words that are real words
        :return: list of possible corrections for misspelled word
        '''

        suggest_List = []
        transpose_List = []

        perm = perms(self.wrongWord)  # all permutations

        for i in list(perm):
            transpose_List.append(i)  # place all list of permuted letters into another list
        attempts = []

        # convert list of characters to a string
        for words in transpose_List:
            attempt = ''
            for chars in words:
                attempt += chars
            attempts.append(attempt)

        # Form all strings into a list
        for word in attempts:
            if word in self.everyWord:
                suggest_List.append(word)
        suggestions = []

        # find any perms that are present in the english language
        for i in suggest_List:
            if i not in suggestions:
                suggestions.append(i)
        if len(suggestions) > 0:
            return suggestions
        else:
            return ''


    def replaceEachVowelTest(self):
        '''
        Replaces every vowel in the incorrect word with a different vowel in the
        alphabet, and checks if it's a possible correction.
        
        :return: list of possible corrections for misspelled word
        '''

        #string of vowels
        vowel = 'aeiouy'

        test_word = self.wrongWord
        temp_word = test_word
        corrected_words = []

        #loop through word in question to see if charcater is a vowel
        #and replace vowel to see if corrected word exists
        for i in range(len(test_word)):
            test_word = temp_word
            if test_word[i] in vowel:
                for letter in vowel:
                    #sandwich to create new word with replaced value
                    test_word = test_word[:i] + letter + test_word[i+1:]
                    if test_word in self.everyWord:
                        corrected_words.append(test_word)
                    if len(corrected_words) > 0:
                        return corrected_words
                    else:
                        return ''


    def adjKeyboardTest(self):
        '''
        replaces characters in word with adjacent letters on a qwerty keyboard
        and checks if they are a possible correction.

        :return: list of possible corrections for misspelled words
        '''


        #dictionary with alphabet key and adjacent letters on a qwerty keyboard associated with the key
        adjKeyboard = {
            'a':['q','w','s','x','z'],
            'b':['v','g','h','n'],
            'c':['x','d','f','v'],
            'd':['x','s','e','r','f','c'],
            'e':['w','s','d','f','r'],
            'f':['d','r','t','g','v','c'],
            'g':['y','h','b','v','f','r'],
            'h':['y','u','j','n','b','g'],
            'i':['u','j','k','l','o'],
            'j':['i','k','m','n','h','u'],
            'k':['l','m','j','i','o'],
            'l':['n','k','o','p'],
            'm':['n','j','k','l'],
            'n':['b','h','j','m'],
            'o':['p','l','k','i'],
            'p':['o','l'],
            'q':['w','a'],
            'r':['e','d','f','t'],
            's':['a','w','e','d','x','z'],
            't':['r','f','g','h','y'],
            'u':['y','h','j','k','i'],
            'v':['c','f','g','b'],
            'w':['q','a','s','d','e'],
            'x':['z','s','d','c'],
            'y':['t','g','h','u'],
            'z':['a','s','x']
        }



        test_word = self.wrongWord
        temp_word = test_word
        corrected_words = []

        #Iterate through by indexing letter by letter and check which letter corresponds with which key
        #Iterate through values of key and replace letter with adjcaent letters on keyboard.
        for i in range(len(test_word)):
            test_word = temp_word
            for letter in adjKeyboard[temp_word[i]]:
                # sandwich to create new word with replaced value
                test_word = test_word[:i] + letter + test_word[i + 1:]
                if test_word in self.everyWord:
                    corrected_words.append(test_word)
        if len(corrected_words) > 0:
            return corrected_words
        else:
            return ''

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
