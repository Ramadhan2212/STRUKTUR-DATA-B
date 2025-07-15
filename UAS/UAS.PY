# Inisialisasi array untuk menyimpan data customer
nama_customer = []
tanggal_belanja = []
barang_dibeli = []

# Menentukan jumlah customer
jumlah = int(input("Berapa banyak customer yang ingin dimasukkan? "))

# Input data untuk tiap customer
for i in range(jumlah):
    print(f"\nInput Data Customer ke-{i+1}")
    nama = input("Masukkan nama customer: ")
    tanggal = input("Masukkan tanggal belanja (format: DD-MM-YYYY): ")
    
    # Input daftar barang yang akan dibeli
    daftar_barang = []
    jumlah_barang = int(input("Berapa banyak jenis barang yang dibeli? "))
    for j in range(jumlah_barang):
        barang = input(f"  Masukkan nama barang ke-{j+1}: ")
        daftar_barang.append(barang)
    
    # Simpan semua data
    nama_customer.append(nama)
    tanggal_belanja.append(tanggal)
    barang_dibeli.append(daftar_barang)