from os import system, name

# Fungsi untuk melihat isi tumpukan dokumen
def lihat() :
    pass

# Fungsi untuk menghapus dokumen dari tumpukan dokumen
def hapus() :
    pass

# Fungsi untuk memperbarui isi dokumen dari tumpukan dokumen
def perbarui() :
    pass

# Fungsi untuk menambah dokumen ke tumpukan dokumen
def tambah() :
    pass

# Fungsi untuk mencari dokumen di dalam tumpukan dokumen
def cari() :
    pass

def main() :
    global lanjut
    print(f"{"="*10}Stadoc{"="*10}")
    print("1.Lihat tumpukan dokumen")
    print("2.Perbarui tumpukan dokumen")
    print("3.Hapus tumpukan dokumen")
    print("4.Tambah tumpukan dokumen")
    print("5.Keluar")

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