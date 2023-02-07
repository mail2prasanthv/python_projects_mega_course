# Saving image
import requests

import requests
response = requests.get('https://imgs.xkcd.com/comics/making_progress.png')

with open('image5.png','wb') as file:#wb-writing in binary mode
    file.write(response.content)


