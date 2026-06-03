import sqlite3

koneksi = sqlite3.connect("buku_kontak.db")
kursor = koneksi.cursor()

kursor.execute("""
   CREATE TABLE IF NOT EXISTS kontak (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nama    TEXT NOT NULL,
        telepon TEXT,
        email   TEXT
    )
""")

def tambah_kontak(nama, telepon, email):
    kursor.execute("INSERT INTO kontak (nama, telepon, email) VALUES (?, ?, ?)",
                   (nama, telepon, email))
    koneksi.commit()
    print(f"kontak '{nama}' berhasil di tambahkan!")
    
def lihat_semua_kontak():
    kursor.execute("SELECT * FROM KONTAK")
    semua = kursor.fetchall()
    if not semua:
        print("belum ada kontak tersimpan.")
    else:
        print("\n---Daftar kontak ---")
        for baris in semua:
            print(f"ID:{baris[0]} | Nama:{baris[1]} | HP:{baris[2]} | Email:{baris[3]}")

def cari_by_nomor(nomor):
    kursor.execute("SELECT * FROM kontak WHERE telepon = ?", (nomor,))
    hasil = kursor.fetchone()
    if hasil:
        print("\n--- kontak Ditemukan ---")
        print(f"NAMA     : {hasil[1]}")
        print(f"Telepon  : {hasil[2]}")
        print(f"Email    : {hasil[3]}")
    else:
        print(f"Nomor '{nomor}' tidak di temukan di buku kontak.")

while True:
    print("\n=== BUKU KONTAK ===")
    print("1. Tambah kontak")
    print("2. Lihat semua kontak")
    print("3. Cari kontak by nomor hp")
    print("4. keluar")
    
    pilihan = input("Pilihan menu (1/2/3/4): ")
    
    if pilihan == "1":
        nama    = input("Nama    : ")
        telepon = input("TELEPON : ")
        email   = input("Email   : ")
        tambah_kontak(nama, telepon, email)
        
    elif pilihan == "2":
        lihat_semua_kontak()
        
    elif pilihan == "3":
        nomor   = input("masukan nomor hp yang di cari: ")
        cari_by_nomor(nomor)
        
    elif pilihan == "4":
        print("sampai jumpa!")
        koneksi.close()
        break
    
    else:
        print("pilihan tidak valid, coba lagi !")
