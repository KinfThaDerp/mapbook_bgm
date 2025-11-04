from mapbook_lib.controller import userInfo, userAppend, userRemove, userUpdate, get_map
from mapbook_lib.model import users

def main():
    while True:
        print('==============================MENU==============================')
        print("0. Wyjście z programu")
        print("1. Wyświetlanie znajomych")
        print("2. Dodawanie znajomego")
        print("3. Usuwanie znajomego")
        print("4. Aktualizacja znajomego")
        print("5. Wyświetl mapę znajomych")
        print('================================================================')
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

if __name__ == '__main__':
    main()