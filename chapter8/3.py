"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen. 

"""
import os, re, sys

def regex_search(folder, regExpression):
    allFiles = show_files(folder)
    regUser = re.compile(regExpression)           

    match = regUser.findall(allFiles)
    
    if len(match) > 0:
        print(match)
    else:
        print('No file match with the expression regular ' + regExpression) 
        

    


def show_files(folder):
    try:
        allFiles = os.listdir(folder)
        ans = ''

        for i in allFiles:
            if i[-1] == 't' and i[-2] == 'x' and i[-3] == 't':
                ans += i + '  |  '
                
        return ans

    except FileNotFoundError:
        print('Dir not found')
        sys.exit()
        return



if __name__ == '__main__':
    
    userFolder = input('Put the path of the folder where you wanna search: ')
    print(show_files(userFolder))

    regExpression = input('Regex:')
    print(regex_search(userFolder, regExpression))


