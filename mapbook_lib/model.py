


class User:
    def __init__(self, name:str, location:str, posts:int, img_url:str, map_widget):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_Coordinates()
        print(self.coords)
        self.marker = map_widget.set_position(self.coords[0], self.coords[1], text=self.name, image_zoom_visibility=(0,float('inf') ))

    def get_Coordinates(self):
        import requests
        from bs4 import BeautifulSoup
        headers = {
            "User-Agent": "<Mozilla 5/0 (Windows NT 10.0; Win64; x64; Trident/7.0)>",
        }
        url:str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url, headers=headers)
        #print(response.text)
        response_html = BeautifulSoup(response.content, 'html.parser')
        latitude = float((response_html.select('.latitude'))[1].text.replace(',','.'))
        longitude = float((response_html.select('.longitude'))[1].text.replace(',','.'))
        return [latitude, longitude]