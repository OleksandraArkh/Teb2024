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
#n=str(input"Wpisz slowo:")
#while n!=pumpernikiel
#    n=(input"Wpisz inne slowo:")
#    if n==pumpernikiel:
#        break
#    print("Udalo ci sie opuscic petle")
print()
print("3.2.1.10 LABORATORIUM: continue - Brzydki Zjadacz Samogłosek")
