mahasiswa = []

while True:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    mahasiswa.append(data)
    data = {"NIM": nim, "Nama":nama}

    tambah_lagi = input("Apakah ingin menambah data lagi? (ya/tidak): ")
    if tambah_lagi.lower() != 'ya':
        print (data)
    else:    
        break

    print("Data Mahasiswa")
    for i in mahasiswa:
        print(i['Nama'],":", i['NIM'])
    



