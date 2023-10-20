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
        return f"Dobrý deň, som učiteľ {self.titul} {self.meno} {self.priezvisko} a mám {self.vek} rokov, učím predmet {self.predmet} a som tiredny triede {self.trieda}"


class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        return f"Ahoj, volam sa {self.meno} {self.priezvisko} a mám {self.vek} rokov a som žiakom triedy {self.trieda}"




POCET_STUDENTOV = 10
POCET_UCITELOV = 5
vyber_ucitel = 0
vyber_ziak = 0
studenti_triedy = list()

studenti = list()
ucitelia = list()


def uc_vyber():
    while 1:
        vyber_ucitel = input("Vyber id ucitela: ")
        try:
            int(vyber_ucitel)
        except ValueError:
            print("Treba zadať číslo")
            continue

        break

def zi_vyber():
    while 1:
        vyber_ziak = input("Vyber id ziaka: ")
        try:
            int(vyber_ziak)
        except ValueError:
            print("Treba zadať číslo")
            continue

        break

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
    print(f"{i + 1}. " + ucitelia[i].meno)


while 1:
    uc_vyber()
    if(vyber_ucitel - 1 <= len(ucitelia)):
        print(ucitelia[vyber_ucitel - 1].pozdrav())
        for i in range(len(studenti)):
            if studenti[i - 1].trieda == ucitelia[vyber_ucitel - 1].trieda:
                studenti_triedy.append(studenti[i - 1])
        break
    else:
        continue

for i in range(len(studenti_triedy)):
    print(f"{i + 1}. " + studenti_triedy[i].meno)

while 1:
    if studenti_triedy:
        zi_vyber()
        if (vyber_ziak - 1 <= len(studenti_triedy)):
            print(studenti_triedy[vyber_ziak].pozdrav())
            break
        else:
            continue
    else:
        print("V triede nikto neni :)")
        break


ucitelia_new = sorted(ucitelia, key=lambda ucitel: ucitel.priezvisko)
ziaci_new = sorted(studenti, key=lambda student: student.priezvisko)

for ucitel in ucitelia_new:
    print(ucitel.meno + " " + ucitel.priezvisko)

for student in ziaci_new:
    print(student.meno + " " + student.priezvisko)