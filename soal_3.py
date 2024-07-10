from collections import deque
antrian = deque()

def tambah_Antrian():
    pelanggan = input('Masukkan Nama Pelanggan : ')
    antrian.append(pelanggan)
    print(f'{pelanggan} Berhasil Ditambahkan Kedalam Antrian')
    print(35*'=')

def hapus_Antrian():
    if len(antrian) == 0:
        print('Data Kosong : Tidak Bisa Dihapus')
    else:
        antrian.popleft()
        print(f'Pelanggan Selanjutnya : {antrian[0]}')
    print(35*'=')  
def tampilan():
    print('''Pilihan
          1. Tambah Antrian
          2. Hapus Antrian
          3. Keluar''')
pilihan = input('Masukkan Pilihan : ')
if pilihan == '1':
    tambah_Antrian()
elif pilihan == '2':
    hapus_Antrian()
elif pilihan == '3':
    exit()
else:
    print(35*'=')
    print('Masukkan Pilihan Yang Valid!')
    print(35*'=')
while True:
    tampilan()      



   