#############################################################################
# TOPIK : TUMPUKAN DOKUMEN
# NO KELOMPOK : 
# ANGGOTA : 
# - IHSAN HAMIZAN (J0403251051)
# - MUHAMMAD RAIHAN RAMADHAN (J0403251038)
# - HANIF MISBAH (J0403251)
#
#############################################################################

from os import system, name
from stack import Stack

data = Stack()
nama_file = "tumpukan.txt"

# Fungsi untuk membersihkan layar
def clear() :
    if name == 'nt':
        c = system('cls')
    else:
        c = system('clear')

# Fungsi untuk melihat daftar dokumen
def daftarDokumen() :
    for urutan,dokumen in enumerate(data.data) :
        print(f"{urutan+1}.{dokumen['judul']}")

# Fungsi untuk melihat isi tumpukan Dokumen
def read() :
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file :
            barisBersih = baris.strip()
            judul, penulis = barisBersih.split(',')
            dokumen = {'judul' : judul, 'penulis' : penulis}
            data.push(dokumen)
    
    print("Data telah berhasil dibaca")
    

# Fungsi untuk menghapus dokumen dari tumpukan dokumen
def delete() :
    if len(data.data) == 0:
        print("Tidak ada dokumen untuk dihapus")
        return

    item = data.peek()
    print(f"data teratas adalah dokumen dengan judul \"{item['judul']}\" dengan penulis \"{item['penulis']}\".")
    konfirmasi = input("Yakin mau hapus? (yes/no): ").lower()

    if konfirmasi == "yes":
        dokumen = data.pop()
        print("Dokumen", dokumen, "berhasil dihapus")
    else:
        print("Penghapusan dibatalkan")

# Fungsi untuk memperbarui isi dari tumpukan dokumen
def update() :
    with open(nama_file,"w",encoding="utf-8") as file :
        for dokumen in data.data :
            file.write(f"{dokumen['judul']},{dokumen['penulis']}\n")

    print("Tumpukan berhasil diperbarui")

# Fungsi untuk menambah dokumen ke tumpukan dokumen
def create() :
    judulDokumen = input("Masukkan nama judul dokumen : ")
    penulisDOkumen = input("Masukkan nama penulis dokumen : ")

    data.push({
        "judul" : judulDokumen,
        "penulis" : penulisDOkumen
    })

    print("Dokumen berhasil dibuat")

def sorting(item, sort_by="judul") : 
    if len(item)>1:             #Syarat rekursi jika data tersisa 1 maka rekursi akan berhenti
        mid = len(item)//2      #proses membagi dua datalist untuk mencari titik tengah
        lefthalf = item[:mid]   #proses membagi data dimana data dari index awal hingga tengah akan masuk ke bagian kiri
        righthalf = item[mid:]  #proses membagi data dimana data dari index tengah hingga akhir akan masuk ke bagian kanan
        sorting(lefthalf, sort_by)       #proses rekursi yang akan terus membelah data sebelah kiri
        sorting(righthalf, sort_by)      #proses rekursi yang akan terus membelah data sebelah kanan
        l=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kiri
        r=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kanan
        t=0                     #variabel untuk menempatkan kembali data ke list utama
        
        #proses membandingkan data kiri dan kanan dengan metode ascending
        while l < len(lefthalf) and r < len(righthalf): 
            if lefthalf[l][sort_by] <= righthalf[r][sort_by]:
                item[t]=lefthalf[l]
                l=l+1
            else:
                item[t]=righthalf[r]
                r=r+1
            t=t+1
        #pengecekan kembali sisa data yang belum terurut disebelah kiri
        while l < len(lefthalf):
            item[t]=lefthalf[l]
            l=l+1
            t=t+1
        #pengecekan kembali sisa data yang belum terurut disebelah kanan
        while r < len(righthalf):
            item[t]=righthalf[r]
            r=r+1
            t=t+1

# Fungsi untuk mencari dokumen di dalam tumpukan dokumen
def cari(data, item) :
    first = 0
    last = len(data)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if data[midpoint]['judul'] == item:
            return print("Dokumen ditemukan:", data[midpoint]['judul'])
        else:
            if item < data[midpoint]['judul']:
                last = midpoint-1
            else:
                first = midpoint+1
    return print("Data tidak ditemukan")




def main() :
    global lanjut
    print(f"{"="*10}Isi tumpukan Dokumen{"="*10}")
    daftarDokumen()
    print(f"{"="*40}")
    print("1.Melihat tumpukan dokumen")
    print("2.Memperbarui tumpukan dokumen")
    print("3.Menghapus dokumen")
    print("4.Membuat dokumen")
    print("5.Mengurutkan  dokumen")
    print("6.Mencari dokumen anda")
    print("7.Keluar")
    

    pilihan = int(input("Menu yang dipilih : "))
    clear()
    match pilihan :
        case 1 :
            read()
        case 2 :
            update()
        case 3 :
            delete()
        case 4 :
            create()
        case 5 :
            sorting(data.data)
            print("Dokumen berhasil diurutkan", data.data)
        case 6 :
            inputCari = input("Masukkan nama dokumen yang ingin dicari : ")
            item_list = list(data.data)
            sorting(item_list)
            cari(item_list, inputCari)
        case 7 :
            lanjut = False
        case _ :
            if name == 'nt':
                c = system('cls')
            else:
                c = system('clear')

lanjut = True
while lanjut :

    main()
