# Minta input jumlah deret dari pengguna
jumlah = int(input("Masukkan jumlah deret yang ingin ditampilkan: "))

# Inisialisasi deret sesuai pola kamu
deret = []

for i in range(jumlah):
    if i == 0:
        deret.append(1)
    elif i == 1:
        deret.append(2)
    elif i == 2:
        deret.append(2)
    elif i == 3:
        deret.append(5)
    elif i == 4:
        deret.append(8)
    else:
        # Setelah angka kelima, lanjut dengan pola a[n] = a[n-2] + a[n-1]
        deret.append(deret[i - 2] + deret[i - 1])

# Tampilkan hasil
print("Output:")
for i in range(len(deret)):
    print(deret[i], end=", " if i < len(deret) - 1 else "")