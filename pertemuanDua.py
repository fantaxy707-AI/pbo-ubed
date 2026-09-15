# == Modul Praktikum Python: Functions (Tema: Sistem Perpustakaan) == #

import datetime

# --- VARIABEL GLOBAL ---
stok_buku_pusat = 500
biaya_admin = 5000


# --- DEFINISI FUNGSI ---
def sapa_anggota():
    print('Selamat datang di Sistem Perpustakaan Daerah')
    print('Sistem siap menerima perintah\n')


def hitung_denda(hari_terlambat, tarif_per_hari):
    total_denda = hari_terlambat * tarif_per_hari
    print('Total denda keterlambatan: Rp', total_denda)


def proses_peminjaman():
    global stok_buku_pusat
    stok_buku_pusat = stok_buku_pusat - 1
    print('Proses peminjaman berhasil dicatat.')
    print('Sisa stok buku pusat saat ini:', stok_buku_pusat)


def hitung_poin_membaca(jumlah_buku):
    if jumlah_buku == 1:
        return 10
    else:
        return (10 * jumlah_buku) + hitung_poin_membaca(jumlah_buku - 1)


def proses_pendaftaran_anggota():
    biaya_kartu = 15000  # Variabel lokal
    total_biaya = biaya_admin + biaya_kartu
    print('Total biaya pendaftaran anggota baru: Rp', total_biaya)


def cetak_waktu_peminjaman():
    waktu_sekarang = datetime.datetime.now()
    print('Waktu transaksi tercatat:', waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S"))


# --- FUNGSI UTAMA (MAIN) ---
def main():
    print("=== SISTEM PERPUSTAKAAN DIMULAI ===")
    cetak_waktu_peminjaman()
    sapa_anggota()

    # Semua pemanggilan fungsi dieksekusi di sini
    proses_pendaftaran_anggota()
    print('\n')

    hitung_denda(5, 2000)
    print('\n')

    proses_peminjaman()
    proses_peminjaman()
    print('\n')

    total_buku_dibaca = 4
    poin = hitung_poin_membaca(total_buku_dibaca)
    print("Total poin untuk anggota yang membaca", total_buku_dibaca, "buku adalah:", poin)
    print("=== SISTEM SELESAI ===")


# --- ENTRY POINT ---
if __name__ == '__main__':
    main()