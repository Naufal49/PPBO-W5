class AkunGame:
    def __init__(self, username, saldo_diamond):
        self.username = username
        self.saldo_diamond = saldo_diamond 

    def __mul__(self, topup):
        print("Top-up diamond:", topup.jumlah, "diamond")
        return self.saldo_diamond + topup.jumlah

class TopUp:
    def __init__(self, jumlah):
        self.jumlah = jumlah 

akun1 = AkunGame("Naufal", 9500)
topup_game = TopUp(1500)
print (f"Total diamond {akun1.username}: {akun1 * topup_game} diamond")


