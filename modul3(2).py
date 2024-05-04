#Modul 3 czesc 2 (3.4,3.6,3.7)
#lab 1
print()
print("3.4.1.6 LABORATORIUM: Listy - podstawy")
liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.
print(liczby_z_kapelusza)
a=int(input("Wpisz ktory numer chcesz zmienic: "))# Krok 1: Napisz wiersz kodu, który prosi użytkownika
b=a-1# o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
c=int(input("Na jaki numer chcesz zmienic? "))
liczby_z_kapelusza[b]=c
print("Teraz liczba wyglanda tak: ",liczby_z_kapelusza)
n=len(liczby_z_kapelusza)-1
del liczby_z_kapelusza[n]# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
print("Teraz liczba, bez ostatniego elementa wyglanda tak: ",liczby_z_kapelusza)
print("Długość istniejącej listy= ",len(liczby_z_kapelusza))# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.
print("koniec")
print()
print("3.4.1.13 LABORATORIUM: Podstawy list - The Beatles")
beatles=[] # Krok 1
print("Krok 1:", beatles)

beatles.append('John Lennon')# Krok 2
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Krok 2:", beatles)

for i in range (1):
    beatles.append('Stu Sutcliffe')# Krok 3
for i in range (1):
    beatles.append('Pete Best')
print("Krok 3:", beatles)

c=len(beatles)-1
del beatles[c]# Krok 4
del beatles[c-1]
print("Krok 4:", beatles)

beatles.insert(0,'Ringo Starr')# Krok 5
print("Krok 5:", beatles)

# Sprawdzanie długości listy.
print("The Fab", len(beatles))
print("koniec")
print()
print("3.6.1.9 LABORATORIUM: Operacje na listach - podstawy")
print()
print("Lista źródłowa")
moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
znaleziono = False
for i in range(len(moja_lista)-1):
    for j in range(len(moja_lista)):
        znaleziono = moja_lista[j] == moja_lista[i+1]
        if znaleziono and j!=i+1:
            moja_lista[i+1]=0
pusta=[]
for f in range(len(moja_lista)):
    if moja_lista[f]!=0:
       pusta.append(moja_lista[f])
print("Lista tylko z unikalnymi elementami:")
print(pusta)
print()
