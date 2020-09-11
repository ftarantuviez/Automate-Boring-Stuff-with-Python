"""
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:
    The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
    unaffected by these events.
    The program would find these occurrences and prompt the user to
    replace them.
    Enter an adjective:
    silly
    Enter a noun:
    chandelier
    Enter a verb:
    screamed
    Enter a noun:
    pickup truck
    The following text file would then be created:
    The silly panda walked to the chandelier and then screamed. A nearby pickup
    truck was unaffected by these events.
    The results should be printed to the screen and saved to a new text file

"""

import os, re



def parse_text(adjective, noun, verb, adverb, fileUser):
    allReplasable = [{'reg': 'ADJECTIVE', 'content': adjective}, {'reg': 'NOUN', 'content': noun}, {'reg': 'VERB', 'content': verb}, {'reg': 'ADVERB', 'content': adverb}]


    if os.path.isfile(fileUser):

        readerFileUser = open(fileUser)
        textFileUser = readerFileUser.read()
        readerFileUser.close()

        writerFileUser = open(fileUser, 'w')

        for regex in allReplasable:
            newRegex = re.compile(regex['reg'])
            match = newRegex.search(textFileUser)
            

            if match != None:
                textFileUser = newRegex.sub(regex['content'], textFileUser)

        writerFileUser.write(textFileUser)
        writerFileUser.close()

    else:
        return 'There is no file in ' + fileUser




if __name__ == '__main__':
    
    adjetive = input('Adjetive: \n')
    noun = input('Noun: \n')
    verb = input('Verb: \n')
    adverb = input('Adverb: \n')

    fileUser = input('Which is the path of your file?')

    parse_text(adjetive, noun, verb, adverb, fileUser)
