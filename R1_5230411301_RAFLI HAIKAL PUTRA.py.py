class Pegawai:
    def __init__(self, nik, nama, alamat):  # Memperbaiki __init__ dari _init_
        self.nik = nik
        self.nama = nama
        self.alamat = alamat


class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):  # Memperbaiki __init__ dari _init_
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi


class Struk:
    def __init__(self, no_transaksi, nama_pegawai, no_transaksi_detail, nama_produk, jumlah_produk, total_harga):  # Memperbaiki __init__ dari _init_
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.no_transaksi_detail = no_transaksi_detail
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

    def print_struk(self):
        print("=== Struk Pembelian ===")
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Nama Pegawai: {self.nama_pegawai}")
        print(f"No Transaksi Detail: {self.no_transaksi_detail}")
        print(f"Nama Produk: {self.nama_produk}")
        print(f"Jumlah Produk: {self.jumlah_produk}")
        print(f"Total Harga: Rp {self.total_harga}")
        print("========================")


class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):  # Memperbaiki __init__ dari _init_
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

    def get_info(self):
        return f"Kode Produk: {self.kode_produk}, Nama Produk: {self.nama_produk}, Jenis Produk: {self.jenis_produk}"


class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):  # Memperbaiki __init__ dari _init_
        super().__init__(kode_produk, nama_snack, "Snack")  # Memperbaiki __init__ dari _init_
        self.harga = harga

    def get_info(self):  # Overriding method
        return f"Snack: {self.nama_produk}, Harga: Rp {self.harga}"


class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):  # Memperbaiki __init__ dari _init_
        super().__init__(kode_produk, nama_makanan, "Makanan")  # Memperbaiki __init__ dari _init_
        self.harga = harga

    def get_info(self):  # Overriding method
        return f"Makanan: {self.nama_produk}, Harga: Rp {self.harga}"


class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):  # Memperbaiki __init__ dari _init_
        super().__init__(kode_produk, nama_minuman, "Minuman")  # Memperbaiki __init__ dari _init_
        self.harga = harga

    def get_info(self):  # Overriding method
        return f"Minuman: {self.nama_produk}, Harga: Rp {self.harga}"


# Contoh penggunaan
pegawai = Pegawai("123", "Budi", "Jl. Merdeka")
transaksi = Transaksi("001", "Detail transaksi")
struk = Struk("001", pegawai.nama, transaksi.no_transaksi, "Nasi Goreng", 3, 60000)
snack = Snack("S001", "Keripik", 5000)
makanan = Makanan("M001", "Nasi Goreng", 20000)
minuman = Minuman("D001", "Teh Manis", 7000)

# Output informasi
print(snack.get_info())
print(makanan.get_info())
print(minuman.get_info())
print()
struk.print_struk()