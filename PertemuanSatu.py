import random
import math

# =========================================================#
# FUNDAMENTAL DASAR#

# 0. VARIABLES AND LITERALS
nama_anggota, id_anggota = "Harold", 2595114037
print("Nama anggota:", nama_anggota)
print("ID anggota  :", id_anggota)

kuota_a = kuota_b = kuota_c = 5
print(f"kuota_a={kuota_a}, kuota_b={kuota_b}, kuota_c={kuota_c}")

MAKS_PINJAMAN_PER_ANGGOTA = 5
print("Batas maksimal pinjaman:", MAKS_PINJAMAN_PER_ANGGOTA)

literal_integer = 2595114037
literal_float = 4.7
literal_underscore = 1_000_000
literal_string = 'Perpustakaan Kampus'
literal_boolean = True
literal_khusus = None

print("Literal int (dengan underscore):", literal_underscore)
print("Literal string:", literal_string)
print("Literal None  :", literal_khusus)

# =========================================================#
# 1. TYPE CONVERSION

jumlah_buku = 120
rata_rata_pinjam_harian = 3.5

proyeksi_pinjaman = jumlah_buku + rata_rata_pinjam_harian
print("Nilai:", proyeksi_pinjaman)
print("Tipe Data:", type(proyeksi_pinjaman))

id_scan = '007'
nomor_transaksi = 23

print("Tipe id_scan sebelum casting:", type(id_scan))
id_scan = int(id_scan)
print("Tipe id_scan sesudah casting:", type(id_scan))

kode_gabungan = nomor_transaksi + id_scan
print("Kode gabungan:", kode_gabungan)
print("Tipe kode_gabungan:", type(kode_gabungan))

# =========================================================#
# 2. BASIC INPUT & OUTPUT

nama_perpustakaan = "Perpustakaan Kampus Unhasy"

print("Selamat Datang!")
print(f"Anda berada di {nama_perpustakaan}")

print("Selamat Datang!", end=' ')
print(f"di {nama_perpustakaan}")

print("Tahun Ajaran", 2026, "Selamat belajar!", sep='. ')

saldo_denda = -500
print(5)
print(saldo_denda)
print(nama_perpustakaan)

# =========================================================#
# 3. OPERATORS

# Arithmetic
stok_buku = 10
buku_dipinjam = 9
print('stok + dipinjam  =', stok_buku + buku_dipinjam)
print('stok - dipinjam  =', stok_buku - buku_dipinjam)
print('stok * dipinjam  =', stok_buku * buku_dipinjam)
print('stok / dipinjam  =', stok_buku / buku_dipinjam)
print('stok // dipinjam =', stok_buku // buku_dipinjam)
print('stok ** dipinjam =', stok_buku ** buku_dipinjam)

# Comparison
kuota_pinjam = 16
jumlah_dipinjam = 11
print('kuota > dipinjam  is', kuota_pinjam > jumlah_dipinjam)
print('kuota < dipinjam  is', kuota_pinjam < jumlah_dipinjam)
print('kuota == dipinjam is', kuota_pinjam == jumlah_dipinjam)
print('kuota != dipinjam is', kuota_pinjam != jumlah_dipinjam)
print('kuota >= dipinjam is', kuota_pinjam >= jumlah_dipinjam)
print('kuota <= dipinjam is', kuota_pinjam <= jumlah_dipinjam)

# Logical
anggota_aktif = True
punya_denda = False
print('anggota_aktif and punya_denda is', anggota_aktif and punya_denda)
print('anggota_aktif or punya_denda is', anggota_aktif or punya_denda)
print('not anggota_aktif is', not anggota_aktif)

# Identity
id1 = 5
id2 = 5
judul1 = 'Laskar Pelangi'
judul2 = 'Laskar Pelangi'
daftar1 = ['Fiksi', 'Sastra']
daftar2 = ['Fiksi', 'Sastra']
print(id1 is not id2)
print(judul1 is judul2)
print(daftar1 is daftar2)

# Membership
judul_buku = 'Bumi Manusia'
kategori = {1: 'Fiksi', 2: 'Sastra'}
print('B' in judul_buku)
print('Manusia' not in judul_buku)
print(1 in kategori)
print('Fiksi' in kategori)

# =========================================================#
#FLOW CONTROL#
# 0. BOOLEANS & BOOLEAN EXPRESSIONS

anggota_aktif = True
print("Status anggota aktif:", anggota_aktif, "->", type(anggota_aktif))

stok_buku = 0
print("stok_buku > 0 menghasilkan:", stok_buku > 0)

print("bool(0)          :", bool(0))
print("bool(1)          :", bool(1))
print("bool('')         :", bool(''))
print("bool('Buku')     :", bool('Buku'))
print("bool([])         :", bool([]))
print("bool(['Buku A']) :", bool(['Buku A']))

daftar_pinjaman = []
if daftar_pinjaman:
    print("Anggota masih punya pinjaman aktif.")
else:
    print("Tidak ada pinjaman aktif.")

# =========================================================#
# 1. IF...ELSE STATEMENT

usia_pendaftar = int(input("Masukkan usia calon anggota: "))
if usia_pendaftar >= 17:
    print("Boleh mendaftar sebagai anggota perpustakaan.")
print("Proses pendaftaran selesai.")

usia_pendaftar = int(input("Masukkan usia calon anggota: "))
if usia_pendaftar >= 17:
    print("Pendaftaran disetujui.")
else:
    print("Pendaftaran ditolak, usia belum memenuhi syarat.")

username_db = "admin"
password_db = "pustaka@123"
username = input("Masukkan username petugas: ")
password = input("Masukkan password petugas: ")
if (username == username_db) and (password == password_db):
    print("Login berhasil, selamat bekerja.")
else:
    print("Login gagal, akses ditolak.")

usia_pendaftar = int(input("Masukkan usia calon anggota: "))
if usia_pendaftar < 0:
    print("Usia tidak valid.")
elif usia_pendaftar >= 17:
    print("Pendaftaran disetujui.")
else:
    print("Pendaftaran ditolak.")

# =========================================================#
# 2. FOR LOOP

daftar_buku = ["Laskar Pelangi", "Bumi Manusia", "Negeri 5 Menara"]
for judul in daftar_buku:
    print(judul)
    print("---")

kata_kunci = 'Python'
for huruf in kata_kunci:
    print(huruf)

total_antrian = 0
for i in range(1, 11):
    total_antrian += i
print(f"Total nomor antrian = {total_antrian}")

# =========================================================#
# 3. WHILE LOOP

# while stok >= 0.0: (contoh infinite loop, stok tidak pernah diupdate)
#     print(stok)

stok = float(input("Masukkan jumlah stok buku (angka negatif untuk berhenti): "))
while stok >= 0.0:
    print(stok)
    stok = float(input("Masukkan stok buku berikutnya: "))

n = 10
i = 1
while i <= n:
    print(i)
    i += 1

total_denda = 0
denda = float(input("Masukkan nominal denda (0 untuk berhenti): "))
while denda != 0.0:
    total_denda += denda
    denda = float(input("Masukkan nominal denda (0 untuk berhenti): "))
print(f"Total denda terkumpul: Rp{total_denda}")

# =========================================================#
# 4. BREAK & CONTINUE

id_target = int(input("Masukkan ID buku yang dicari (1-5): "))
for id_buku in range(1, 6):
    if id_buku == id_target:
        break
    print(id_buku)

while True:
    jumlah_input = int(input("Masukkan jumlah buku masuk (negatif untuk berhenti): "))
    if jumlah_input < 0:
        break
    print(f"Buku masuk tercatat: {jumlah_input}")

for nomor_antrian in range(1, 11):
    if nomor_antrian % 2 == 0:
        continue
    print(nomor_antrian)

total_denda_valid = 0
while True:
    denda = int(input("Masukkan nominal denda (0 untuk berhenti): "))
    if denda < 0:
        continue
    if denda == 0:
        break
    total_denda_valid += denda
print(f"Total denda yang tercatat: Rp{total_denda_valid}")

# =========================================================#
# 5. PASS STATEMENT

anggota_valid = True
if anggota_valid:
    pass
else:
    print("Login tidak valid. Arahkan ke formulir pendaftaran.")

# =========================================================#
#DATA TYPE#

# 1. NUMBERS
id_buku = 1024
indeks_baca = 4.7
kode_referensi_kompleks = 2 + 3j

print("=== NUMBERS: int, float, complex ===")
print(f"ID Buku      : {id_buku}  -> {type(id_buku)}")
print(f"Indeks Baca  : {indeks_baca} -> {type(indeks_baca)}")
print(f"Contoh complex: {kode_referensi_kompleks} -> {type(kode_referensi_kompleks)}")

indeks_baca = round((indeks_baca + 5.0) / 2, 2)
print(f"Indeks Baca setelah review baru: {indeks_baca}")

kode_rak_hex = 0x1F
kode_rak_bin = 0b1010

print("\n=== NUMBERS: Number Systems ===")
print(f"Kode rak (hex 0x1F) dalam desimal: {kode_rak_hex}")
print(f"Kode rak (bin 0b1010) dalam desimal: {kode_rak_bin}")

print("\n=== NUMBERS: Type Conversion ===")
print("int(4.9) ->", int(4.9))
print("float(5) ->", float(5))
print("complex(3) ->", complex(3))

daftar_buku = ["Laskar Pelangi", "Bumi Manusia", "Negeri 5 Menara"]
rekomendasi_hari_ini = random.choice(daftar_buku)
print("\n=== NUMBERS: Modul random ===")
print("Rekomendasi buku hari ini:", rekomendasi_hari_ini)

total_buku_baru = 47
kapasitas_per_rak = 10
jumlah_rak_dibutuhkan = math.ceil(total_buku_baru / kapasitas_per_rak)
print("\n=== NUMBERS: Modul math ===")
print(f"{total_buku_baru} buku baru butuh {jumlah_rak_dibutuhkan} rak (kapasitas {kapasitas_per_rak}/rak)")

# =========================================================#
# 2. LIST

daftar_pinjaman = ["Laskar Pelangi", "Bumi Manusia"]

print("\n=== LIST (daftar pinjaman) ===")
print(f"Awal            : {daftar_pinjaman} -> {type(daftar_pinjaman)}")

daftar_pinjaman.append("Negeri 5 Menara")
print(f"Setelah pinjam  : {daftar_pinjaman}")

daftar_pinjaman.remove("Bumi Manusia")
print(f"Setelah kembali : {daftar_pinjaman}")
print(f"Jumlah pinjaman aktif: {len(daftar_pinjaman)}")

# =========================================================#
# 3. TUPLE

lokasi_rak = ("Lantai 2", "Rak B", 5)

print("\n=== TUPLE (lokasi rak) ===")
print(f"Lokasi rak Laskar Pelangi: {lokasi_rak} -> {type(lokasi_rak)}")
print(f"Lantai : {lokasi_rak[0]}")
print(f"Rak    : {lokasi_rak[1]}")
print(f"Slot   : {lokasi_rak[2]}")

# =========================================================#
# 4. STRING

judul_buku = "  laskar pelangi  "
penulis = "Andrea Hirata"
isbn = "978-979-1227-78-0"

print("\n=== STRING ===")
judul_bersih = judul_buku.strip().title()
print(f"Judul mentah   : '{judul_buku}'")
print(f"Judul dibersihkan: '{judul_bersih}'")

print("Panjang judul   :", len(judul_bersih))
print("Judul huruf besar semua:", judul_bersih.upper())
print("Cek ISBN diawali '978':", isbn.startswith("978"))
print("Ganti kata di judul:", judul_bersih.replace("Pelangi", "Bintang"))

kata_penulis = penulis.split(" ")
print("Split nama penulis:", kata_penulis)
print("Join dengan tanda titik:", ".".join(kata_penulis))

print("4 huruf pertama judul:", judul_bersih[:4])
print(f"Buku '{judul_bersih}' ditulis oleh {penulis} (ISBN: {isbn})")

# =========================================================#
# 5. SET

kategori_buku = {"Fiksi", "Sastra", "Fiksi", "Drama", "Sastra"}

print("\n=== SET (kategori buku) ===")
print(f"Kategori tersimpan : {kategori_buku} -> {type(kategori_buku)}")
print(f"Jumlah kategori unik: {len(kategori_buku)}")

kategori_buku.add("Non-Fiksi")
kategori_buku.add("Fiksi")
print(f"Setelah add        : {kategori_buku}")

# =========================================================#
# 6. DICTIONARY

profil_anggota = {
    "id_anggota": 2595114037,
    "nama": "Harold",
    "indeks_baca_rata_rata": indeks_baca,
    "daftar_pinjaman": daftar_pinjaman,
    "status_aktif": True,
}

print("\n=== DICTIONARY (profil anggota) ===")
print(f"Profil lengkap : {profil_anggota} -> {type(profil_anggota)}")
print(f"Nama           : {profil_anggota['nama']}")
print(f"Status aktif   : {profil_anggota['status_aktif']}")

profil_anggota["status_aktif"] = False
print(f"Setelah update : status_aktif = {profil_anggota['status_aktif']}")

# =========================================================#
#FUNCTIONS#

def sapa_anggota():
    print("Selamat datang di Perpustakaan Kampus!")

sapa_anggota()

def hitung_denda(hari_terlambat, tarif_per_hari=500):
    total = hari_terlambat * tarif_per_hari
    print(f"Total denda keterlambatan: Rp{total}")

hitung_denda(3)
hitung_denda(5, 1000)

def cek_ketersediaan(jumlah_stok):
    if jumlah_stok > 0:
        return "Buku tersedia untuk dipinjam"
    else:
        return "Buku sedang habis"

status_buku = cek_ketersediaan(2)
print("Status:", status_buku)

total_buku_perpustakaan = 500

def pinjam_buku():
    buku_dipinjam_lokal = 2
    sisa_buku = total_buku_perpustakaan - buku_dipinjam_lokal
    print(f"Sisa buku setelah dipinjam: {sisa_buku}")

pinjam_buku()

diskon_denda = lambda nominal_denda: nominal_denda - (nominal_denda * 0.1)
print(f"Denda setelah diskon: Rp{diskon_denda(50000)}")

def denda_berlipat(hari):
    if hari == 1:
        return 500
    else:
        return 2 * denda_berlipat(hari - 1)

print(f"Denda berlipat hari ke-4: Rp{denda_berlipat(4)}")

denda_mentah = 4523.10
denda_dibulatkan = math.ceil(denda_mentah)
print(f"Denda dibulatkan ke atas: Rp{denda_dibulatkan}")