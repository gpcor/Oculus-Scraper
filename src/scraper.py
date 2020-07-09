import requests
import subprocess
from time import sleep


class Oculus_Scraper():

    def __init__(self, url):
        self.url = url
        self.available_text = "Notify Me"
        self.audio_file = 'resources/Small_Item_Catch.mp3'

    def availability(self):
        self.rift_page = requests.get(url)
        self.rift_page_text = requests.get(url).text
        return(self.rift_page.status_code)

    def get_item(self):
        # print("Available"), subprocess.call(["afplay", self.audio_file]) if self.available_text not in self.rift_page_text else print("Unavailable!")
        print('Unavailable') if self.available_text in self.rift_page_text else print("Available") & subprocess.call(["afplay", self.audio_file])


url = 'https://www.oculus.com/rift-s/'
scraper = Oculus_Scraper(url)

while True:
    status = scraper.availability()
    if status == 200:
        print('page is up')
        scraper.get_item()
        sleep(10)
    else:
        print('Site returned code: ' + str(status.status_code))
