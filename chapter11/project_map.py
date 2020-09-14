"""
This is what your program does:
    •    Gets a street address from the command line arguments or clipboard.
    •    Opens the web browser to the Google Maps page for the address.
   
   This means your code will need to do the following:
        •    Read the command line arguments from sys.argv.
        •    Read the clipboard contents.
        •    Call the webbrowser.open() function to open the web browser.
        Open a new file editor window and save it as mapIt.py

"""

import webbrowser, sys, pyperclip


def search_google_maps(address):
    URL = 'https://www.google.com/maps/place/'
    print('opening...')
    webbrowser.open(URL + address)
    print('opened successfully ' + address)


if __name__ == '__main__':
    address = ''

    if len(sys.argv) > 1:    
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = pyperclip.paste()

    search_google_maps(address)

