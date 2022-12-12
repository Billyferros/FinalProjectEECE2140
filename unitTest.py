from implementCorrection import punctuation_Remover

incorrect = 'hhello'


EnglishDict = {}
# creates super dictionary
with open('words.txt', encoding='utf8') as f:
    for word in f:
        word = word.strip()
        word = word.lower()
        EnglishDict[word] = word

# opens file and removes punctuation and makes all characters lower
with open('words.txt', encoding='utf8') as text:
    modified_text = text.read()
modified_text = punctuation_Remover.punct_remove(modified_text)
modified_text = modified_text.lower()
modified_text = modified_text.strip()
modified_text = modified_text.split()


def doubleLetterTest(wrong, everyWord):
    '''
    Examines word to test if a double letter mistake is present
    :return: list of possible corrections for misspelled word
    '''

    suggest_List = []
    dubLet_List = []


    # alters word so that one of the same consequtive letters is removed
    temp_wrong_word = wrong
    wrong_word = list(temp_wrong_word)
    holder_word = wrong_word

    i = 1
    while i < len(wrong_word):

        print(dubLet_List)
        if wrong_word[i] == wrong_word[i - 1]:
            del wrong_word[i]
            dubLet_List.append(wrong_word[:])

        i += 1

    print(dubLet_List)


    print(dubLet_List)



    corrections = []

    # puts the word back into a list
    for word in dubLet_List:
        correction = ''
        for chr in word:
            correction += chr
        corrections.append(correction)

    # checks if word is real
    for word in corrections:
        if word in everyWord:
            suggest_List.append(word)

    suggestions = []
    # checks to see if permutations are real words and returns list of ones that are
    for i in suggest_List:
        if i not in suggestions:
            suggestions.append(i)
    if len(suggestions) > 0:
        return suggestions
    else:
        return ''


def adjKeyboardTest(wrong, everyWord):
    '''
    replaces characters in word with adjacent letters on a qwerty keyboard
    and checks if they are a possible correction.

    :return: list of possible corrections for misspelled words
    '''

    # dictionary with alphabet key and adjacent letters on a qwerty keyboard associated with the key
    adjKeyboard = {
        'a': ['q', 'w', 's', 'x', 'z'],
        'b': ['v', 'g', 'h', 'n'],
        'c': ['x', 'd', 'f', 'v'],
        'd': ['x', 's', 'e', 'r', 'f', 'c'],
        'e': ['w', 's', 'd', 'f', 'r'],
        'f': ['d', 'r', 't', 'g', 'v', 'c'],
        'g': ['y', 'h', 'b', 'v', 'f', 'r'],
        'h': ['y', 'u', 'j', 'n', 'b', 'g'],
        'j': ['i', 'k', 'm', 'n', 'h', 'u'],
        'k': ['l', 'm', 'j', 'i', 'o'],
        'l': ['n', 'k', 'o', 'p'],
        'm': ['n', 'j', 'k', 'l'],
        'n': ['b', 'h', 'j', 'm'],
        'o': ['p', 'l', 'k', 'i'],
        'p': ['o', 'l'],
        'q': ['w', 'a'],
        'r': ['e', 'd', 'f', 't'],
        's': ['a', 'w', 'e', 'd', 'x', 'z'],
        't': ['r', 'f', 'g', 'h', 'y'],
        'u': ['y', 'h', 'j', 'k', 'i'],
        'v': ['c', 'f', 'g', 'b'],
        'w': ['q', 'a', 's', 'd', 'e'],
        'x': ['z', 's', 'd', 'c'],
        'y': ['t', 'g', 'h', 'u'],
        'z': ['a', 's', 'x']
    }

    test_word = wrong
    temp_word = test_word
    corrected_words = []

    # Iterate through by indexing letter by letter and check which letter corresponds with which key
    # Iterate through values of key and replace letter with adjacent letters on keyboard.
    for i in range(len(test_word)):
        test_word = temp_word
        for letter in adjKeyboard[temp_word[i]]:
            # sandwich to create new word with replaced value
            test_word = test_word[:i] + letter + test_word[i + 1:]
            if test_word in everyWord:
                corrected_words.append(test_word)
    if len(corrected_words) > 0:
        return corrected_words
    else:
        return ''


adjKeyboard = {
    'a': ['q', 'w', 's', 'x', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['x', 's', 'e', 'r', 'f', 'c'],
    'e': ['w', 's', 'd', 'f', 'r'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['y', 'h', 'b', 'v', 'f', 'r'],
    'h': ['y', 'u', 'j', 'n', 'b', 'g'],
    'j': ['i', 'k', 'm', 'n', 'h', 'u'],
    'k': ['l', 'm', 'j', 'i', 'o'],
    'l': ['n', 'k', 'o', 'p'],
    'm': ['n', 'j', 'k', 'l'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['p', 'l', 'k', 'i'],
    'p': ['o', 'l'],
    'q': ['w', 'a'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    't': ['r', 'f', 'g', 'h', 'y'],
    'u': ['y', 'h', 'j', 'k', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'd', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x']
    }






#print(adjKeyboard[incorrect[0]])
#print(incorrect[:0] + adjKeyboard[incorrect[0]][1] + incorrect[1:])
#print(adjKeyboardTest(incorrect,EnglishDict))


print(doubleLetterTest(incorrect,EnglishDict))