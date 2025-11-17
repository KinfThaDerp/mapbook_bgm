import requests
from bs4 import BeautifulSoup

class User:
    def __init__(self, name:str, location:str, posts:int, img_url:str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_Coordinates()

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
        #print(latitude, '\n', longitude)
        return [latitude, longitude]


def userInfo(userData: list) -> None:
    for user in userData:
        if user.name[-1] == "a":
            print(
                f"Twoja znajoma {user.name} z miejscowości {user.location} opublikowała {user.posts} postów.")
        else:
            print(
                f"Twój znajomy {user.name} z miejscowości {user.location} opublikował {user.posts} postów.")


def userAppend(userData: list) -> None:
    userData.append(User(
        name=str(input("Podaj imię znajomego: ")),
        location=str(input("Podaj jego miejscowość: ")),
        posts = int(input("Podaj liczbe jego postów: ")),
        img_url=str(input("Podaj URL zdjęcia tej osoby: "))
        ))

def userRemove(userData: list) -> None:
    tmp_userBeingRemoved: str = str(input("Podaj imię znajomego do usunięcia: "))
    for user in userData:
        if user.name == tmp_userBeingRemoved:
            userData.remove(user)


def userUpdate(userData: list) -> None:
    tmp_userToUpdate = str(input("Jak nazywa sie uzytkownik do zaktualizowania? "))
    for user in userData:
        if user.name == tmp_userToUpdate:
            user.name = str(input("Podaj nowe imie: "))
            user.location = str(input("Podaj nowa lokalizacje: "))
            user.posts = int(input("Podaj nowa liczbe postow: "))
            user.coords = user.get_Coordinates()



def get_map(userData: list) -> None:
    import folium
    m = folium.Map(location=(52.23, 21), zoom_start=6)
    import webbrowser

    for user in userData:
        folium.Marker(
            location= user.coords,
            tooltip=f"Kliknij mnie!",
            popup=f"<h4>user: {user.name}</h4> {user.location}, {user.posts}, <img class='shrinkToFit' src='{user.img_url}/>",
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("index.html")
    webbrowser.open('index.html')

if __name__ == '__main__':
    userData = []
    userAppend(userData)
    userRemove(userData)
    userInfo(userData)

