from abc import ABC, abstractmethod
from datetime import date, timedelta

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    pass

class KetagyasSzoba(Szoba):
    pass

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglalas_hozzaadas(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Jelenleg nincsenek foglalások.")
        else:
            print("Foglalások listája:")
            for foglalas in self.foglalasok:
                print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar}")

    def elerheto_szobak(self):
        print("Elérhető szobák:")
        foglalt_szobaszamok = [foglalas.szoba.szobaszam for foglalas in self.foglalasok]
        for szoba in self.szobak:
            if szoba.szobaszam not in foglalt_szobaszamok:
                print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}")

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def felhasznaloi_interfesz(szalloda):
    while True:
        print("\nÜdvözöljük a Hotel Anteiku foglalási rendszerében!")
        print("1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Foglalások listázása")
        print("4 - Elérhető szobák listázása")
        print("5 - Kilépés")
        valasztas = input("Kérem válasszon egy opciót: ")
        if valasztas == '1':
            foglalas(szalloda)
        elif valasztas == '2':
            lemondas(szalloda)
        elif valasztas == '3':
            szalloda.foglalasok_listazasa()
        elif valasztas == '4':
            szalloda.elerheto_szobak()
        elif valasztas == '5':
            print("Köszönjük, hogy a Hotel Anteiku-t választotta. Viszontlátásra!")
            break
        else:
            print("Érvénytelen opció. Kérem próbálja újra.")

def foglalas(szalloda):
    szobaszam = input("Kérem adja meg a szobaszámot: ")
    ev = int(input("Év: "))
    honap = int(input("Hónap: "))
    nap = int(input("Nap: "))
    try:
        datum = date(ev, honap, nap)
        if datum < date.today():
            print("A megadott dátum a múltban van. Kérem adjon meg egy jövőbeli dátumot.")
            return
    except ValueError as e:
        print(f"Érvénytelen dátum: {e}")
        return
    for szoba in szalloda.szobak:
        if szoba.szobaszam == szobaszam:
            szalloda.foglalas_hozzaadas(Foglalas(szoba, datum))
            print(f"Foglalás létrehozva a(z) {szobaszam} számú szobára, dátum: {datum}")
            return
    print("A megadott szobaszám nem található.")
def lemondas(szalloda):
    szobaszam = input("Kérem adja meg a szobaszámot a lemondáshoz: ")
    for index, foglalas in enumerate(szalloda.foglalasok):
        if foglalas.szoba.szobaszam == szobaszam:
            del szalloda.foglalasok[index]
            print(f"Foglalás a(z) {szobaszam} számú szobára lemondva.")
            return
    print("A megadott szobaszámhoz nem tartozik foglalás.")

hotel_anteiku = Szalloda("Hotel Anteiku")
egyagyas1 = EgyagyasSzoba(5000, '101')
egyagyas2 = EgyagyasSzoba(5000, '102')
egyagyas3 = EgyagyasSzoba(5000, '103')
egyagyas4 = EgyagyasSzoba(5000, '104')
ketagyas1 = KetagyasSzoba(8000, '201')
ketagyas2 = KetagyasSzoba(8000, '202')
ketagyas3 = KetagyasSzoba(8000, '203')
ketagyas4 = KetagyasSzoba(8000, '204')

hotel_anteiku.szoba_hozzaadas(egyagyas1)
hotel_anteiku.szoba_hozzaadas(egyagyas2)
hotel_anteiku.szoba_hozzaadas(egyagyas3)
hotel_anteiku.szoba_hozzaadas(egyagyas4)
hotel_anteiku.szoba_hozzaadas(ketagyas1)
hotel_anteiku.szoba_hozzaadas(ketagyas2)
hotel_anteiku.szoba_hozzaadas(ketagyas3)
hotel_anteiku.szoba_hozzaadas(ketagyas4)

felhasznaloi_interfesz(hotel_anteiku)
