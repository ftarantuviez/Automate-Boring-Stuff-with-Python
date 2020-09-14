"""
Link Verification
Write a program that, given the URL of a web page, will attempt to download every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.

"""

import os, sys, requests, bs4

def download_links(URL):
    
    # Fetching data
    main_page = requests.get(URL)
    main_page.raise_for_status()

    # Parsing to HTML
    html = bs4.BeautifulSoup(main_page.text, features="html.parser")
    links = html.select('a')

    for link in links:
        link_url = link.get('href')

        res = requests.get(link_url)
        if res.status_code == requests.codes.not_found:
            print('404 Not found ' + link_url)
        res.raise_for_status()


        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        print(os.path.basename(link_url))



if __name__ == '__main__':

    if len(sys.argv) > 1:
        URL = sys.argv[1]

        download_links(URL)

    else:
        print('No url recived')
