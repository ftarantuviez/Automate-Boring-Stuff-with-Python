"""
“I’m Feeling Lucky” Google Search
Whenever I search a topic on Google, I don’t look at just one search result
at a time. By middle-clicking a search result link (or clicking while holding ctrl), I open the first several links in a bunch of new tabs to read later.
I search Google often enough that this workflow—opening my browser,
searching for a topic, and middle-clicking several links one by one—is
tedious. It would be nice if I could simply type a search term on the command line and have my computer automatically open a browser with all
the top search results in new tabs. Let’s write a script to do this.
This is what your program does:
    •    Gets search keywords from the command line arguments.
    •    Retrieves the search results page.
    •    Opens a browser tab for each result.
    This means your code will need to do the following:
    •    Read the command line arguments from sys.argv.
    •    Fetch the search result page with the requests module.
    •    Find the links to each search result.
    •    Call the webbrowser.open() function to open the web browser.

"""
import sys, os, webbrowser, requests, bs4

def google_search(search_parameters):

    print('Googling...') # display text while downloading the Google page

    res = requests.get('http://google.com/search?q=' + ' '.join(search_parameters))
    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Open a browser tab for each result.
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))
    print(numOpen, linkElems)
    for i in range(numOpen):
         webbrowser.open('http://google.com' + linkElems[i].get('href'))


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        google_search(sys.argv[1:])
    else:
        print('No parameters founds')

