# program untuk menampilkan deret bilangan genap

# input jumlah deret
jumlah = int(input("Masukkan jumlah deret bilangan genap:"))

# inisialisasi list untuk menyiapkan deret
deret_genap = []

# loop untuk mengisi list dengan bilangan genap
for i in range(1, jumlah + 1):
    deret_genap.append(i * 2)

    # Tampilkan hasil
    print("deret bilangan deret:")
    print(",".join(map(str,deret_genap)))