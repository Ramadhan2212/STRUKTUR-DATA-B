# program menampilkan deret fibonacci

# input jumlah deret
jumlah = int(input("masukkan jumlah deret fibonacci: "))

# inisialisasi dua angka pertama 
fibo = []

a, b = 1,1 
for _ in range(jumlah):
    fibo.append(a)
    a, b = b, a + b

# tampilakan hasil
print("deret fibonacci:")
print(",".join(map(str, fibo)))