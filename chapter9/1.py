"""
Selective Copy
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.

"""
import os, re, shutil


def selective_copy():
    
    ans = []

    while True:
        userFolder = input('Put the path of your folder: \n')
        newUserFolder = input('How will call you the new folder: ')

        if os.path.isdir(userFolder):
            folder = os.path.join(userFolder, newUserFolder)
            os.makedirs(folder)

            print(f'FOLDER TO SAVE = {folder}')

            for folders, subfolders, filenames in os.walk(userFolder):
                for filename in filenames:
                    if validationPdf(filename) or validationJpg(filename):
                        ans.append(os.path.join(folders, filename))


            for path in ans:
                shutil.copy(path, folder)    
    
            break
        else:
            print('BRO, you have to put a valid path')
            continue

    return ans


def validationPdf(filename):
    if filename[-1] == 'f' and filename[-2] == 'd' and filename[-4] == '.':
        return True
    else:
        return False

def validationJpg(filename):
    if filename[-1] == 'g' and filename[-2] == 'p' and filename[-4] == '.':
        return True
    else:
        return False


if __name__ == '__main__':
    print(selective_copy())
