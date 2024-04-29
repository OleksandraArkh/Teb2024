# 1 - Dodaj, 2 - Edytuj, 3 - Usuń, 4 - Wyświetl, 5 - Zakończ
lista_pracownikow = []

while True:
    print("1-Dodaj")
    print("2-Edytuj")
    print("3-Usuń")
    print("4-Wyświetl")
    print("5-Zakończ")
    wybor = input("Wybierz: ")
    if wybor not in ['1', '2', '3', '4', '5']:
        print('Invalid value. try again [1-5]')

    if wybor == '1':
        pracownik = dict()
        pracownik["imie"] = input("Podaj imię: ")
        pracownik["nazwisko"] = input("Podaj nazwisko: ")
        pracownik["stanowisko"] = input("Podaj stanowisko: ")
        pracownik["pensja"] = input("Podaj pensja: ")
        pracownik["data_zatrudnienia"] = input("Podaj datę zatrudnienia: ")
        lista_pracownikow.append(pracownik)
        if input("Chcesz zrobic wiecej?(napisz Tak albo Nie): ") == "Nie":
            break
    if wybor == '2':
        wybor2 = input("Co chcesz zmienic: imie, nazwisko, stanowisko, pensija, data_zatrudnienia?: ")
        if wybor2 == "imie":
            pracownik["imie"] = input("Wpisz imie")
        if wybor2 == "nazwisko":
            pracownik["nazwisko"] = input("Wpisz nazwisko")
        if wybor2 == "stanowisko":
            pracownik["stanowisko"] = input("Wpisz stanowisko")
        if wybor2 == "pensija":
            pracownik["pensja"] = input("pensija")
        if wybor2 == "data_zatrudnienia":
            pracownik["data_zatrudnienia"] = input("Wpisz data_zatrudnienia")
            if input("Chcesz zrobic wiecej?(napisz Tak albo Nie): ") == "Nie":
                break
    if wybor == '3':
        print("# | Imie  |  Nazwisko")
        for index, pracownik in enumerate(lista_pracownikow):
            print(f"{index+1} | {pracownik['imie']}  |  {pracownik['nazwisko']}")
        wybor3 = input("Kogo chcesz usunac: ?: ")
        if not wybor3.isdigit() or int(wybor3) > len(lista_pracownikow):
            print(f"Invalid value. try again [1-{len(lista_pracownikow)}]")
        del lista_pracownikow[int(wybor3)-1]

        if input("Chcesz zrobic wiecej?(napisz Tak albo Nie): ") == "Nie":
            break
    if wybor == '4':
        print("#\t|\tImie\t|\tNazwisko\t|\tStanowisko\t|\tpensja\t|\tdata_zatrudnienia")
        for index, pracownik in enumerate(lista_pracownikow):
            print(f"{index + 1}\t|\t{pracownik['imie']}\t|\t{pracownik['nazwisko']}\t|\t{pracownik['stanowisko']}\t|\t{pracownik['pensja']}\t|\t{pracownik['data_zatrudnienia']}")
        if input("Chcesz zrobic wiecej?(napisz Tak albo Nie): ") == "Nie":
            break

    if wybor == '5':
        print("Koniec")
        break
