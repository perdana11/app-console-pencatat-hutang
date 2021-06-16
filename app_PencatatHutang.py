import csv
from datetime import datetime as tg
import os

dataCSV = "dataPembelian.csv"

def load (dataCSV='dataPembelian.csv'):
    os.system("cls")
    data = []
    try:
        with open (dataCSV, "r") as file:
            for item in file.readlines():
                tulis = item.replace('\n','')
                split = tulis = tulis.split(',')
                data.append(split)
    except IOError as e:
        print(e)
    return data

def store (data, dataCSV='dataPembelian.csv'):
    try:
        list_Penampung = []
        for item in data:
            list_Penampung.append(','.join(item)+'\n')
        with open (dataCSV, 'w') as file:
            file.writelines(list_Penampung)
    except IOError as e:
        print(e)

def lihat_data(data):
    print('{0:^80}'.format('===DAFTAR PENGHUTANG==='))
    print('')
    print("{0:2s} {1:10s} {2:8s}    {3:16s}      {4:16s}   {5:8s}".format("No","Tanggal","Nama Orang", "Nama Barang", "Jumlah Barang", "Total Harga"))
    #memprint header untuk tampilan pada terminal
    print("="*80)
    for i in range(len(data)):
        total = int(data[i][4])
        format_total = 'Rp {:,}'.format(total)
        print("{0:2d} {1:10s}   {2:8s}     {3:16s}       {4:16s}  {5:8s}".format(i+1,data[i][0], data[i][1], data[i][2],data[i][3], format_total))

def menambah_data(data):
    os.system('cls')
    print("---Masukkan Data---")
    print('')
    tanggal = tg.now().strftime('%d-%m-%Y')
    nama_orang = input("Nama Orang: ")
    nama_barang = input("Nama Barang: ")
    jumlah = input("Jumlah Barang: ")
    total = input("Total Harga: ")
    temp = (tanggal, nama_orang, nama_barang, jumlah, total)
    data.append(temp)
    store(data)

def rubah_data(data):
    os.system('cls')
    lihat_data(data)
    print("\n---Perbarui Data---")
    index = int(input('Pilih data yang akan diperbarui: '))
    index -= 1
    preview(index)
    confirm = input('Apakah anda yakin akan memperbarui data ini?[y/t]')
    if confirm == 'y':
        data[index][1] = input('Nama Orang: ')
        data[index][2] = input('Nama Barang: ')
        data[index][3] = input('Jumlah Barang: ')
        data[index][4] = input('Total Harga: ')
        store(data)

def hapus_data(data):
    os.system('cls')
    lihat_data(data)
    print('\n---Hapus Data---')
    penghilangan = input("Nama orang yang ingin dihapus: ")
    for baris in data: 
        if penghilangan in baris :
            os.system('cls')
            print('{0:10s}   {1:8s}   {2:16s}     {3:16s}  {4:8s}'.format("Tanggal","Nama Orang", "Nama Barang", "Jumlah Barang", "Total Harga"))
            print('='*80)
            print('{0:10s}    {1:8s}     {2:16s}        {3:16s}{4:8s}'.format(baris[0], baris[1], baris[2], baris[3], "Rp "+baris[4]))
            confirm = input("Apakah Anda yakin ingin menghapus data ini?[y/t]")
            if confirm == "y":
                data.remove(baris)
                store(data)

def preview(index):
    os.system('cls')
    print('{0:2s} {1:10s} {2:8s}    {3:16s}      {4:16s}   {5:8s}'.format("No","Tanggal","Nama Orang", "Nama Barang", "Jumlah Barang", "Total Harga"))
    print('='*80)
    total = int(data[index][4])
    format_total = 'Rp {:,}'.format(total)
    print('{0:2d} {1:10s}   {2:8s}     {3:16s}       {4:16s}  {5:8s}'.format(index+1, data[index][0], data[index][1], data[index][2],data[index][3], format_total))

def cari(data):
    os.system('cls')
    index = input("Masukkan nama yang ingin dicari: ")
    for i in (data):
        if index in i:
            print('{0:10s}   {1:8s}   {2:16s}     {3:16s}  {4:8s}'.format("Tanggal","Nama Orang", "Nama Barang", "Jumlah Barang", "Total Harga"))
            print('='*80)
            total = int(i[4])
            formatTotal = 'Rp {:,}'.format(total)
            print('{0:10s}    {1:8s}     {2:16s}        {3:16s}{4:8s}'.format(i[0], i[1], i[2], i[3], formatTotal))
            print("\nMenu:  1.Hapus  2.Rubah  3.Cicil")
            menu = input("\nPilih Menu: ")
            if menu == "1":
                data.remove(i)
                store(data)
            elif menu == "2":
                i[2] = input("Nama Barang: ")
                i[3] = input("Jumlah: ")
                i[4] = input("Total Harga: ")
                store(data)
            elif menu == "3":
                besarUang = int(input("Besar Uang Untul Mencicil: Rp "))
                total = int(i[4])
                total = total - besarUang
                i[4] = str(total)
                store(data)
            else:
                input("\nTekan Enter Untuk Kembali")
    os.system('cls')

def angsur(data):
    os.system('cls')
    lihat_data(data)
    print("\n---Perbarui Data---")
    index = int(input('Pilih data yang ingin mencicil hutang: '))
    index -= 1
    preview(index)
    confirm = input('Apakah anda yakin akan memperbarui data ini?[y/t]')
    if confirm == 'y':
        besarUang = int(input("Besar Uang Untul Mencicil: Rp "))
        total = int(data[index][4])
        total = total - besarUang
        data[index][4] = str(total)
        store(data)
            
data = load()
while True:
    lihat_data(data)
    print('')
    print('Menu:\n1.Tambah  2.Perbarui  3.Hapus  4.Cari  5.Angsur  6.Keluar')
    print('')
    main_menu = input('Pilih menu: ')
    if main_menu == '1':
        menambah_data(data)
    elif main_menu == '2':
        rubah_data(data)
    elif main_menu == '3':
        hapus_data(data)
    elif main_menu == "4":
        cari(data)
    elif main_menu == "5":
        angsur(data)
    else:
        exit()