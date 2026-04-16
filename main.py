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

# Fungsi untuk melihat isi tumpukan dokumen
def lihat() :
    pass

# Fungsi untuk menghapus dokumen dari tumpukan dokumen
def hapus(stack) :
    if len(stack) == 0:
        print("Tidak ada dokumen untuk dihapus")
        return

    print("Dokumen teratas:", stack[-1])
    konfirmasi = input("Yakin mau hapus? (yes/no): ").lower()

    if konfirmasi == "yes":
        dokumen = stack.pop()
        print("Dokumen", dokumen, "berhasil dihapus")
    else:
        print("Penghapusan dibatalkan")

# Fungsi untuk memperbarui isi dokumen dari tumpukan dokumen
def perbarui() :
    pass

# Fungsi untuk menambah dokumen ke tumpukan dokumen
def tambah() :
    
    pass


def sorting(data): 
    if len(data)>1:             #Syarat rekursi jika data tersisa 1 maka rekursi akan berhenti
        mid = len(data)//2      #proses membagi dua datalist untuk mencari titik tengah
        lefthalf = data[:mid]   #proses membagi data dimana data dari index awal hingga tengah akan masuk ke bagian kiri
        righthalf = data[mid:]  #proses membagi data dimana data dari index tengah hingga akhir akan masuk ke bagian kanan
        sorting(lefthalf)       #proses rekursi yang akan terus membelah data sebelah kiri
        sorting(righthalf)      #proses rekursi yang akan terus membelah data sebelah kanan
        l=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kiri
        r=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kanan
        t=0                     #variabel untuk menempatkan kembali data ke list utama
        
        #proses membandingkan data kiri dan kanan dengan metode ascending
        while l < len(lefthalf) and r < len(righthalf): 
            if lefthalf[l] <= righthalf[r]:
                data[t]=lefthalf[l]
                l=l+1
            else:
                data[t]=righthalf[r]
                r=r+1
            t=t+1
        #pengecekan kembali sisa data yang belum terurut disebelah kiri
        while l < len(lefthalf):
            data[t]=lefthalf[l]
            l=l+1
            t=t+1
        #pengecekan kembali sisa data yang belum terurut disebelah kanan
        while r < len(righthalf):
            data[t]=righthalf[r]
            r=r+1
            t=t+1
#data = connect to database and get data from database
pass

# Fungsi untuk mencari dokumen di dalam tumpukan dokumen
def cari(data, item) :
    first = 0
    last = len(data)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if data[midpoint] == item:
            return print("Dokumen ditemukan:", data[midpoint])
        else:
            if item < data[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return "Data tidak ditemukan"
data = ['alreihan', 'reihanalex','reihanaul', 'sukaraihan', 'asep', '123asep', '983asepsukaraihan']
sorting(data)
pass

def main() :
    global lanjut
    print(f"{"="*10}Stadoc{"="*10}")
    print("1.Lihat tumpukan dokumen")
    print("2.Perbarui tumpukan dokumen")
    print("3.Hapus tumpukan dokumen")
    print("4.Tambah tumpukan dokumen")
    print("5.Urutkan tumpukan dokumen")
    print("6.Cari dokumen anda")
    print("7.Keluar")

    pilihan = int(input("Menu yang dipilih : "))
    match pilihan :
        case 1 :
            lihat()
        case 2 :
            perbarui()
        case 3 :
            hapus()
        case 4 :
            tambah()
        case 5 :
            sorting(data)
        case 6 :    
           inputan = input("Masukkan nama dokumen yang ingin dicari : ")
           print(cari(data, inputan))
        case 7 :
            lanjut = False
        case _ :
            if name == 'nt':
                c = system('cls')
                # return
            else:
                c = system('clear')
                # return

lanjut = True
while lanjut :

    main()
