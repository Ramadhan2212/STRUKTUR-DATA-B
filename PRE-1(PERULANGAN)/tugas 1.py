tinggi = 3

for i in range(tinggi):
    jumlah_bintang = 2 * i + 1
    jumlah_spasi = tinggi - i - 1
    print(" " * jumlah_spasi + "*" * jumlah_bintang)