# ringkasan_algoritma.py
# Program: ringkasan hasil algoritma dari tiga studi kasus
#   (a) persentase mahasiswa per status
#   (b) rata-rata diskon yang diberikan
#   (c) persentase item yang perlu restock
#
# ASUMSI (karena soal tidak menjelaskan):
#   - Aturan Soal 1 punya 3 status, jadi tabel (a) menampilkan ketiganya.
#   - Rata-rata diskon dihitung dua cara: semua transaksi, dan hanya
#     transaksi yang mendapat diskon (> 0%).
#   - "Perlu restock" = stok <= 10 (status RENDAH atau HABIS).

# ============================================================
# KONSTANTA ATURAN BISNIS
# ============================================================
IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18

DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20   # IPK >= 3.8
DISKON_PRESTASI_BAIK = 0.15     # IPK >= 3.5
DISKON_MEMUASKAN = 0.10         # IPK >= 3.0
DISKON_TEPAT_WAKTU = 0.05

BATAS_PERINGATAN = 10           # stok <= 10 perlu restock

# ============================================================
# DATA CONTOH
# ============================================================
daftar_mhs = [
    {"nim": "2021001", "nama": "Andi", "ipk": 3.52, "sks": 20},
    {"nim": "2021002", "nama": "Budi", "ipk": 1.75, "sks": 15},
    {"nim": "2021003", "nama": "Cici", "ipk": 3.90, "sks": 22},
    {"nim": "2021004", "nama": "Dodi", "ipk": 1.20, "sks": 12},
    {"nim": "2021005", "nama": "Eka",  "ipk": 3.00, "sks": 18},
    {"nim": "2021006", "nama": "Fani", "ipk": 2.50, "sks": 15},
    {"nim": "2021007", "nama": "Gita", "ipk": 1.40, "sks": 20},
    {"nim": "2021008", "nama": "Hadi", "ipk": 2.80, "sks": 21},
]

# Transaksi diskon: (ipk, is_anak_karyawan, is_tepat_waktu)
data_diskon = [
    (3.5, True,  False),
    (3.9, False, True),
    (3.6, False, False),
    (3.2, False, True),
    (2.8, False, False),
    (2.8, False, True),
    (3.9, True,  True),
]

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
# FUNGSI ATURAN BISNIS
# ============================================================
def tentukan_status(ipk, sks):
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"
    else:
        return "Tidak Aktif"


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    """Mengembalikan total diskon (contoh: 0.25 = 25%)."""
    if is_anak_karyawan:
        diskon_utama = DISKON_ANAK_KARYAWAN
    elif ipk >= 3.8:
        diskon_utama = DISKON_PRESTASI_TINGGI
    elif ipk >= 3.5:
        diskon_utama = DISKON_PRESTASI_BAIK
    elif ipk >= 3.0:
        diskon_utama = DISKON_MEMUASKAN
    else:
        diskon_utama = 0.0

    diskon_tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0.0
    return diskon_utama + diskon_tambahan


def perlu_restock(stok):
    """True jika stok RENDAH atau HABIS."""
    return stok <= BATAS_PERINGATAN


def hitung_persen(bagian, total):
    """Persentase bagian dari total. Aman jika total = 0."""
    if total == 0:
        return 0.0
    return bagian / total * 100


# ============================================================
# FUNGSI CETAK TABEL
# ============================================================
GARIS_3 = "+" + "-" * 30 + "+" + "-" * 8 + "+" + "-" * 10 + "+"
GARIS_2 = "+" + "-" * 36 + "+" + "-" * 14 + "+"


def tabel_3_kolom(judul, baris, total):
    """baris = list of (label, jumlah). Cetak tabel Keterangan/Jumlah/Persen."""
    print(f"\n{judul}")
    print(GARIS_3)
    print(f"| {'Keterangan':<28} | {'Jumlah':>6} | {'Persen':>8} |")
    print(GARIS_3)
    for label, jumlah in baris:
        persen = hitung_persen(jumlah, total)
        print(f"| {label:<28} | {jumlah:>6} | {persen:>7.1f}% |")
    print(GARIS_3)
    print(f"| {'Total':<28} | {total:>6} | {100.0:>7.1f}% |")
    print(GARIS_3)


def tabel_2_kolom(judul, baris):
    """baris = list of (label, nilai_teks)."""
    print(f"\n{judul}")
    print(GARIS_2)
    print(f"| {'Keterangan':<34} | {'Nilai':>12} |")
    print(GARIS_2)
    for label, nilai in baris:
        print(f"| {label:<34} | {nilai:>12} |")
    print(GARIS_2)


# ============================================================
# (a) PERSENTASE MAHASISWA PER STATUS
# ============================================================
jumlah_status = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
for mhs in daftar_mhs:
    status = tentukan_status(mhs["ipk"], mhs["sks"])
    jumlah_status[status] += 1

persen_aktif = hitung_persen(jumlah_status["Aktif"], len(daftar_mhs))

# ============================================================
# (b) RATA-RATA DISKON
# ============================================================
total_diskon_semua = 0.0
jumlah_penerima = 0
for ipk, is_anak, is_tepat in data_diskon:
    diskon = hitung_diskon(ipk, is_anak, is_tepat)
    total_diskon_semua += diskon
    if diskon > 0:
        jumlah_penerima += 1

jumlah_transaksi = len(data_diskon)
rata_semua = hitung_persen(total_diskon_semua, jumlah_transaksi)
rata_penerima = hitung_persen(total_diskon_semua, jumlah_penerima)

# ============================================================
# (c) PERSENTASE ITEM YANG PERLU RESTOCK
# ============================================================
jumlah_restock = 0
for item in inventaris:
    if perlu_restock(item["stok"]):
        jumlah_restock += 1

persen_restock = hitung_persen(jumlah_restock, len(inventaris))

# ============================================================
# TAMPILKAN LAPORAN
# ============================================================
print("=" * 50)
print("RINGKASAN ALGORITMA TIGA STUDI KASUS")
print("=" * 50)

tabel_3_kolom(
    "(a) Status Mahasiswa",
    [("Aktif", jumlah_status["Aktif"]),
     ("Peringatan", jumlah_status["Peringatan"]),
     ("Tidak Aktif", jumlah_status["Tidak Aktif"])],
    len(daftar_mhs),
)

tabel_2_kolom(
    "(b) Rata-rata Diskon",
    [("Jumlah transaksi", str(jumlah_transaksi)),
     ("Transaksi yang dapat diskon", str(jumlah_penerima)),
     ("Rata-rata (semua transaksi)", f"{rata_semua:.1f}%"),
     ("Rata-rata (penerima diskon saja)", f"{rata_penerima:.1f}%")],
)

tabel_3_kolom(
    "(c) Kebutuhan Restock",
    [("Perlu restock (RENDAH/HABIS)", jumlah_restock),
     ("Stok mencukupi", len(inventaris) - jumlah_restock)],
    len(inventaris),
)

tabel_2_kolom(
    "RINGKASAN AKHIR",
    [("Mahasiswa berstatus Aktif", f"{persen_aktif:.1f}%"),
     ("Rata-rata diskon (semua transaksi)", f"{rata_semua:.1f}%"),
     ("Item perlu restock", f"{persen_restock:.1f}%")],
)