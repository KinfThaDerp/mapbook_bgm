import requests
from bs4 import BeautifulSoup

def userInfo(userData: list) -> None:
    for user in userData:
        if user["alias_name"][-1] == "a":
            print(
                f"Twoja znajoma {user["alias_name"]} z miejscowości {user["location"]} opublikowała {user['posts']} postów.")
        else:
            print(
                f"Twój znajomy {user["alias_name"]} z miejscowości {user["location"]} opublikował {user['posts']} postów.")


def userAppend(userData: list) -> None:
    userData.append({
        "alias_name": str(input("Podaj imię znajomego: ")),
        "location": str(input("Podaj jego miejscowość: ")),
        "posts": int(input("Podaj liczbe jego postów: ")),
        "img_url": str(input("Podaj URL zdjęcia tej osoby: "))})


def userRemove(userData: list) -> None:
    tmp_userBeingRemoved: str = str(input("Podaj imię znajomego do usunięcia: "))
    for user in userData:
        if user["alias_name"] == tmp_userBeingRemoved:
            userData.remove(user)


def userUpdate(userData: list) -> None:
    tmp_userToUpdate = str(input("Jak nazywa sie uzytkownik do zaktualizowania? "))
    for list in userData:
        if list["alias_name"] == tmp_userToUpdate:
            list.update({"alias_name": str(input("Podaj nowe imie: "))})
            list.update({"location": str(input("Podaj nowa lokalizacje: "))})
            list.update({"posts": int(input("Podaj nowa liczbe postow: "))})

def get_Coordinates(city_name:str, )-> list[float]:
    headers = {
        "User-Agent": "<Mozilla 5/0 (Windows NT 10.0; Win64; x64; Trident/7.0)>",
    }
    url:str = f'https://pl.wikipedia.org/wiki/{city_name}'
    response = requests.get(url, headers=headers)
    #print(response.text)
    response_html = BeautifulSoup(response.content, 'html.parser')
    latitude = float((response_html.select('.latitude'))[1].text.replace(',','.'))
    longitude = float((response_html.select('.longitude'))[1].text.replace(',','.'))
    #print(latitude, '\n', longitude)
    return [latitude, longitude]

def get_map(userData: list) -> None:
    import folium
    m = folium.Map(location=(52.23, 21), zoom_start=6)
    import webbrowser

    for user in userData:
        folium.Marker(
            location=get_Coordinates(user['location']),
            tooltip=f"Kliknij mnie!",
            popup=f"<h4>user: {user['alias_name']}</h4> {user['location']}, {user['posts']}, <img class='shrinkToFit' src='{user['img_url']}'/>",
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("index.html")
    webbrowser.open('index.html')

if __name__ == '__main__':
    userData = []
    userAppend(userData)
    userRemove(userData)
    userInfo(userData)

