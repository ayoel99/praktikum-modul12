# validasi_data.py
# Program: validasi data mahasiswa (NIM, IPK, SKS, semester)
# Setiap fungsi validasi mengembalikan LIST ERROR.
# List kosong = data valid.

# Konstanta aturan bisnis
PANJANG_NIM = 10
TAHUN_MIN = 2000
TAHUN_MAKS = 2037
IPK_MIN = 0.0
IPK_MAKS = 4.0
SKS_MIN = 0
SKS_MAKS = 24
SEMESTER_MIN = 1
SEMESTER_MAKS = 14


def validasi_nim(nim):
    """NIM: 10 digit angka, tahun masuk 2000-2037."""
    errors = []
    if not nim.isdigit():
        errors.append("NIM harus berisi angka saja")
    elif len(nim) != PANJANG_NIM:
        errors.append(f"NIM harus {PANJANG_NIM} digit (sekarang {len(nim)})")
    else:
        tahun = int(nim[:4])
        if tahun < TAHUN_MIN or tahun > TAHUN_MAKS:
            errors.append(f"Tahun masuk di NIM ({tahun}) harus "
                          f"antara {TAHUN_MIN} dan {TAHUN_MAKS}")
    return errors


def validasi_ipk(ipk_teks):
    """IPK: angka antara 0.0 dan 4.0."""
    errors = []
    try:
        ipk = float(ipk_teks)
    except ValueError:
        errors.append("IPK harus berupa angka")
        return errors
    if not (IPK_MIN <= ipk <= IPK_MAKS):
        errors.append(f"IPK harus antara {IPK_MIN} dan {IPK_MAKS}")
    return errors


def validasi_sks(sks_teks):
    """SKS: bilangan bulat antara 0 dan 24."""
    errors = []
    try:
        sks = int(sks_teks)
    except ValueError:
        errors.append("SKS harus berupa bilangan bulat")
        return errors
    if sks < SKS_MIN or sks > SKS_MAKS:
        errors.append(f"SKS harus antara {SKS_MIN} dan {SKS_MAKS}")
    return errors


def validasi_semester(semester_teks):
    """Semester: bilangan bulat antara 1 dan 14."""
    errors = []
    try:
        semester = int(semester_teks)
    except ValueError:
        errors.append("Semester harus berupa bilangan bulat")
        return errors
    if semester < SEMESTER_MIN or semester > SEMESTER_MAKS:
        errors.append(f"Semester harus antara {SEMESTER_MIN} dan {SEMESTER_MAKS}")
    return errors


def validasi_data_mahasiswa(nim, ipk, sks, semester):
    """Gabungkan semua validasi. Mengembalikan list semua error."""
    errors = []
    errors.extend(validasi_nim(nim))
    errors.extend(validasi_ipk(ipk))
    errors.extend(validasi_sks(sks))
    errors.extend(validasi_semester(semester))
    return errors


# ============================================================
# PROGRAM UTAMA
# ============================================================
print("=== Validasi Data Mahasiswa ===")

while True:
    print("\nMasukkan data mahasiswa:")
    nim = input("NIM      : ").strip()
    ipk = input("IPK      : ").strip()
    sks = input("SKS      : ").strip()
    semester = input("Semester : ").strip()

    daftar_error = validasi_data_mahasiswa(nim, ipk, sks, semester)

    print("\n--- Hasil Validasi ---")
    if len(daftar_error) == 0:
        print("DATA VALID. Semua data memenuhi aturan.")
    else:
        print(f"DATA TIDAK VALID. Ditemukan {len(daftar_error)} kesalahan:")
        for nomor, pesan in enumerate(daftar_error, start=1):
            print(f"  {nomor}. {pesan}")

    lagi = input("\nValidasi data lain? (y/n): ").strip().lower()
    if lagi != "y":
        print("Terima kasih. Program selesai.")
        break
        