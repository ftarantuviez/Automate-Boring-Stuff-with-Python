"""
Blogs and other regularly updating websites usually have a front page with
the most recent post as well as a Previous button on the page that takes you
to the previous post. Then that post will also have a Previous button, and so
on, creating a trail from the most recent page to the first post on the site.
If you wanted a copy of the site’s content to read when you’re not online,
you could manually navigate over every page and save each one. But this is
pretty boring work, so let’s write a program to do it instead.
XKCD is a popular geek webcomic with a website that fits this structure
(see Figure 11-6). The front page at http://xkcd.com/ has a Prev button that
guides the user back through prior comics. Downloading each comic by
hand would take forever, but you can write a script to do this in a couple of
minutes.

Here’s what your program does:
    •    Loads the XKCD home page.
    •    Saves the comic image on that page.
    •    Follows the Previous Comic link.
    •    Repeats until it reaches the first comic.

This means your code will need to do the following:
    •    Download pages with the requests module.
    •    Find the URL of the comic image for a page using Beautiful Soup.
    •    Download and save the comic image to the hard drive with iter_content().
    •    Find the URL of the Previous Comic link, and repeat

"""
import requests, os, bs4

def download_comics():
    
    url = 'http://xkcd.com' # starting url
    os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

    
    while not url.endswith('#'):
        
        # Download the page
        print('Downloading page %s...' % url)

        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')

            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

    
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFile.close()
             
                # Get the Prev button's url.
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prevLink.get('href')

    print('Done.')



if __name__ == '__main__':

    download_comics()
