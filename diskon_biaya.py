# diskon_biaya.py
# Program: kalkulator diskon biaya kuliah

# Konstanta aturan bisnis
DISKON_ANAK_KARYAWAN = 0.25
DISKON_PRESTASI_TINGGI = 0.20   # IPK >= 3.8
DISKON_PRESTASI_BAIK = 0.15     # IPK >= 3.5
DISKON_MEMUASKAN = 0.10         # IPK >= 3.0
DISKON_TEPAT_WAKTU = 0.05       # bayar tepat waktu (tambahan)

print("=== Kalkulator Diskon Biaya Kuliah ===")

# --- Input 1: biaya SPP (ulangi sampai valid) ---
while True:
    try:
        biaya_spp = float(input("Biaya SPP            : Rp"))
        if biaya_spp > 0:
            break
        print("  Error: biaya harus lebih dari 0")
    except ValueError:
        print("  Error: masukkan angka yang valid")

# --- Input 2: anak karyawan? ---
while True:
    jawab = input("Anak karyawan? (y/n)  : ").lower()
    if jawab in ["y", "n"]:
        break
    print("  Error: jawab dengan y atau n")
is_anak_karyawan = (jawab == "y")

# --- Input 3: IPK (0.0 - 4.0) ---
while True:
    try:
        ipk = float(input("IPK (0.0 - 4.0)      : "))
        if 0.0 <= ipk <= 4.0:
            break
        print("  Error: IPK harus antara 0.0 dan 4.0")
    except ValueError:
        print("  Error: masukkan angka yang valid")

# --- Input 4: tepat waktu? ---
while True:
    jawab = input("Bayar tepat waktu? (y/n): ").lower()
    if jawab in ["y", "n"]:
        break
    print("  Error: jawab dengan y atau n")
is_tepat_waktu = (jawab == "y")

# --- Hitung diskon utama (hanya satu yang berlaku) ---
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

# --- Diskon tambahan: tepat waktu ---
if is_tepat_waktu:
    diskon_tambahan = DISKON_TEPAT_WAKTU
else:
    diskon_tambahan = 0.0

total_diskon = diskon_utama + diskon_tambahan
potongan = biaya_spp * total_diskon
biaya_final = biaya_spp - potongan

# --- Tampilkan hasil ---
print("\n=== Hasil Perhitungan ===")
print(f"Kategori diskon : {kategori}")
print(f"Diskon utama    : {diskon_utama:.0%}")
print(f"Diskon tepat waktu: {diskon_tambahan:.0%}")
print(f"Total diskon    : {total_diskon:.0%}")
print(f"Biaya SPP       : Rp{biaya_spp:,.0f}")
print(f"Potongan        : Rp{potongan:,.0f}")
print(f"Biaya final     : Rp{biaya_final:,.0f}")