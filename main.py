# Przygotuj liste slowników które będą przechowywały informacje o użytkownikach na temat:
# Imie(alias name), Miejscowość (location), Liczba postów(posts),
from asyncio import wait_for

from bs4 import BeautifulSoup

users: list = [
    {"alias_name": "Bassam", "location": "Warszawa", "posts": 10, "img_url": ''},
    {"alias_name": "Michasia", "location": "Radom", "posts": 20, "img_url": ''},
    {"alias_name": "Kasia", "location": "Legionowo", "posts": 30, "img_url": ''},
    {"alias_name": "Asia", "location": "Milanówek", "posts": 40, "img_url": ''}
]


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
    import requests
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


while True:
    print('==============================MENU==============================')
    print("0. Wyjście z programu")
    print("1. Wyświetlanie znajomych")
    print("2. Dodawanie znajomego")
    print("3. Usuwanie znajomego")
    print("4. Aktualizacja znajomego")
    print("5. Wyświetl mapę znajomych")
    tmp_choice: int = int(input("Wybierz opcje menu: "))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print("Wybrano funkcję wyświetlania aktywności znajomych")
        userInfo(users)
    if tmp_choice == 2:
        print("Wybrano funkcje dodawania znajomych")
        userAppend(users)
    if tmp_choice == 3:
        print("Wybrano funkcje usuwania znajomych")
        userRemove(users)
    if tmp_choice == 4:
        print("Wybrano funkcje aktualizowania znajoymch")
        userUpdate(users)
    if tmp_choice == 5:
        print("Wybrano funkcję wyświetlania mapy użytkowników")
        get_map(users)
    print('================================================================')