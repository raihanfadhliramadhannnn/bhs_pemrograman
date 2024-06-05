from datetime import date

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def set_harga(self, new_harga):
        self.harga = new_harga

    def get_harga(self):
        return self.harga

class Order:
    def __init__(self, order_id, produk, jumlah):
        self.order_id = order_id
        self.produk = produk
        self.jumlah = jumlah
        self.total = produk.get_harga() * jumlah
        self.status = "Pending"
        self.tanggal = date.today()

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return (f"Order ID: {self.order_id}, Produk: {self.produk.nama}, "
                f"Jumlah: {self.jumlah}, Total: {self.total}, Status: {self.status}, Tanggal: {self.tanggal}")

class Pelanggan:
    def __init__(self, pelanggan_id, nama, kontak):
        self.pelanggan_id = pelanggan_id
        self.nama = nama
        self.kontak = kontak
        self.riwayat_order = []

    def tambah_order(self, order):
        self.riwayat_order.append(order)

    def __repr__(self):
        return f"Pelanggan ID: {self.pelanggan_id}, Nama: {self.nama}, Kontak: {self.kontak}, Riwayat: {self.riwayat_order}"

class Penjualan:
    def __init__(self):
        self.orders = []

    def tambah_penjualan(self, order):
        self.orders.append(order)

    def get_total_pemasukan(self):
        total_pemasukan = sum(order.total for order in self.orders)
        return total_pemasukan

    def __repr__(self):
        return f"Penjualan: {self.orders}"

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n=== Aplikasi Kasir Laundry ===")
    print("1. Tambah Produk")
    print("2. Tambah Pelanggan")
    print("3. Tambah Order")
    print("4. Update Status Order")
    print("5. Tampilkan Total Pemasukan")
    print("6. Tampilkan Data Pelanggan")
    print("7. Keluar")
    pilihan = input("Pilih menu: ")
    return pilihan

# Inisialisasi data
produk_list = []
pelanggan_list = []
penjualan = Penjualan()

# Fungsi untuk menemukan produk berdasarkan nama
def find_produk(nama):
    for produk in produk_list:
        if produk.nama == nama:
            return produk
    return None

# Fungsi untuk menemukan pelanggan berdasarkan ID
def find_pelanggan(pelanggan_id):
    for pelanggan in pelanggan_list:
        if pelanggan.pelanggan_id == pelanggan_id:
            return pelanggan
    return None

# Main loop aplikasi
while True:
    pilihan = tampilkan_menu()
    
    if pilihan == '1':
        # Tambah Produk
        nama = input("Nama Produk: ")
        harga = float(input("Harga Produk: "))
        produk = Produk(nama, harga)
        produk_list.append(produk)
        print("Produk berhasil ditambahkan.")
    
    elif pilihan == '2':
        # Tambah Pelanggan
        pelanggan_id = int(input("ID Pelanggan: "))
        nama = input("Nama Pelanggan: ")
        kontak = input("Kontak Pelanggan: ")
        pelanggan = Pelanggan(pelanggan_id, nama, kontak)
        pelanggan_list.append(pelanggan)
        print("Pelanggan berhasil ditambahkan.")
    
    elif pilihan == '3':
        # Tambah Order
        pelanggan_id = int(input("ID Pelanggan: "))
        pelanggan = find_pelanggan(pelanggan_id)
        if pelanggan:
            produk_nama = input("Nama Produk: ")
            produk = find_produk(produk_nama)
            if produk:
                jumlah = int(input("Jumlah: "))
                order_id = len(penjualan.orders) + 1
                order = Order(order_id, produk, jumlah)
                pelanggan.tambah_order(order)
                penjualan.tambah_penjualan(order)
