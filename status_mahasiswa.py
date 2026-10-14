# status_mahasiswa.py
# Program: menentukan status 5 mahasiswa

# Konstanta aturan bisnis (huruf besar semua)
IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18
JUMLAH_MAHASISWA = 5

daftar_mhs = []  # list kosong untuk menampung data

# --- Tahap 1: input data ---
print("=== Input Data Mahasiswa ===")
for i in range(1, JUMLAH_MAHASISWA + 1):
    print(f"\nMahasiswa ke-{i}")
    nim = input("NIM  : ")
    nama = input("Nama : ")
    ipk = float(input("IPK  : "))
    sks = int(input("SKS  : "))

    mhs = {"nim": nim, "nama": nama, "ipk": ipk, "sks": sks}
    daftar_mhs.append(mhs)  # masukkan ke list

# --- Tahap 2: tentukan status & tampilkan ---
print("\n=== LAPORAN STATUS MAHASISWA ===")
print(f"{'NIM':<12} {'Nama':<15} {'IPK':>5} {'SKS':>4}  Status")
print("-" * 50)

for mhs in daftar_mhs:
    if mhs["ipk"] >= IPK_MIN_AKTIF and mhs["sks"] >= SKS_MIN:
        status = "Aktif"
    elif mhs["ipk"] >= IPK_MIN_PERINGATAN:
        status = "Peringatan"
    else:
        status = "Tidak Aktif"

    print(f"{mhs['nim']:<12} {mhs['nama']:<15} {mhs['ipk']:>5.2f} {mhs['sks']:>4}  {status}")
    