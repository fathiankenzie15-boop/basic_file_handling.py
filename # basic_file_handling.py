# basic_file_handling.py

import os

NAMA_FILE = "daftar_buku.txt"

def bersihkan_layar():
    """Fungsi helper untuk membersihkan layar terminal agar rapi"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tulis_data_awal():
    """1. WRITE: Menulis data baru (menimpa file lama jika ada)"""
    print("\n" + "="*50)
    print(" [1] MODE WRITE (Menulis Data Awal)")
    print("="*50)
    
    data_buku = [
        "1. Pemrograman Python Dasar - Eko Kurniawan",
        "2. Algoritma dan Struktur Data - Rinaldi Munir",
        "3. Belajar Machine Learning - Andi"
    ]
    
    try:
        with open(NAMA_FILE, 'w', encoding='utf-8') as file:
            for buku in data_buku:
                file.write(buku + "\n")
        print(f"✅ Berhasil! {len(data_buku)} buku telah ditulis ke '{NAMA_FILE}'.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menulis: {e}")

def baca_data():
    """2. READ: Membaca isi file (Dengan penanganan NOT FOUND)"""
    print("\n" + "="*50)
    print(" [2] MODE READ (Membaca Data)")
    print("="*50)
    
    try:
        # Mode 'r' khusus untuk membaca
        with open(NAMA_FILE, 'r', encoding='utf-8') as file:
            isi = file.read()
            if isi.strip():
                print("📚 DAFTAR BUKU SAAT INI:\n")
                print(isi)
            else:
                print("⚠️ File ada, tetapi masih kosong.")
                
    except FileNotFoundError:
        # INI ADALAH PENANGANAN "NOT FOUND"
        print(f"❌ ERROR: File '{NAMA_FILE}' TIDAK DITEMUKAN (Not Found)!")
        print("💡 Solusi: Silakan pilih Menu 1 (Write) terlebih dahulu untuk membuat file.")

def tambah_dan_baca():
    """3. WRITE & READ (Append): Menambah data lalu langsung membacanya"""
    print("\n" + "="*50)
    print(" [3] MODE WRITE & READ (Tambah Data Baru)")
    print("="*50)
    
    judul = input("Masukkan Judul Buku : ")
    penulis = input("Masukkan Nama Penulis : ")
    data_baru = f"- {judul} oleh {penulis}"
    
    try:
        with open(NAMA_FILE, 'a+', encoding='utf-8') as file:
            # Langkah A: WRITE (Menambah data di baris baru)
            file.write(data_baru + "\n")
            print(f"\n✅ Buku '{judul}' berhasil ditambahkan!")
            
           
            file.seek(0)
            isi_terbaru = file.read()
            
            print("\n📚 DAFTAR BUKU TERBARU:")
            print(isi_terbaru)
            
    except FileNotFoundError:
        print(f"❌ ERROR: File '{NAMA_FILE}' TIDAK DITEMUKAN (Not Found)!")
        print("💡 Solusi: Jalankan Menu 1 terlebih dahulu.")

def hapus_buku():
    """4. UPDATE/DELETE: Menghapus buku tertentu (Read -> Filter -> Write)"""
    print("\n" + "="*50)
    print(" [4] MODE DELETE (Menghapus Buku)")
    print("="*50)
    
    keyword = input("Masukkan kata kunci judul buku yang ingin dihapus: ").lower()
    
    try:
        # Baca semua data 
        with open(NAMA_FILE, 'r', encoding='utf-8') as file:
            baris_buku = file.readlines()
            
        
        buku_disimpan = []
        ditemukan = False
        
        for baris in baris_buku:
            if keyword in baris.lower():
                ditemukan = True
                print(f"🗑️ Menghapus: {baris.strip()}")
            else:
                buku_disimpan.append(baris)
                
        if not ditemukan:
            print("⚠️ Buku dengan kata kunci tersebut tidak ditemukan.")
            return

        
        with open(NAMA_FILE, 'w', encoding='utf-8') as file:
            file.writelines(buku_disimpan)
            
        print("✅ Data berhasil diperbarui dan disimpan!")
        
    except FileNotFoundError:
        print(f"❌ ERROR: File '{NAMA_FILE}' TIDAK DITEMUKAN (Not Found)!")

def main():
    while True:
        bersihkan_layar()
        print("="*50)
        print("  PROGRAM FILE HANDLING: MANAJEMEN BUKU")
        print("="*50)
        print("1. Write          : Tulis data awal (Overwrite)")
        print("2. Read           : Baca semua data (Handle Not Found)")
        print("3. Write & Read   : Tambah buku baru & lihat hasilnya")
        print("4. Delete         : Hapus buku berdasarkan kata kunci")
        print("5. Keluar         : Tutup program")
        print("="*50)
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            tulis_data_awal()
        elif pilihan == '2':
            baca_data()
        elif pilihan == '3':
            tambah_dan_baca()
        elif pilihan == '4':
            hapus_buku()
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa! 👋\n")
            break
        else:
            print("\n⚠️ Pilihan tidak valid! Silakan masukkan angka 1-5.")
            
    
        input("\nTekan [Enter] untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()