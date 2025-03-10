class Naruto:
    def jutsu(self):
        print("Jutsu: Rasengan!")

    def elemen(self):
        print("Elemen: Angin")


class Sasuke:
    def jutsu(self):
        print("Jutsu: Chidori!")

    def elemen(self):
        print("Elemen: Petir")

naruto = Naruto()
sasuke = Sasuke()

for ninja in (naruto, sasuke):
    ninja.jutsu()
    ninja.elemen()
