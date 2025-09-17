class Main:
    def __init__(self):
        pass

    def main(self):
        pass

    def uiLogin(self):
        pass

    def uiMenu(self):
        pass

    def uiHitungPembayaran(self):
        pass

    def uiCetakStruk(self):
        pass

class LoginKasir:
    def __init__(self, username: str = "", password: str = ""):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass

class KoneksiDatabase:
    def __init__(self, host: str = "", database: str = "", username: str = "", password: str = ""):
        self.host = host
        self.database = database
        self.username = username
        self.password = password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass

class HitungPembayaran:
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0, totalHarga: float = 0.0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass

    def deleteDataPembayaran(self):
        pass

    def cariDataPembayaranByIdMenu(self):
        pass

class PembayaranTunai:
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass

class PembayaranByCard:
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass

class CetakStruk:
    def __init__(self):
        pass

    def cetakStruk(self):
        pass

class TabelHitungPembayaran:
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0, totalHarga: float = 0.0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self, val):
        pass

    def setNamaMenu(self, val):
        pass

    def setHarga(self, val):
        pass

    def setJumlah(self, val):
        pass

    def setTotalHarga(self, val):
        pass

    def getIdMenu(self):
        pass

    def getNamaMenu(self):
        pass

    def getHarga(self):
        pass

    def getJumlah(self):
        pass

    def getTotalHarga(self):
        pass

class TabelPembayaranByCard:
    def __init__(self, idCard: str = "", jenisCard: str = "", namaBank: str = "", totalHarga: float = 0.0):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self, val):
        pass

    def setJenisCard(self, val):
        pass

    def setNamaBank(self, val):
        pass

    def setTotalHarga(self, val):
        pass

    def getIdCard(self):
        pass

    def getJenisCard(self):
        pass

    def getNamaBank(self):
        pass

    def getTotalHarga(self):
        pass

class CetakStrukData:
    def __init__(self, noStruk: str = "", totalHarga: float = 0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


mainApp = Main()
print("Main:", mainApp.__dict__)

kasir = LoginKasir("admin", "1234")
print("LoginKasir:", kasir.__dict__)

db = KoneksiDatabase("localhost", "db_kasir", "root", "12345")
print("KoneksiDatabase:", db.__dict__)

hitung = HitungPembayaran("M001", "Nasi Goreng", 15000, 2, 30000)
print("HitungPembayaran:", hitung.__dict__)

tunai = PembayaranTunai()
print("PembayaranTunai:", tunai.__dict__)

byCard = PembayaranByCard()
print("PembayaranByCard:", byCard.__dict__)

cetak = CetakStruk()
print("CetakStruk:", cetak.__dict__)

tabelHitung = TabelHitungPembayaran("M002", "Es Teh", 5000, 3, 15000)
print("TabelHitungPembayaran:", tabelHitung.__dict__)

tabelCard = TabelPembayaranByCard("C001", "Debit", "BCA", 100000)
print("TabelPembayaranByCard:", tabelCard.__dict__)

strukData = CetakStrukData("S001", 45000)
print("CetakStrukData:", strukData.__dict__)