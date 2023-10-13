import datetime


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
    def __init__(self, meno, priezvisko, rok, titul, predmet):
        Osoba.__init__(self,meno,priezvisko,rok)
        self.titul = titul
        self.predmet = predmet
    def pozdrav(self):
        print(f"Dobrý deň, som učiteľ {self.titul} {self.meno} {self.priezvisko} a mám {self.vek} rokov, učím predmet {self.predmet}")


jozo = Ucitel("Jozef","Hruška",1995, "Ing.", "Programovanie")
jano = Osoba("Ján","Jablko",2004)


jozo.pozdrav()
jozo.vypis_vek()
jano.pozdrav()
jano.vypis_vek()