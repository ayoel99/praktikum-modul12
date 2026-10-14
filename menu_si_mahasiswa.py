# menu_si_mahasiswa.py
# Program: menu interaktif Sistem Informasi Mahasiswa
# Menggabungkan: status mahasiswa, diskon biaya, peringatan stok

# ============================================================
# KONSTANTA ATURAN BISNIS
# ============================================================
IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18
SKS_MAKS = 24

DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20   # IPK >= 3.8
DISKON_PRESTASI_BAIK = 0.15     # IPK >= 3.5
DISKON_MEMUASKAN = 0.10         # IPK >= 3.0
DISKON_TEPAT_WAKTU = 0.05       # tambahan

BATAS_AMAN = 20
BATAS_PERINGATAN = 10

# Data inventaris untuk menu stok
inventaris = [
    {"kode": "B001", "nama": "Buku Python",    "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database",  "stok": 12, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB", "stok": 5,  "harga": 50000},
    {"kode": "B004", "nama": "Kabel USB",      "stok": 0,  "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless", "stok": 18, "harga": 120000},
    {"kode": "B006", "nama": "Keyboard",       "stok": 30, "harga": 150000},
    {"kode": "B007", "nama": "Headset",        "stok": 8,  "harga": 175000},
    {"kode": "B008", "nama": "Flashdisk 32GB", "stok": 0,  "harga": 80000},
    {"kode": "B009", "nama": "Kertas A4 Rim",  "stok": 60, "harga": 45000},
]


# ============================================================
# FUNGSI BANTU VALIDASI INPUT
# (terus bertanya sampai pengguna mengisi dengan benar)
# ============================================================
def baca_angka(pesan, tipe, minimum, maksimum):
    """Minta angka sampai valid. tipe = int atau float."""
    while True:
        try:
            nilai = tipe(input(pesan))
        except ValueError:
            print("  Error: masukkan angka yang valid")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum} dan {maksimum}")


def baca_ya_tidak(pesan):
    """Minta jawaban y/n. Mengembalikan True jika y."""
    while True:
        jawab = input(pesan).strip().lower()
        if jawab in ["y", "n"]:
            return jawab == "y"
        print("  Error: jawab dengan y atau n")


def baca_teks(pesan):
    """Minta teks yang tidak boleh kosong."""
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("  Error: tidak boleh kosong")


def baca_nim(pesan):
    """Minta NIM: harus 10 digit angka."""
    while True:
        nim = input(pesan).strip()
        if len(nim) == 10 and nim.isdigit():
            return nim
        print("  Error: NIM harus 10 digit angka")


# ============================================================
# FUNGSI ATURAN BISNIS
# ============================================================
def tentukan_status(ipk, sks):
    """Status akademik berdasarkan IPK dan SKS."""
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"
    else:
        return "Tidak Aktif"


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    """Mengembalikan (total_diskon, kategori, diskon_utama, diskon_tambahan)."""
    if is_anak_karyawan:
        diskon_utama = DISKON_ANAK_KARYAWAN
        kategori = "Anak Karyawan"
    elif ipk >= 3.8:
        diskon_utama = DISKON_PRESTASI_TINGGI
        kategori = "Prestasi IPK Tinggi"
    elif ipk >= 3.5:
        diskon_utama = DISKON_PRESTASI_BAIK
        kategori = "Prestasi IPK Baik"
    elif ipk >= 3.0:
        diskon_utama = DISKON_MEMUASKAN
        kategori = "IPK Memuaskan"
    else:
        diskon_utama = 0.0
        kategori = "Tidak ada diskon utama"

    diskon_tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0.0
    return diskon_utama + diskon_tambahan, kategori, diskon_utama, diskon_tambahan


def cek_status_stok(stok):
    """Mengembalikan (status, rekomendasi, prioritas)."""
    if stok == 0:
        return "HABIS", "URGENT: restock segera!", "CRITICAL"
    elif stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari", "HIGH"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu", "MEDIUM"
    else:
        return "AMAN", "Stok mencukupi", "LOW"


# ============================================================
# SUBMENU
# ============================================================
def menu_status_mahasiswa():
    print("\n--- Cek Status Mahasiswa ---")
    nim = baca_nim("NIM (10 digit)   : ")
    nama = baca_teks("Nama             : ")
    ipk = baca_angka("IPK (0.0 - 4.0)  : ", float, 0.0, 4.0)
    sks = baca_angka(f"SKS (0 - {SKS_MAKS})     : ", int, 0, SKS_MAKS)

    status = tentukan_status(ipk, sks)

    print("\n=== Hasil ===")
    print(f"NIM    : {nim}")
    print(f"Nama   : {nama}")
    print(f"IPK    : {ipk:.2f}")
    print(f"SKS    : {sks}")
    print(f"Status : {status}")


def menu_diskon():
    print("\n--- Hitung Diskon Biaya Kuliah ---")
    biaya_spp = baca_angka("Biaya SPP            : Rp", float, 1, 1_000_000_000)
    is_anak_karyawan = baca_ya_tidak("Anak karyawan? (y/n)  : ")
    ipk = baca_angka("IPK (0.0 - 4.0)      : ", float, 0.0, 4.0)
    is_tepat_waktu = baca_ya_tidak("Bayar tepat waktu? (y/n): ")

    total, kategori, utama, tambahan = hitung_diskon(
        ipk, is_anak_karyawan, is_tepat_waktu
    )
    potongan = biaya_spp * total
    biaya_final = biaya_spp - potongan

    print("\n=== Hasil Perhitungan ===")
    print(f"Kategori diskon   : {kategori}")
    print(f"Diskon utama      : {utama:.0%}")
    print(f"Diskon tepat waktu: {tambahan:.0%}")
    print(f"Total diskon      : {total:.0%}")
    print(f"Biaya SPP         : Rp{biaya_spp:,.0f}")
    print(f"Potongan          : Rp{potongan:,.0f}")
    print(f"Biaya final       : Rp{biaya_final:,.0f}")


def tampilkan_laporan_stok():
    total_nilai = 0
    perlu_tindakan = 0

    print("\n" + "=" * 65)
    print("LAPORAN STATUS INVENTARIS")
    print("=" * 65)
    for item in inventaris:
        status, rekomendasi, prioritas = cek_status_stok(item["stok"])
        total_nilai += item["stok"] * item["harga"]
        if prioritas in ["HIGH", "CRITICAL"]:
            perlu_tindakan += 1

        print(f"{item['kode']} {item['nama']:<16} Stok:{item['stok']:>3}  "
              f"Status:{status:<11} [{prioritas}]")
        if prioritas != "LOW":
            print(f"     -> {rekomendasi}")

    print(f"\nTotal nilai inventaris: Rp{total_nilai:,}")
    print(f"Item perlu tindakan   : {perlu_tindakan} dari {len(inventaris)}")


def menu_stok():
    print("\n--- Cek Peringatan Stok ---")
    print("1. Laporan seluruh inventaris")
    print("2. Cek status dari satu jumlah stok")
    sub = input("Pilih (1/2): ").strip()

    if sub == "1":
        tampilkan_laporan_stok()
    elif sub == "2":
        stok = baca_angka("Jumlah stok: ", int, 0, 100000)
        status, rekomendasi, prioritas = cek_status_stok(stok)
        print(f"\nStatus     : {status} [{prioritas}]")
        print(f"Rekomendasi: {rekomendasi}")
    else:
        print("Pilihan tidak valid!")


# ============================================================
# PROGRAM UTAMA: MENU INTERAKTIF
# ============================================================
print("=== SISTEM INFORMASI MAHASISWA ===")

while True:
    print("\nMenu:")
    print("1. Cek Status Mahasiswa")
    print("2. Hitung Diskon Biaya")
    print("3. Cek Peringatan Stok")
    print("0. Keluar")
    pilihan = input("Pilih menu (0-3): ").strip()

    if pilihan == "1":
        menu_status_mahasiswa()
    elif pilihan == "2":
        menu_diskon()
    elif pilihan == "3":
        menu_stok()
    elif pilihan == "0":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Pilih 0, 1, 2, atau 3.")