mahasiswa = []

while True:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    mahasiswa.append(data)
    data = {"NIM": nim, "Nama":nama}

    tambah_lagi = input("Apakah ingin menambah data lagi? (ya/tidak): ")
    if tambah_lagi == 'ya':
        print (data)
    else:    
        break
    for i in mahasiswa:
        print(i['nama'],":", i['nim'])
    



