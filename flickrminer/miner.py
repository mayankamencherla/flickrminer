import os
import flickrapi
import urllib
import time
from PIL import Image

class Miner:
    def __init__(self, key_id, key_secret):
        self.key_id = key_id
        self.key_secret = key_secret

    # This method takes in a tag, mines flickr and saves all the images in a folder
    def mine(self, tag):
        flickr = flickrapi.FlickrAPI(self.key_id, self.key_secret, cache=True)

        # Get path based on tag
        path = '{}/{}'.format(os.getcwd(), tag)

        # Make tag's directory based with full R / W permissions
        if not os.path.exists(path):
            os.mkdir(path, 0o777)

        # Mine the tag's images
        photos = flickr.walk(
            text = tag,
            tag_mode = 'all',
            tags = tag,
            extras = 'url_c',
            sort = 'relevance',
            per_page = 100
        )

        # Calling helper method to save photos
        self.save_tag_photos(path, photos)

    def save_tag_photos(self, path, photos)
        # Save each image in the respective directory
        for photo in photos:
            try:
                url = photo.get('url_c')

                # Name of the jpg will be the current timestamp
                ts = int(time.time())
                name = "{}/{}.jpg".format(path, ts)
                
                # Retrieving image from the url
                urllib.request.urlretrieve(url, name)

                # Resizing the image
                img = Image.open(name)
                img = img.resize((180, 180), Image.ANTIALIAS)
                img.save(name)

            except Exception as e:
                pass