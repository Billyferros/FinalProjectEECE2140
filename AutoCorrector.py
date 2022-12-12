from implementCorrection import textCorrector, DisplayTextFile


# prompts user to enter for their file name
user_file = input("Please enter the name of the file you wish to autocorrect: ")

autocorrect = True
while autocorrect:
    try:
        print("The original text is: ")

        # display text with no corrections
        correction_file = textCorrector(user_file)
        #create object

        file = DisplayTextFile(user_file)
        DisplayTextFile.showFile(file)

        # use spell checker to offer correction suggestions to user
        textCorrector.find_incorrect_words(correction_file)
        autocorrect = False

    #if file does not exist, prompt user to try another file name
    except FileNotFoundError:
        print("File not found")
        user_file = input("Please enter the name of the file you wish to autocorrect: ")

print('Your file has now been corrected!')


