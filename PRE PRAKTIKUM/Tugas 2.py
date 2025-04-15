# Meminta input dari pengguna
jumlah_deret = int(input("Masukkan jumlah deret bilangan genap: "))

print("Output:", end=" ")

# Menggunakan loop untuk mencetak bilangan genap
bilangan = 2
for i in range(jumlah_deret):
    print(bilangan, end=", " if i < jumlah_deret - 1 else "")
    bilangan += 2