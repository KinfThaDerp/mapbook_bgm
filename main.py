zmienna_1:str = "Bassam"
zmienna_2:str = "Michasia"
zmienna_3:str = "Kasia"
zmienna_4:str = "Asia"
# Przygotuj liste slowników które będą przechowywały informacje o użytkownikach na temat:
# Imie(alias name), Miejscowość (location), Liczba postów(posts),
users:list=[
    {"alias_name":zmienna_1, "location":"Warszawa", "posts":10},
    {"alias_name":zmienna_2, "location":"Radom", "posts":20},
    {"alias_name":zmienna_3, "location":"Legionowo", "posts":30},
    {"alias_name":zmienna_4, "location":"Milanówek", "posts":40}
]

for user in users:
    print(f"Twój znajomy {user["alias_name"]} z miejscowości {user["location"]} opublikował {user['posts']} postów.")