import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# List untuk menyimpan data transaksi laundry
transaksi_list = []

# Fungsi untuk menambah transaksi
def tambah_transaksi():
    try:
        # Ambil data dari inputan
        nama_pelanggan = entry_nama.get()
        jenis_pakaian = combo_jenis.get()
        berat = float(entry_berat.get())
        harga_per_kg = harga_jenis[jenis_pakaian]
        total_harga = harga_per_kg * berat
        
        # Menyimpan transaksi ke dalam list
        transaksi = {
            'ID': len(transaksi_list) + 1,
            'Nama Pelanggan': nama_pelanggan,
            'Jenis Pakaian': jenis_pakaian,
            'Berat (kg)': berat,
            'Harga (IDR)': total_harga,
            'Status': 'Belum Selesai'
        }
        transaksi_list.append(transaksi)

        # Tambahkan transaksi ke tabel
        tampilkan_transaksi()

        # Reset input form
        entry_nama.delete(0, tk.END)
        entry_berat.delete(0, tk.END)

        messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan!")
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan angka yang valid untuk berat.")

# Fungsi untuk menampilkan transaksi di tabel
def tampilkan_transaksi():
    for row in treeview.get_children():
        treeview.delete(row)
    
    for transaksi in transaksi_list:
        treeview.insert("", tk.END, values=(transaksi['ID'], transaksi['Nama Pelanggan'], transaksi['Jenis Pakaian'],
                                           transaksi['Berat (kg)'], transaksi['Harga (IDR)'], transaksi['Status']))

# Fungsi untuk mencari transaksi berdasarkan ID
def cari_transaksi():
    search_id = entry_search_id.get()
    if not search_id.isdigit():
        messagebox.showerror("Input Error", "ID Transaksi harus berupa angka.")
        return
    
    search_id = int(search_id)
    found = False
    for transaksi in transaksi_list:
        if transaksi['ID'] == search_id:
            found = True
            treeview.delete(*treeview.get_children())
            treeview.insert("", tk.END, values=(transaksi['ID'], transaksi['Nama Pelanggan'], transaksi['Jenis Pakaian'],
                                               transaksi['Berat (kg)'], transaksi['Harga (IDR)'], transaksi['Status']))
            break
    
    if not found:
        messagebox.showwarning("Tidak Ditemukan", "Transaksi dengan ID tersebut tidak ditemukan.")

# Fungsi untuk mengupdate status transaksi menjadi selesai
def update_status():
    try:
        selected_item = treeview.selection()[0]
        transaksi_id = treeview.item(selected_item, 'values')[0]
        for transaksi in transaksi_list:
            if transaksi['ID'] == transaksi_id:
                transaksi['Status'] = 'Selesai'
                break
        tampilkan_transaksi()
        messagebox.showinfo("Sukses", "Status transaksi berhasil diperbarui menjadi Selesai.")
    except IndexError:
        messagebox.showwarning("Peringatan", "Silakan pilih transaksi yang ingin diupdate.")

# Definisi harga per kg untuk jenis pakaian
harga_jenis = {
    "Kaos": 15000,
    "Celana": 20000,
    "Jaket": 25000,
    "Kemeja": 18000
}

# Membuat root window
root = tk.Tk()
root.title("Sistem Manajemen Laundry Baju")

# Form Input Transaksi
frame_input = tk.Frame(root)
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_nama = tk.Label(frame_input, text="Nama Pelanggan:")
label_nama.grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

label_jenis = tk.Label(frame_input, text="Jenis Pakaian:")
label_jenis.grid(row=1, column=0, padx=5, pady=5)
combo_jenis = ttk.Combobox(frame_input, values=["Kaos", "Celana", "Jaket", "Kemeja"])
combo_jenis.grid(row=1, column=1, padx=5, pady=5)
combo_jenis.set("Kaos")

label_berat = tk.Label(frame_input, text="Berat (kg):")
label_berat.grid(row=2, column=0, padx=5, pady=5)
entry_berat = tk.Entry(frame_input)
entry_berat.grid(row=2, column=1, padx=5, pady=5)

button_tambah = tk.Button(frame_input, text="Tambah Transaksi", command=tambah_transaksi)
button_tambah.grid(row=3, column=0, columnspan=2, pady=10)

# Pencarian Transaksi
frame_search = tk.Frame(root)
frame_search.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_search_id = tk.Label(frame_search, text="Cari ID Transaksi:")
label_search_id.grid(row=0, column=0, padx=5, pady=5)
entry_search_id = tk.Entry(frame_search)
entry_search_id.grid(row=0, column=1, padx=5, pady=5)

button_cari = tk.Button(frame_search, text="Cari", command=cari_transaksi)
button_cari.grid(row=0, column=2, padx=5, pady=5)

# Tabel Daftar Transaksi
frame_tabel = tk.Frame(root)
frame_tabel.grid(row=2, column=0, padx=10, pady=10)

columns = ("ID", "Nama Pelanggan", "Jenis Pakaian", "Berat (kg)", "Harga (IDR)", "Status")
treeview = ttk.Treeview(frame_tabel, columns=columns, show="headings")
treeview.grid(row=0, column=0)

for col in columns:
    treeview.heading(col, text=col)

# Tombol Update Status
button_update_status = tk.Button(root, text="Update Status Selesai", command=update_status)
button_update_status.grid(row=3, column=0, pady=10)

# Menjalankan aplikasi
root.mainloop()
