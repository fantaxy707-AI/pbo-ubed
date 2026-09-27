#==============================#
#======= STUDI KASUS 1 ========#
#==============================#
class Mahasiswa:
    def __init__(self, nama, nim, prodi, IPK):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.IPK = IPK

    def cek_status(self):
        if self.IPK >= 3.5:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_profil(self):
        print (f"nama: {self.nama}")
        print (f"nim: {self.nim}")
        print (f"prodi: {self.prodi}")
        print (f"IPK: {self.IPK}")

mhs1 = Mahasiswa("Ubed", "2595114037", "TI", 3.5)
mhs2 = Mahasiswa("Alfa", "2595114029", "TI", 2.9)
mhs3 = Mahasiswa("Gilang", "259511403726", "TI", 5.0)

mhs1.tampilkan_profil()
mhs2.tampilkan_profil()
mhs3.tampilkan_profil()

print("=" * 30)
print("=" * 30)

#==============================#
#======= STUDI KASUS 2 ========#
#==============================#
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info_kendaraan(self):
        print(f"Nama      : {self.nama}")
        print(f"merk      : {self.merk}")
        print(f"tahun     : {self.tahun}")
        print(f"Kecepatan : {self.kecepatan} km/jam")

class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def info_mobil(self):
        self.info_kendaraan()
        print(f"Kursi     : {self.jumlah_kursi} penumpang")

class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def info_motor(self):
        self.info_kendaraan()
        print(f"Tipe motor: {self.tipe_motor}")


vehicle1 = Mobil("Challanger SRT Hellcat", "Dodge", 2018, 320, 5)
vehicle2 = Motor("SRV 250 AMT", "QJMotor", 2025, 130, "Cruiser Neo-Retro Otomatis")

vehicle1.info_mobil()
print("=" * 30)
vehicle2.info_motor()
print("=" * 30)
print("=" * 30)

#==============================#
#======= STUDI KASUS 3 ========#
#==============================#
class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama

    def info_pegawai(self):
        print(f"ID Pegawai : {self.id_pegawai}")
        print(f"Nama       : {self.nama}")

class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji

    def info_gaji(self):
        print(f"Gaji       : Rp{self.gaji:,}")

class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def info_proyek(self):
        print(f"Proyek     : {self.nama_proyek}")

class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def info_pm(self):
        self.info_pegawai()
        self.info_gaji()
        self.info_proyek()


pm1 = ProjectManager("PM-001", "Ubed", 5000000, "Sistem Akademik")
pm2 = ProjectManager("PM-002", "Ilham", 6000000, "Web E-Commerce")

pm1.info_pm()
print("=" * 30)
pm2.info_pm()



























