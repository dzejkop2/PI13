import datetime


class Osoba:
    def __init__(self, meno_param, priezvisko_param, rok_param):
        self.meno = meno_param
        self.priezvisko = priezvisko_param
        self.rok = rok_param
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov")

    def vypis_vek(self):
        print(self.vek)


kupko = Osoba("Jakub", "Geleta", 2006)
jano = Osoba("Janko", "Hruška", 2000)

kupko.pozdrav()
kupko.vypis_vek()
jano.pozdrav()
jano.vypis_vek()