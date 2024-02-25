from prettytable import PrettyTable

class TokoLego:
    def __init__(self):
        self.produk = {}

    def tambah_produk(self, id_produk, nama, kategori, harga, jumlah):
        if id_produk not in self.produk:
            self.produk[id_produk] = {'nama': nama, 'kategori': kategori, 'harga': harga, 'jumlah': jumlah}
            print(f"Produk '{nama}' berhasil ditambahkan.")
        else:
            print(f"Produk dengan ID {id_produk} sudah ada.")

    def lihat_produk(self):
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Kategori", "Harga", "Jumlah"]
        for id_produk, detail in self.produk.items():
            tabel.add_row([id_produk, detail['nama'], detail['kategori'], detail['harga'], detail['jumlah']])
        print(tabel)

    def ubah_produk(self, id_produk, kolom, nilai_baru):
        if id_produk in self.produk:
            if kolom in self.produk[id_produk]:
                self.produk[id_produk][kolom] = nilai_baru
                print(f"Produk {id_produk} berhasil diupdate.")
            else:
                print(f"Kolom '{kolom}' tidak ditemukan.")
        else:
            print(f"Produk dengan ID {id_produk} tidak ditemukan.")

    def hapus_produk(self, id_produk):
        if id_produk in self.produk:
            del self.produk[id_produk]
            print(f"Produk {id_produk} berhasil dihapus.")
        else:
            print(f"Produk dengan ID {id_produk} tidak ditemukan.")

    def menu_crud(self):
        # product dumpies
        self.tambah_produk(60248, 'police station (743 pieces)', 'LEGO City', 1.945, 100)
        self.tambah_produk(70668, 'LEGACY Jays Storm Fighter (460 pieces)', 'LEGO Ninjago', 1.850, 50)
        self.tambah_produk(43206, 'Cinderella and Prince Charmings Castle (365 pieces)', 'LEGO Disney princess', 1.599, 30)
        self.tambah_produk(43241, 'Rapunzels Tower & The Snuggly Duckling(345 pieces)', 'LEGO Disney princess', 1.599, 10)
        self.tambah_produk(76401, 'Hogwarts Courtyard: Sirius Rescue Building Kit (345 Pieces)', 'LEGO Harry Potter', 971 , 30)

        while True:
            print("===============================================")
            print(" selamat datang di Sistem manajemen Toko LEGO: ")
            print("===============================================")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Ubah Produk")
            print("4. Hapus Produk")
            print("5. Keluar")

            pilihan = input("Pilih Menu (1-5): ")

            if pilihan == '1':
                id_produk = int(input("Masukkan ID Produk: "))
                nama = input("Masukkan Nama Produk: ")
                kategori = input("Masukkan Kategori Produk: ")
                harga = float(input("Masukkan Harga Produk: "))
                jumlah = int(input("Masukkan Jumlah Produk: "))
                self.tambah_produk(id_produk, nama, kategori, harga, jumlah)

            elif pilihan == '2':
                self.lihat_produk()

            elif pilihan == '3':
                id_produk = int(input("Masukkan ID Produk yang ingin diubah: "))
                kolom = input("Masukkan Nama Kolom yang ingin diubah: ")
                nilai_baru = input("Masukkan Nilai Baru: ")
                self.ubah_produk(id_produk, kolom, nilai_baru)

            elif pilihan == '4':
                id_produk = int(input("Masukkan ID Produk yang ingin dihapus: "))
                self.hapus_produk(id_produk)

            elif pilihan == '5':
                print("Terima kasih! Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")


toko_lego = TokoLego()
toko_lego.menu_crud()
