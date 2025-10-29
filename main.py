zmienna_1: str = "Bassam"
zmienna_2: str = "Michasia"
zmienna_3: str = "Kasia"
zmienna_4: str = "Asia"
# Przygotuj liste slowników które będą przechowywały informacje o użytkownikach na temat:
# Imie(alias name), Miejscowość (location), Liczba postów(posts),
users: list = [
    {"alias_name": zmienna_1, "location": "Warszawa", "posts": 10},
    {"alias_name": zmienna_2, "location": "Radom", "posts": 20},
    {"alias_name": zmienna_3, "location": "Legionowo", "posts": 30},
    {"alias_name": zmienna_4, "location": "Milanówek", "posts": 40}
]


def userInfo(nestledDict: list) -> None:
    for user in nestledDict:
        if user["alias_name"][-1] == "a":
            print(
                f"Twoja znajoma {user["alias_name"]} z miejscowości {user["location"]} opublikowała {user['posts']} postów.")
        else:
            print(
                f"Twój znajomy {user["alias_name"]} z miejscowości {user["location"]} opublikował {user['posts']} postów.")


def userAppend(nestledDict: list) -> None:
    nestledDict.append({
        "alias_name": str(input("Podaj imię znajomego: ")),
        "location": str(input("Podaj jego miejscowość: ")),
        "posts": int(input("Podaj liczbe jego postów: "))})


def userRemove(nestledDict: list) -> None:
    tmp_userBeingRemoved: str = str(input("Podaj imię znajomego do usunięcia: "))
    for user in nestledDict:
        if user["alias_name"] == tmp_userBeingRemoved:
            nestledDict.remove(user)


# def userUpdate(nestledDict: list) -> None:
#     tmp_userToUpdate = str(input("Jak nazywa sie uzytkownik do zaktualizowania? "))
#     for list in nestledDict:
#         if list["alias_name"] == tmp_userToUpdate:
#             list.update({"alias_name": str(input("Podaj nowe imie: "))})
#             list.update({"location": str(input("Podaj nowa lokalizacje: "))})
#             list.update({"posts": int(input("Podaj nowa liczbe postow: "))})


while True:
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
        # userUpdate(users)
