import datetime

# variabel global buat stok sama biaya dasar
stok_buku = 500
biaya_admin = 5000

# fungsi dasar tanpa parameter
def sapa_anggota():
    print("Selamat datang di Perpustakaan Daerah!")
    print("Silakan pilih menu yang tersedia.\n")

# fungsi dengan argumen dan default value
def hitung_denda(hari_telat, tarif=2000):
    denda = hari_telat * tarif
    print(f"Buku telat {hari_telat} hari. Total denda: Rp{denda}")

# manipulasi variabel global dari dalam fungsi
def pinjam_buku():
    global stok_buku
    stok_buku -= 1
    print(f"Peminjaman sukses. Sisa buku di rak sekarang: {stok_buku}")

# fungsi rekursif buat ngitung poin member
def hitung_poin(jumlah_buku):
    if jumlah_buku == 1:
        return 10
    else:
        return 10 + hitung_poin(jumlah_buku - 1)

# ngetes variable scope (variabel lokal)
def daftar_member():
    biaya_kartu = 15000  # ini lokal, gak bisa dipanggil dari luar fungsi
    total = biaya_admin + biaya_kartu
    print(f"Biaya bikin kartu member baru: Rp{total}")

# pake modul bawaan Python
def cek_waktu():
    sekarang = datetime.datetime.now()
    print(f"Waktu akses: {sekarang.strftime('%Y-%m-%d %H:%M:%S')}")

# fungsi utama buat jalanin semua kode di atas
def main():
    cek_waktu()
    sapa_anggota()
    
    daftar_member()
    print("-" * 30)
    
    hitung_denda(3)
    print("-" * 30)
    
    pinjam_buku()
    pinjam_buku()
    print("-" * 30)
    
    buku_dibaca = 4
    poin_didapat = hitung_poin(buku_dibaca)
    print(f"Member ini udah baca {buku_dibaca} buku, dapet poin: {poin_didapat}")

# titik awal program jalan
if __name__ == '__main__':
    main()
