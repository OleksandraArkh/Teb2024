print("4.3.1.6 LABORATORIUM: Tworzenie własnej funkcji - podstawy")
print()


def czy_przestepny(rok):
    if rok % 4 == 0:
        return True
    if rok % 4 > 0:
        return False

dane_testowe = [1900, 2000, 2016, 1987]
wyniki_testow = [False, True, True, False]
for i in range(len(dane_testowe)):
    r = dane_testowe[i]
    print(r, "->", end="")
    wynik = czy_przestepny(r)
    if wynik == wyniki_testow[i]:
        print("OK")
    else:
        print("Nie powiodło się")
print()
print("4.3.1.7 LABORATORIUM: Pisanie i używanie własnych funkcji - podstawy")

def czy_przestepny(rok):
    if rok % 4 == 0:
        return True
    if rok % 4 > 0:
        return False

def dni_w_miesiacu(rok, miesiac):
    if czy_przestepny(rok)==True:
        if miesiac==1:
            return 31
        if miesiac==2:
            return 29
        if miesiac==3:
            return 31
        if miesiac==4:
            return 30
        if miesiac==5:
            return 31
        if miesiac==6:
            return 30
        if miesiac==7:
            return 31
        if miesiac==8:
            return 31
        if miesiac==9:
            return 30
        if miesiac==10:
            return 31
        if miesiac==11:
            return 30
        if miesiac==12:
            return 31
    else:
        if miesiac==1:
            return 31
        if miesiac==2:
            return 28
        if miesiac==3:
            return 31
        if miesiac==4:
            return 30
        if miesiac==5:
            return 31
        if miesiac==6:
            return 30
        if miesiac==7:
            return 31
        if miesiac==8:
            return 31
        if miesiac==9:
            return 30
        if miesiac==10:
            return 31
        if miesiac==11:
            return 30
        if miesiac==12:
            return 31


testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")
print()
print("4.3.1.8 LABORATORIUM: Pisanie i używanie własnych funkcji - podstawy")
print()
def czy_przestepny(rok):
    if rok % 4 == 0:
        return True
    if rok % 4 > 0:
        return False


def dni_w_miesiacu(rok, miesiac):
    if czy_przestepny(rok) == True:
        if miesiac == 1:
            return 31
        if miesiac == 2:
            return 29
        if miesiac == 3:
            return 31
        if miesiac == 4:
            return 30
        if miesiac == 5:
            return 31
        if miesiac == 6:
            return 30
        if miesiac == 7:
            return 31
        if miesiac == 8:
            return 31
        if miesiac == 9:
            return 30
        if miesiac == 10:
            return 31
        if miesiac == 11:
            return 30
        if miesiac == 12:
            return 31
    else:
        if miesiac == 1:
            return 31
        if miesiac == 2:
            return 28
        if miesiac == 3:
            return 31
        if miesiac == 4:
            return 30
        if miesiac == 5:
            return 31
        if miesiac == 6:
            return 30
        if miesiac == 7:
            return 31
        if miesiac == 8:
            return 31
        if miesiac == 9:
            return 30
        if miesiac == 10:
            return 31
        if miesiac == 11:
            return 30
        if miesiac == 12:
            return 31


def dzien_w_roku(rok, miesiac, dzien):
    if dni_w_miesiacu(rok, miesiac) == 31:
        for dzienm in range(1, dni_w_miesiacu(rok, miesiac) + 1):
            if dzienm == dzien:
                return f"Dzien istnieje: {rok}, {miesiac}, {dzien}"
    if dni_w_miesiacu(rok, miesiac) == 30:
        for dzienm in range(1, dni_w_miesiacu(rok, miesiac) + 1):
            if dzienm == dzien:
                return f"Dzien istnieje: {rok}, {miesiac}, {dzien}"
    if dni_w_miesiacu(rok, miesiac) == 29:
        for dzienm in range(1, dni_w_miesiacu(rok, miesiac) + 1):
            if dzienm == dzien:
                return f"Dzien istnieje: {rok}, {miesiac}, {dzien}"
    if dni_w_miesiacu(rok, miesiac) == 28:
        for dzienm in range(1, dni_w_miesiacu(rok, miesiac) + 1):
            if dzienm == dzien:
                return f"Dzien istnieje: ", rok, miesiac, dzien
    return f"Dzien nie istnieje: {rok}, {miesiac}, {dzien}"


print(dzien_w_roku(2000, 12, 31))
print()
print("4.3.1.9 LABORATORIUM: Liczby pierwsze - jak je znaleźć?")
print()
def czy_pierwsza(liczba):
	if liczba == 2:
		return liczba
	if liczba>0:
		if liczba%2!=0:
			return liczba
for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")
print()
print("4.3.1.10 LABORATORIUM: Konwersja zużycia paliwa")
print()
def l100kmtompg(litry):
    return (1*100*1000/(1609.344))/(1*litry/(3.785411784))
def mpgtol100km(mile):
    return 3.785411784/(mile*1609.344/(1000*100))
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
