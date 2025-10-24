gaji_pokok = 300000
print("SILAHKAN INPUT DATA ANDA")
nama = input("Nama Karyawan :")
golongan = input("Golongan Jabatan [1,2,3]:")
pendidikan = input("Pendidikan [SMA/D1/D3/S1]:")
jam_kerja =int(input("Jumlah Jam Kerja :"))

if golongan == "1":
	persentase_jabatan = 0.05 * gaji_pokok
elif golongan== "2":
	persentase_jabatan = 0.10 * gaji_pokok
elif golongan == "3":
	persentase_jabatan = 0.15 * gaji_pokok
else:
	persentase_jabatan = 0

if pendidikan.upper() == "SMA":
	persentase_pendidikan  = 0.025 * gaji_pokok
elif pendidikan.upper() == "D1":
	persentase_pendidikan  = 0.05 * gaji_pokok
elif pendidikan.upper() == "D3":
	persentase_pendidikan  = 0.20 * gaji_pokok
elif pendidikan.upper() == "S1":
	persentase_pendidikan = 0.30 * gaji_pokok
else:
	persentase_pendidikan = 0

if jam_kerja >= 8:
    lembur = jam_kerja * 3500

gaji = gaji_pokok + persentase_jabatan + persentase_pendidikan

print("Karyawan yang bernama "  +str(nama))
print("Honor yang diterima ", gaji)
print("   Tunjangan Jabatan ", persentase_jabatan)
print("   Tunjangan Pendidikan ", persentase_pendidikan)
print("   Honor Lembur ", lembur )



