#Modul3.1
print("Modul 3.1 Operatory porownania i wykonanie warunkowe")
#lab 1
print()
print("Lab 1  Pytania i odpowiedzi")
n=int(input("wpisz n " ))
print(100<=n)
#lab 2
print()
print("Lab 2 : Operatory i Warunki")
k = str(input("Wpisz rosline: "))
if k==str("Skrzydłokwiat"):
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")
else:
        print("Nie, ja chcę Skrzydłokwiat...!")
        k = str(input("Wpisz rosline: "))
#lab 3
print()
print("Lab 3  Niezbędne elementy instrukcji if-else")
print()
dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod<=85528:
    podatek=dochod*0.18-556.2
else: podatek=14839.2+(dochod-85528)*0.32
if podatek<0:
    podatek=0.0

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
#lab 4
print()
print("Lab 4  Niezbędne elementy instrukcji if-else")
print()
rok = int(input("Wprowadź rok: "))

if rok<1582:
    print("Rok nie jest w kalendarzu gregorianskim")
elif rok%4!=0:
    print("Rok jest zwykly")
elif rok%100!=0:
    print("Rok jest przestepny")
elif rok%400!=0:
    print("Rok jest zwykly")
else: print("Rok jest przestepny")

print()
#Modul 3.2
print("Modul 3.2 petle")
print()
print("3.2.1.3 LABORATORIUM: Pętla while - Zgadnij sekretny numer")
tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
numer=int(input("Podaj numer: "))
while numer!=tajny_numer:
    print(
        """
        
        Nie, to nie jest ta liczba,
        którą wybrałem dla ciebie. 
        Spróbuj ponownie!
        
        """)
    numer=int(input("Podaj inny numer: "))
print(
    """
    ____________________________________
    Dobra robota!
    To numer, który wybrałem dla ciebie! 
    Jesteś teraz wolny.
    ____________________________________
    """)
print()
print("3.2.1.6 LABORATORIUM: Niezbędne elementy pętli for")
import time # LINIA I
for i in range(1,6):
    print(i,"Mississippi")
    # Napisz pętlę for, która liczy do pięciu.
    # Ciało pętli: wyświetl w oknie konsoli numer iteracji i słowo "Mississippi".
    time.sleep(1) # LINIA II
print("Ready or not, here I come!")
# Napisz funkcję print, która wyświetli wiadomość końcową.
print()
print("3.2.1.9 LABORATORIUM: Instrukcja break - Utknięcie w pętli")
n=str(input("Wpisz slowo: "))
while n=='pumpernikiel':
        print("Udalo ci sie opuscic petle")
        break
if n!='pumpernikiel':
    n=(input("Wpisz inne slowo(pumpernikiel): "))
    while n=='pumpernikiel':
        print("Udalo ci sie opuscic petle")
        break
    if n!='pumpernikiel':
        print("Nie bede cie torturowac, idz i odpoczni.")
print()
print("3.2.1.10 LABORATORIUM: continue - Brzydki Zjadacz Samogłosek")
slowo_uzytkownika=str(input("Wpisz slowo: "))# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera=='A':
        litera=''
        continue
    elif litera=='E':
        litera=''
        continue
    elif litera=='I':
        litera=''
        continue
    elif litera=='O':
        litera=''
        continue
    elif litera=='U':
        litera=''
    print(litera)
    continue
    # Uzupełnij pętlę for poniżej.
print()
print("koniec")
print()
print("3.2.1.11 LABORATORIUM: continue - Ładny Zjadacz Samogłosek")
slowo_bez_samoglosek = ""

slowo_uzytkownika=str(input("Wpisz slowo: "))# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika.
slowo_uzytkownika = slowo_uzytkownika.upper()

for litera in slowo_uzytkownika:
    if litera=='A':
        litera=''
        continue
    elif litera=='E':
        litera=''
        continue
    elif litera=='I':
        litera=''
        continue
    elif litera=='O':
        litera=''
        continue
    elif litera=='U':
        litera=''
    slowo_bez_samoglosek=slowo_bez_samoglosek+litera
    continue
    # Uzupełnij pętlę for poniżej.
print(slowo_bez_samoglosek)
# Wyświetl słowo przypisane do zmiennej slowo_bez_samoglosek.
print("koniec")
print()
print("3.2.1.14 LABORATORIUM: Więcej o pętli while")
blokow = int(input("Wprowadź liczbę bloków: "))
b1=blokow
wysokosc=0
n=0
while n<blokow:
    wysokosc+=1
    blokow=blokow-n
    n+=1
m=0
b=0
w=wysokosc
while w!=0:
    w-=1
    m+=1
    b=b+m
if b!=b1:
    wysokosc-=1
print("Wysokość piramidy wynosi:", wysokosc)
print()
print("3.2.1.15 LABORATORIUM: Problem Collatza")
print()
c0=int(input("Wpisz dowolną nieujemną i niezerową liczbę całkowitą: "))
liczba_krokow=0
while c0!=1:
    if c0%2==0:
        c0/=2
    else:
        c0=3*c0+1
    if c0!=1:
        c0=c0
    liczba_krokow+=1
    print(c0)
print("liczba kroków = ",liczba_krokow)
print()
print()