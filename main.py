from mapbook_lib.controller import userInfo, userAppend, userRemove, userUpdate, get_map
from mapbook_lib.model import users
from tkinter import *
import tkintermapview

# zmienna_na_licznik = 0
# def updateLicznik():
#     global zmienna_na_licznik
#     zmienna_na_licznik += 1
#     napis.config(text=str(zmienna_na_licznik))
#     return

users: list = []

class User:
    def __init__(self, name:str, location:str, posts:int, img_url:str):
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

def add_user(userData: list) -> None:
    userData.append(User(
        name=str(entry_name.get()),
        location=str(entry_location.get()),
        posts=int(entry_posty.get()),
        img_url=str(entry_img_url.get()),
        ))
    user_info(userData)
    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_posty.delete(0, END)
    entry_img_url.delete(0, END)
    entry_name.focus()


def user_info(userData: list) -> None:
    list_box.delete(0, END)
    for idx, user in enumerate(userData):
        list_box.insert(idx, f"{user.name} {user.location} {user.posts} postów")


def delete_user(userData: list) -> None:
    i = list_box.index(ACTIVE)
    userData[i].marker.delete()
    userData.pop(i)
    user_info(userData)
    print(i)

def user_details(userData: list) -> None:
    i = list_box.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=f"{userData[i].name}")
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=f"{userData[i].location}")
    label_posty_szczegoly_obiektu_wartosc.config(text=f"{userData[i].posts}")
    map_widget.set_position(userData[i].coords[0], userData[i].coords[1])
    map_widget.set_zoom(15)


def edit_user(userData: list) -> None:
    i = list_box.index(ACTIVE)
    entry_name.insert(0, userData[i].name)
    entry_location.insert(0, userData[i].location)
    entry_posty.insert(0, userData[i].posts)
    entry_img_url.insert(0, userData[i].img_url)

    button_dodaj_obiekt.config(text="Zapisz edycje", command=lambda: update_user(userData, i))


def update_user(userData: list, i: int) -> None:
    userData[i].name = str(entry_name.get())
    userData[i].location = str(entry_location.get())
    userData[i].posts = int(entry_posty.get())
    userData[i].img_url = str(entry_img_url.get())

    userData[i].coords = userData[i].get_Coordinates()
    userData[i].marker.set_position(userData[i].coords[0], userData[i].coords[1], userData[i].name)

    user_info(userData)

    button_dodaj_obiekt.config(text="Dodaj obiekt", command=lambda: add_user(users))

    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_posty.delete(0, END)
    entry_img_url.delete(0, END)
    entry_name.focus()


root = Tk()
root.title("mapbook_bgm")
root.geometry("1025x1060")


ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0)

# RAMKA LISTA OBIEKTÓW
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista Obiektów")
label_lista_obiektow.grid(row=0,column=0, columnspan=3)

list_box = Listbox(ramka_lista_obiektow, width=30, height=10)
list_box.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow,text="Pokaz Szczegoly",command=lambda: user_details(users))
button_pokaz_szczegoly.grid(row=2,column=0)

button_usun_obiekt = Button(ramka_lista_obiektow,text="Usuń Obiekt",command=lambda: delete_user(users))
button_usun_obiekt.grid(row=2,column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow,text="Edytuj Obiekt",command=lambda: edit_user(users))
button_edytuj_obiekt.grid(row=2,column=2)



# RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0,column=0, columnspan=2)

label_imie = Label(ramka_formularz, text="Imie: ")
label_imie.grid(row=1,column=0, sticky=W)


label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")
label_lokalizacja.grid(row=2,column=0, sticky=W)


label_posty = Label(ramka_formularz, text="Posty: ")
label_posty.grid(row=3,column=0, sticky=W)


label_img_url = Label(ramka_formularz, text="Obrazek: ")
label_img_url.grid(row=4,column=0, sticky=W)


entry_name = Entry(ramka_formularz)
entry_name.grid(row=1,column=2)

entry_location = Entry(ramka_formularz)
entry_location.grid(row=2,column=2)

entry_posty = Entry(ramka_formularz)
entry_posty.grid(row=3,column=2)

entry_img_url = Entry(ramka_formularz)
entry_img_url.grid(row=4,column=2)

button_dodaj_obiekt = Button(ramka_formularz, text="Dodaj obiekt", command=lambda: add_user(users))
button_dodaj_obiekt.grid(row=5,column=0,columnspan=3)



# RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoly_obiektow = Label(ramka_szczegoly_obiektu, text="Szczegoly obiektu: ")
label_szczegoly_obiektow.grid(row=0,column=0, sticky=W)

label_imie_szczegolu_obiektu = Label(ramka_szczegoly_obiektu, text="Imie: ")
label_imie_szczegolu_obiektu.grid(row=1,column=0, sticky=W)

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_imie_szczegoly_obiektu_wartosc.grid(row=1,column=1 )

label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja obiektu: ")
label_lokalizacja_szczegoly_obiektu.grid(row=2,column=0, sticky=W)

label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=2,column=1)

label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Posty obiektu: ")
label_posty_szczegoly_obiektu.grid(row=3,column=0, sticky=W)

label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_posty_szczegoly_obiektu_wartosc.grid(row=3,column=1)


#RAMKA MAPY
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1025, height=600, corner_radius=0)
map_widget.set_position(52.0,21.0)
map_widget.set_zoom(6)
map_widget.grid(row=0,column=0)


# guzik = Button(root,text="Kliknij mnie",command=lambda: updateLicznik())
# guzik.grid(column=0,row=0)
# root.bind("<Control-Button-1>",updateLicznik())


# napis = Label(root,text=f"{zmienna_na_licznik}")
# napis.grid(column=1,row=0)

root.mainloop()
