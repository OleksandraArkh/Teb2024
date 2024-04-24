#Modul 2
print("Modul2 lab\n")
# In your first lab: 1)użyj funkcji print() do wypisania słów "Wlazl kotek na plotek" na ekranie;2)następnie użyj funkcji print() raz jeszcze, lecz tym razem wypisz swoje imię;3)usuń podwójny cudzysłów i uruchom kod. Obserwuj reakcję Pythona. Jaki rodzaj błędu jest wywołany?4)następnie, usuń nawiasy, wprowadź cudzysłów ponownie, i uruchom kod ponownie. jaki rodzaj blędu jest wywołany tym razem?5)eksperymentuj tak dużo jak tylko możesz. Zmień podwójny cudzysłów na pojedyńczy, użyj funkcji print() wielokrotnie w jednej linii, następnie w wielu liniach. Obserwuj, co się stanie.
# first lab 1
print('"Wlazl kotek na plotek"')
print("Oleksandra")
#print(Oleksandra) blad(name 'Oleksandra' is not defined)
#print"Oleksandra" blad(SyntaxError: invalid syntax)
print('Oleksandra')
#print('Oleksandra') wszystko w porzadku
#print("kot")print("pies") blad(SyntaxError: invalid syntax)
# first lab 2
#Zmodyfikuj pierwszą linię kodu wyświetlaną w edytorze, uzywając słów kluczowych sep oraz end, żeby otrzymać oczekiwany wynik. Pamiętaj, użyj dwóch funkcji print(). print("Kurs","Programowania","w") print("Pythonie") Oczekiwany wynik: Kurs***Programowania***w...Pythonie
print("Kurs","Programowania","w",sep="***",end="...")
print("Pythonie")
#first lab 3
# strzałkę
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#zmniejszyć liczbę użytych funkcji print()poprzez wstawianie znaku \n pomiędzy linie tekstu
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
#?stworzyć strzałkę dwa razy większą (zachowując jednak proporcje)
print("    *\n")
print("   * *\n")
print("  *   *\n")
print(" *     *\n")
print("***   ***\n")
print("  *   *\n")
print("  *   *\n")
print("  *****\n")
#print("    *\n    *\n   * *\n   * *\n  *   *\n  *   *\n *     *\n *     *\n***   ***\n***   ***\n  *   *\n  *   *\n  *   *\n  *   *\n  *****\n  *****")
print("       **\n      ****\n     **  **\n    **    **\n   **      **\n  **        **\n **          **\n******    ******\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    **    **\n    ********\n    ********\n")
#zduplikuować strzałkę, i umieścić ją obok pierwszej
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)
#usunąć którykolwiek cudzysłów i patrz na zachowanie Pythona; zwróć uwagę, w którym miejscu Python dostrzega błąd - czy jest to miejsce, w którym faktycznie ten błąd występuje?
# print(Pythonie") - blad: SyntaxError: invalid syntax
#zrobić to samo z nawiasami
# print"Pythonie") - blad: SyntaxError: EOL while scanning string literal
#zmienić którekolwiek słowo print na coś innego, różniącego się tylko wielkością liter (np. Print) - co się stanie teraz?
# Print("Pythonie") - blad: NameError: name 'Print' is not defined
#zamienić niektóre cudzysłowy na apostrofy; zwróć uwagę na to, co się się wydarzy.
print('Kurs',"Programowania","w") # wszystko w porzadku

#second lab modul 2
print()
print("second lab modul 2\n")
#Napisz jedną linijkę kodu, używając funkcji print(), podwójnego cudzysłowu do zapisania łańcucha znaków (""), znaku nowej linii (\n) oraz znaku ucieczki (\), aby uzyskać oczekiwany wynik (trzy linie tekstu). 
# "Ucze sie"
#""jezyka""
#"""Python"""

print('"Ucze sie"', "\"\"jezyka\"\"","\"\"\"Python\"\"\"", sep="\n")

#2.4 lab
print()
print("2.4.1 lab \n")
#Dawno, dawno temu, w Krainie Pomarańczy, Pomarańczowy Król miał trzy pomarańcze, Agnieszka miała pięć pomarańczy, a Adam miał ich sześć. Wszyscy żyli długo i szczęśliwie. Koniec historii.
pomaranczowy_krol=3
agnieszka=5
adam=6
print(pomaranczowy_krol,agnieszka,adam, sep=",")
pomaranczy_razem=agnieszka+adam+pomaranczowy_krol
print(pomaranczy_razem)
print("Całkowita liczba pomarańczy:",pomaranczy_razem)
print()

banany=50
winogrona=150
kiwi=15
truskawki=4000
owoce=banany+winogrona+kiwi+truskawki
print("polowa bananow:",banany/2)
print("owoce w sklepie:",owoce)

#lab 2.4.2
print()
print("2.4.2 lab \n")
#Zakładając, że 1 mila jest równa w przybliżeniu 1.61 kilometra, uzupełnij program w edytorze tak, aby konwertował:
kilometry = 12.25
mile = 7.38

mile_na_kilometry =mile*1.61 # Napisz kod tutaj.
kilometry_na_mile =kilometry/1.61  # Napisz kod tutaj.

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

#lab 2.4.3
print()
print("2.4.3 lab \n")
#3x3 - 2x2 + 3x - 1

x =0  # Tutaj wprowadź swoje dane testowe.
x = float(x)
y=3*(x*x*x)-2*(x*x)+3*x-1# Tutaj napisz swój kod.
print("y =", y) #x=0,y=-1

x =1  # Tutaj wprowadź swoje dane testowe.
x = float(x)
y=3*(x*x*x)-2*(x*x)+3*x-1# Tutaj napisz swój kod.
print("y =", y) #x=1,y=3.0

x =-1  # Tutaj wprowadź swoje dane testowe.
x = float(x)
y=3*(x*x*x)-2*(x*x)+3*x-1# Tutaj napisz swój kod.
print("y =", y) #x=-1,y=-9.0

#2.5 lab komentarzy w Pythonie
print()
print("2.5 lab komentarzy w Pythonie \n")
#Ten program oblicza liczbę sekund w danej liczbie godzin.
#ten program został napisany dwa dni temu

a = 2 #liczba godzin
sekundy = 3600 #liczba sekund w 1 godzinie

print("Godzin: ", a) # wyświetla ilość godzin
print("Sekund w godzinach: ", a * sekundy)  # wyswietla ilość sekund w zadanej liczbie godzin

print("Do widzenia") #tutaj powinniśmy również wyświetlić "Do widzenia", ale programista nie miał już na to czasu
a=3
print("Sekund w 3 godzinach: ", a * sekundy) # to jest koniec programu, który oblicza liczbę sekund w 3 godzinach

#2.6.1 lab
print()
print("2.6.1 lab \n")
a=float(input("Wpisz a "))# tu wprowadź wartość zmiennoprzecinkową dla zmiennej a
b=float(input("Wpisz b "))# tu wprowadź wartość zmiennoprzecinkową dla zmiennej b

print("wynik dodania: ",a+b)# tutaj wypisz wynik dodania
print("wynik odejmowania: ",a-b)# tutaj wypisz wynik odejmowania
print("wynik mnożenia*: ",a*b)# tutaj wypisz wynik mnożenia
print("wynik dzielenia: ",a/b)# tutaj wypisz wynik dzielenia

print("\nI to by było na tyle!")

#2.6.2 lab
print()
print("2.6.2 lab \n")
x = float(input("Wprowadź wartość dla x: "))

y=(1/(x+(1/(x+(1/(x+(1/x)))))))# tutaj wpisz swój kod

print("y =",y)

#2.6.3 lab
print()
print("2.6.2 lab \n")

h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

print(int(((h*60+m+d)/60)%24),":",(h*60+m+d)%60) # wprowadź tutaj swój kod

#Praca domowa
print()
print("Praca domowa\n")
#Stwórz program, dzięki któremu użytkownik przekonwertuje odległość podaną w kilometrach na podane jednostki: milimetry, centrymentry, metry, cale, stopy, mile.

print("Prosze napisac ile kilometrow\n chcesz przekonwertowac w:\n metry, centymetry, milimetry,\n cale, stopy, mile")

km=input()

mm = int(km)*1000000
cm = int(km)*100000
m = int(km)*1000
cale= int(km)*39370.1
stopy= int(m)*3.2808
mile = int(km)*0,6214

print(f"W kilometrach {km}")
print(f"W metrach {m}")
print(f"W centymetrach {cm}")
print(f"W milimetrach {mm}")
print(f"W cale {cale}")
print(f"W stopy {stopy}")
print(f"W mile {mile}\n")

print(f"{km} kilometry = {m} metry\n             = {cm} centymetry\n             = {mm} milimetry\n             = {cale} cale\n             = {stopy} stopy\n             = {mile} mile")

