import datetime
import random


class Osoba:
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov")

    def vypis_vek(self):
        print(self.vek)


class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda):
        Osoba.__init__(self,meno,priezvisko,rok)
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda
    def pozdrav(self):
        print(f"Dobrý deň, som učiteľ {self.titul} {self.meno} {self.priezvisko} a mám {self.vek} rokov, učím predmet {self.predmet} a som tiredny triedy {self.trieda}")



class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        print(f"Ahoj, volam sa {self.meno} {self.priezvisko} a mám {self.vek} rokov a som žiakom triedy {self.trieda}")


POCET_STUDENTOV = 10
POCET_UCITELOV = 5

studenti = list()

for i in range(POCET_STUDENTOV):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)

    meno = random.choice(mena)
    meno = meno[:-1]

    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(2005,2008)
    if rok == 2005:
        trieda = "IV."
    elif rok == 2006:
        trieda = "III."
    elif rok == 2007:
        trieda = "II."
    else:
        trieda = "I."

    trieda += random.choice(("A","B","C"))

    studenti.append(Student(meno,priezvisko,rok,trieda))

print("Študenti: \n")
for i in range(POCET_STUDENTOV):
    studenti[i].pozdrav()

ucitelia = list()
for i in range(POCET_UCITELOV):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)

    meno = random.choice(mena)
    meno = meno[:-1]

    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(1958, 2004)
    predmet = random.choice(("Matematika","Fyzika","Programovanie"))
    titul = random.choice(("Mgr.","Ing.","Bc."))
    trieda = random.choice(("I.","II.","III.","IV.")) + random.choice(("A","B","C"))

    ucitelia.append(Ucitel(meno, priezvisko, rok, titul, predmet, trieda))

print("Učitelia: \n")
for i in range(POCET_UCITELOV):
    ucitelia[i].pozdrav()