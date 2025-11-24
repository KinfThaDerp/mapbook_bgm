import requests
from bs4 import BeautifulSoup
from mapbook_lib.model import User
from tkinter import *

def add_user(userData: list, entry_name, entry_location, entry_posty, entry_img_url, map_widget, list_box) -> None:
    userData.append(User(
        name=str(entry_name.get()),
        location=str(entry_location.get()),
        posts=int(entry_posty.get()),
        img_url=str(entry_img_url.get()),
        map_widget=map_widget
    ))
    user_info(userData, list_box)
    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_posty.delete(0, END)
    entry_img_url.delete(0, END)
    entry_name.focus()

def user_info(userData: list, list_box) -> None:
    list_box.delete(0, END)
    for idx, user in enumerate(userData):
        list_box.insert(idx, f"{user.name} {user.location} {user.posts} postów")

def delete_user(userData: list, list_box) -> None:
    i = list_box.index(ACTIVE)
    temp_user = userData[i]

    if isinstance(temp_user, User):
        # Proceed with marker deletion if it's a User object
        temp_user.marker.delete()
        userData.pop(i)
        user_info(userData, list_box)
        print(f"Deleted user at index {i}")
    else:
        # This will print if there's something other than a User object in userData
        print(f"Error: Expected User object but got {type(temp_user)}")

def user_details(userData: list, list_box, label_imie_szczegoly_obiektu_wartosc, label_lokalizacja_szczegoly_obiektu_wartosc, label_posty_szczegoly_obiektu_wartosc, map_widget) -> None:
    i = list_box.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=f"{userData[i].name}")
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=f"{userData[i].location}")
    label_posty_szczegoly_obiektu_wartosc.config(text=f"{userData[i].posts}")
    map_widget.set_position(userData[i].coords[0], userData[i].coords[1])
    map_widget.set_zoom(15)

def edit_user(userData: list, entry_name, entry_location, entry_posty, entry_img_url, button_dodaj_obiekt, list_box) -> None:
    # Set a flag or keep track of the user being edited
    i = list_box.index(ACTIVE)
    # Populate the form fields with the existing user's data
    entry_name.insert(0, userData[i].name)
    entry_location.insert(0, userData[i].location)
    entry_posty.insert(0, userData[i].posts)
    entry_img_url.insert(0, userData[i].img_url)

    # Change the button to "Save Changes"
    button_dodaj_obiekt.config(
        text="Zapisz edycje",
        command=lambda: update_user(userData, i, entry_name, entry_location, entry_posty, entry_img_url, button_dodaj_obiekt, list_box)
    )
def update_user(userData: list, i: int, entry_name, entry_location, entry_posty, entry_img_url, button_dodaj_obiekt, list_box) -> None:
    # Update user data from the form
    userData[i].name = str(entry_name.get())
    userData[i].location = str(entry_location.get())
    userData[i].posts = int(entry_posty.get())
    userData[i].img_url = str(entry_img_url.get())

    # Update coordinates and marker
    userData[i].coords = userData[i].get_Coordinates()
    userData[i].marker.set_position(userData[i].coords[0], userData[i].coords[1], userData[i].name)

    # Refresh the list of users
    user_info(userData, list_box)

    # Change the button back to "Add User"
    button_dodaj_obiekt.config(
        text="Dodaj obiekt",
        command=lambda: add_user(users, entry_name, entry_location, entry_posty, entry_img_url, map_widget, list_box)
    )

    # Clear the form fields
    entry_name.delete(0, END)
    entry_location.delete(0, END)
    entry_posty.delete(0, END)
    entry_img_url.delete(0, END)
    entry_name.focus()
