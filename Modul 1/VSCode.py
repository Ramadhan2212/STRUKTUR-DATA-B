def main():
    # Meminta jumlah mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    data_mahasiswa = {}

    # Input data untuk setiap mahasiswa
    for _ in range(jumlah_mahasiswa):
        print("\nMasukkan data mahasiswa:")
        nim = input("NIM: ")
        nama = input("Nama: ")

        # Input mata kuliah dan nilai
        mata_kuliah = []
        while True:
            mk = input("Mata kuliah (atau tekan Enter untuk selesai): ")
            if not mk:
                break
            try:
                nilai = float(input(f"Nilai untuk {mk}: "))
                mata_kuliah.append((mk, nilai))
            except ValueError:
                print("Nilai harus berupa angka. Coba lagi.")

        # Menyimpan data mahasiswa
        data_mahasiswa[nim] = {"nama": nama, "mata_kuliah": mata_kuliah}

    # Menampilkan data mahasiswa
    print("\nData Mahasiswa:")
    for nim, info in data_mahasiswa.items():
        print(f"\nNIM: {nim}")
        print(f"Nama: {info['nama']}")
        print("Mata Kuliah dan Nilai:")
        total_nilai = 0
        for mk, nilai in info["mata_kuliah"]:
            print(f"  {mk}: {nilai}")
            total_nilai += nilai
        rata_rata = total_nilai / len(info["mata_kuliah"]) if info["mata_kuliah"] else 0
        print(f"Nilai Rata-rata: {rata_rata:.2f}")

if __name__ == "__main__":
    main()