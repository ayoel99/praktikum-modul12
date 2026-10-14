# peringatan_stok.py
# Program: sistem peringatan stok barang

# Konstanta aturan bisnis
BATAS_AMAN = 20
BATAS_PERINGATAN = 10


def cek_status_stok(stok):
    """Kembalikan (status, rekomendasi, prioritas) berdasarkan jumlah stok."""
    if stok == 0:
        return "HABIS", "URGENT: restock segera!", "CRITICAL"
    elif stok <= BATAS_PERINGATAN:
        return "RENDAH", "Restock dalam 1-3 hari", "HIGH"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "Rencanakan restock 1-2 minggu", "MEDIUM"
    else:
        return "AMAN", "Stok mencukupi", "LOW"


# Data inventaris: list berisi dictionary (9 item, semua status ada)
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

# Penghitung (counter)
total_nilai = 0
total_stok = 0
jumlah_per_status = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}
perlu_tindakan = 0   # item berprioritas HIGH atau CRITICAL

# --- Laporan per item ---
print("=" * 70)
print("LAPORAN STATUS INVENTARIS")
print("=" * 70)

for item in inventaris:
    status, rekomendasi, prioritas = cek_status_stok(item["stok"])
    nilai = item["stok"] * item["harga"]

    # update penghitung
    total_nilai += nilai
    total_stok += item["stok"]
    jumlah_per_status[status] += 1
    if prioritas in ["HIGH", "CRITICAL"]:
        perlu_tindakan += 1

    print(f"{item['kode']} {item['nama']:<16} Stok:{item['stok']:>3}  "
          f"Status:{status:<11} [{prioritas}]")
    if prioritas != "LOW":
        print(f"     -> {rekomendasi}")

# --- Ringkasan statistik ---
jumlah_item = len(inventaris)
rata_rata_stok = total_stok / jumlah_item

print("\n" + "=" * 70)
print("RINGKASAN")
print("=" * 70)
print(f"Jumlah item            : {jumlah_item}")
for status, jumlah in jumlah_per_status.items():
    print(f"  Status {status:<11}   : {jumlah}")
print(f"Item perlu tindakan    : {perlu_tindakan} dari {jumlah_item}")
print(f"Total stok             : {total_stok} unit")
print(f"Rata-rata stok per item: {rata_rata_stok:.1f} unit")
print(f"Total nilai inventaris : Rp{total_nilai:,}")
