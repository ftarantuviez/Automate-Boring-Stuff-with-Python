"""
Image Site Downloader
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature.

"""
import os, sys, bs4, requests


class Search:

    def __init__(self, category):
        self.category=category
        self.web = input('[F] to search in Flickr: ')

        if self.web.upper() == 'F':
            self._search_flickr()

    def _search_flickr(self):
        URL = 'https://www.flickr.com/search/?text=' + category
        os.makedirs('Flickr')

        # Getting data
        flickr = requests.get(URL)
        flickr.raise_for_status()

        # Parsing to HTML
        html = bs4.BeautifulSoup(flickr.text, features="html.parser")
        images = html.select('.view .photo-list-photo-view')

        # Downloading images

        for image in images:
            style = image.get('style')
            init_image_url = style.find('live.staticflickr.com')
            final_image_url = style.find('jpg')
            
            image_url = 'https://' + style[init_image_url : final_image_url + 3]
            print('Downloading ' + image_url)

            res = requests.get(image_url)
            res.raise_for_status()

            imageFile = open(os.path.join('Flickr', os.path.basename(image_url)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFile.close()
        
        print('Done')




if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        category = ' '.join(sys.argv[1:])
        new_search = Search(category)
    else:
        print('No category insert')




