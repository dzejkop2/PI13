import tkinter as tk


canvas = tk.Canvas()
canvas.pack()


class Tvar:
    def __init__(self, x, y, dlzka, farba="white"):
        self.x = x
        self.y = y
        self.dlzka = dlzka
        self._farba = farba

    def __str__(self):
        return f"Ja som tvar, x: {self.x}, y: {self.y}, dlzka: {self.dlzka}, farba: {self._farba}"


class Stvorec(Tvar):
    def vykresli(self):
        canvas.create_rectangle(self.x, self.y, self.x + self.dlzka, self.y + self.dlzka, fill=self._farba)


tvar = Tvar(10, 10, 100)
print(tvar)

stvorec = Stvorec(10,10,100,"red")
stvorec.vykresli()

canvas.mainloop()
