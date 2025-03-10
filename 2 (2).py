class Ninja:
    def intro(self):
        print("There are many levels of ninja.")
    
    def ninja(self):
        print("Each ninja has their own levels.")


class Naruto(Ninja):
    def levels(self):
        print("Naruto levels: Genin!")


class Sasuke(Ninja):
    def levels(self):
        print("Sasuke levels: Chunin!")


# Membuat objek dari kelas Naruto dan Sasuke
naruto = Naruto()
sasuke = Sasuke()

# Polimorfisme: Iterasi objek dan memanggil metode tanpa melihat kelasnya
for ninja in (naruto, sasuke):
    ninja.intro()
    ninja.ninja()
    ninja.levels()
