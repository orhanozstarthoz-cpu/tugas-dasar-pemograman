# Program Perhitungan Gaji Karyawan PT. BOS PELIT

# Gaji pokok karyawan
gaji_pokok = 300000

# Input data karyawan
nama_karyawan = input("Masukkan Nama karyawan: ")
golongan = int(input("Masukkan golongan jabatan (1-3): "))
pendidikan = input("Masukkan tingkat pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Masukkan jumlah jam kerja dalam sehari: "))

# Hitung gaji sesusai dengan jabatan masing-masing
if  golongan == 1 :
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid!")

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Tingkat pendidikan tidak valid!")

# --- Hitung honor lembur ---
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# --- Total gaji akhir ---
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# --- Tampilkan hasil ---
print("\n=== RINCIAN GAJI KARYAWAN ===")
print("Nama Karyawan       : " ,nama_karyawan)
print("Gaji Pokok          : ", gaji_pokok)
print("Tunjangan Jabatan   : " ,tunjangan_jabatan)
print("Tunjangan Pendidikan : " ,tunjangan_pendidikan)
print("Honor Lembur        : " ,lembur)
print("Total Gaji Diterima : " , total_gaji )