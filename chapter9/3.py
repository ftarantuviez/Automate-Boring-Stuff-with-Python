"""
Filling in the Gaps
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.

"""
import os, shutil


def find_with_prefix(pathFolder, prefix):
    
    allFiles = os.listdir(pathFolder)
    ans = []

    for filename in allFiles:
        perh_prefix = filename[:len(prefix)]
        
        if perh_prefix == prefix:
            ans.append(os.path.join(os.path.abspath(pathFolder), filename))

    if len(ans) > 0:
        ans.sort()
        answerFolder = os.path.join(pathFolder, 'Answer')
        os.makedirs(answerFolder)
        index = 1

        zeros = int(input('How many zeros before do you want: '))
        

        for filepath in ans:
            number = str(index).rjust(zeros, '0')
            basename = os.path.basename(filepath)
            extension = basename[basename.index('.') :]

            rename = prefix + number + extension
            shutil.move(filepath, os.path.join(answerFolder, rename))

            index += 1
            

    else:
        print('No files with the prefix ' + prefix)
    


def add_with_prefix(pathFolder, prefix):
    
    position = int(input('In which position do you wanna add this file: '))
    allFiles = os.listdir(pathFolder)

    if position > len(allFiles) or position <= 0:
        print(f'Position out of range, you can add in the range of (1 - {len(allFiles) + 1})')
        return add_with_prefix(pathFolder, prefix)
    
    else:
        absPath = os.path.abspath(pathFolder)
        for i in range(position - 1, len(allFiles)):

            edit_file_extension = allFiles[i][allFiles[i].index('.') : ]
            editFile = prefix + str(i + 2).rjust(3, '0') + edit_file_extension
            shutil.move(os.path.join(absPath, allFiles[i]), os.path.join(absPath, editFile)) 

 
        extension = input('Which kind of file is? (Extension): ')
        text = input('Would you like write something in the file? (Y/n): ') 
        newFile = prefix + str(position).rjust(3, '0') + '.' + extension

        if text.upper() == 'Y':
            text = input(f'Write what you wanna write in {newFile}')
            writer = open(os.path.join(absPath, newFile), 'w')
            writer.write(text)
            writer.close()
        else:
            createFile = open(os.path.join(absPath, newFile), 'w')
            createFile.close()


if __name__ == '__main__':
    
    userFolder = ''
    while True:
        userFolder = input('Put the path of the folder: ')

        if os.path.exists(userFolder):
            break
        else:
            print('Path not found')
            continue

    isFinding = input('[F] to find, [A] to add: ')
    prefix = input('Which is the prefix that you wanna search: ')

    if isFinding.upper() == 'F':
        find_with_prefix(userFolder, prefix)

    elif isFinding.upper() == 'A':

        add_with_prefix(userFolder, prefix)
    else:
        print('no commmand')


