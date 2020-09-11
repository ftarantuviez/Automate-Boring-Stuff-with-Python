"""
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free up 
room on your computer, you’ll get the most bang for your buck by deleting
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than
100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.

"""
import os

def find_heavy_files(userSize):
    ans = []

    while True:
        userFolder = input('Put the path where you want search: ')

        if os.path.exists(userFolder):
            
            for foldername, subfoldername, filenames in os.walk(userFolder):

                for filename in filenames:
                    path = os.path.join(foldername, filename)
                    
                    if os.path.getsize(path) > userSize:
                        os.unlink(path)
                        ans.append(path)
                        print(os.path.basename(path) + ' was deleted')

            if len(ans) > 0:
                print('This are the paths deleted \n')
                print('*' * 50 + '\n')
                print('\n'.join(ans))
            else:
                print('No file delted')

            break

        
        else:
            print('Directory not found')



if __name__ == '__main__':
    userSize = int(input('Put the min size to delete: '))
    find_heavy_files(userSize)
