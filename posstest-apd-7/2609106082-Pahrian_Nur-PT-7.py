import os


users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "pahri": {"password": "123", "role": "Pengguna Biasa"},
    "sari": {"password": "123", "role": "Pengguna Biasa"}
}

daftar_kondisi = {"1": "Mulus", "2": "Baik", "3": "Minus"}

data_hp = {
    1: {"penjual": "budi", "merk": "Samsung", "tipe": "Galaxy A52",
        "kondisi": "Baik", "harga": 2500000, "status": "Tersedia"},
    2: {"penjual": "sari", "merk": "Xiaomi", "tipe": "Redmi Note 10",
        "kondisi": "Mulus", "harga": 1800000, "status": "Tersedia"}
}
id_terakhir = 2

transaksi = {}
no_transaksi = 0


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")



def tampil_daftar_hp(kata_cari):
    print("-" * 78)
    print("ID | Penjual | Merk | Tipe | Kondisi | Harga | Status")
    print("-" * 78)
    jumlah = 0
    for id_hp, h in data_hp.items():
        if kata_cari in h["merk"].lower():
            print(id_hp, "|", h["penjual"], "|", h["merk"], "|",
                  h["tipe"], "|", h["kondisi"], "| Rp",
                  format_rupiah(h["harga"]), "|", h["status"])
            jumlah += 1
    if jumlah == 0:
        print("Data HP tidak ditemukan.")
    else:
        print("-" * 78)
        print("Jumlah data:", jumlah)



def cek_angka(teks):
    if teks == "":
        return False
    for huruf in teks:
        if huruf not in "0123456789":
            return False
    return True



def format_rupiah(angka):
    if angka < 1000:
        return str(angka)
    sisa = str(angka % 1000)
    while len(sisa) < 3:
        sisa = "0" + sisa
    return format_rupiah(angka // 1000) + "." + sisa



def hitung_hp_tersedia():
    jumlah_tersedia = 0
    for id_hp, h in data_hp.items():
        if h["status"] == "Tersedia":
            jumlah_tersedia += 1
    return jumlah_tersedia



def buat_nomor_transaksi():
    global no_transaksi
    no_transaksi += 1
    return no_transaksi


program_jalan = True

while program_jalan:
    bersihkan_layar()
    print("=" * 42)
    print("      TOKO JUAL BELI HP BEKAS")
    print("=" * 42)
    print("HP tersedia saat ini :", hitung_hp_tersedia())
    print("-" * 42)
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar")
    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        percobaan = 0
        sudah_login = False
        nama_aktif = ""
        role_aktif = ""

        while percobaan < 3:
            bersihkan_layar()
            print("=== LOGIN ===")
            username = input("Username : ").strip()
            password = input("Password : ").strip()

            if username in users and users[username]["password"] == password:
                sudah_login = True
                nama_aktif = username
                role_aktif = users[username]["role"]

            if sudah_login:
                print("Login Berhasil")
                input("Tekan Enter untuk lanjut...")
                break
            else:
                percobaan += 1
                print("Login Gagal. Sisa percobaan:", 3 - percobaan)
                input("Tekan Enter untuk lanjut...")

        if percobaan == 3 and not sudah_login:
            print("Percobaan habis. Program berakhir.")
            program_jalan = False

        while sudah_login:
            bersihkan_layar()
            print("=" * 42)
            print("Halo,", nama_aktif, "(" + role_aktif + ")")
            print("=" * 42)
            print("[1] Jual HP              (Create)")
            print("[2] Lihat / Cari HP      (Read)")
            print("[3] Ubah Data HP         (Update)")
            print("[4] Hapus HP             (Delete)")
            if role_aktif == "Admin":
                print("[5] Kelola Pengguna")
                print("[6] Riwayat Semua Transaksi")
            else:
                print("[5] Beli HP")
                print("[6] Riwayat Transaksi Saya")
            print("[0] Logout")
            menu = input("Pilih menu: ").strip()

           
            if menu == "1":
                bersihkan_layar()
                print("=== JUAL HP ===")
                try:
                    merk = input("Merk          : ").strip()
                    tipe = input("Tipe          : ").strip()
                    print("Kondisi: [1] Mulus  [2] Baik  [3] Minus")
                    kondisi = input("Pilih kondisi : ").strip()
                    harga = input("Harga (Rp)    : ").strip()

                    if merk == "" or tipe == "":
                        raise ValueError("Merk dan tipe tidak boleh kosong!")
                    if kondisi not in daftar_kondisi:
                        raise ValueError("Kondisi harus 1, 2, atau 3!")
                    if not cek_angka(harga):
                        raise ValueError("Harga harus berupa angka bulat positif!")
                    harga_angka = int(harga)
                    if harga_angka <= 0:
                        raise ValueError("Harga harus lebih dari 0!")
                except ValueError as pesan_error:
                    print("Error:", pesan_error)
                else:
                    id_terakhir += 1
                    data_hp[id_terakhir] = {
                        "penjual": nama_aktif,
                        "merk": merk,
                        "tipe": tipe,
                        "kondisi": daftar_kondisi[kondisi],
                        "harga": harga_angka,
                        "status": "Tersedia"
                    }
                    nomor_baru = buat_nomor_transaksi()
                    transaksi[nomor_baru] = {
                        "id_hp": id_terakhir,
                        "nama_hp": merk + " " + tipe,
                        "penjual": nama_aktif,
                        "pembeli": "-",
                        "harga": harga_angka,
                        "jenis": "Dijual"
                    }
                    print("HP berhasil didaftarkan dengan ID", id_terakhir)
                finally:
                    input("Tekan Enter untuk kembali...")

           
            elif menu == "2":
                bersihkan_layar()
                print("=== LIHAT / CARI HP ===")
                print("[1] Tampilkan semua")
                print("[2] Cari berdasarkan merk")
                try:
                    sub = input("Pilih: ").strip()
                    if sub != "1" and sub != "2":
                        raise ValueError("Pilihan tidak tersedia!")
                    kata = ""
                    if sub == "2":
                        kata = input("Masukkan merk : ").lower().strip()
                except ValueError as pesan_error:
                    print("Error:", pesan_error)
                else:
                    tampil_daftar_hp(kata)
                finally:
                    input("Tekan Enter untuk kembali...")

            
            elif menu == "3":
                bersihkan_layar()
                print("=== UBAH DATA HP ===")
                try:
                    id_input = input("Masukkan ID HP yang ingin diubah : ").strip()
                    if not cek_angka(id_input):
                        raise ValueError("ID harus berupa angka!")
                    id_hp = int(id_input)
                    if role_aktif != "Admin" and data_hp[id_hp]["penjual"] != nama_aktif:
                        raise ValueError("Anda hanya boleh mengubah HP milik sendiri!")
                    if data_hp[id_hp]["status"] == "Terjual":
                        raise ValueError("HP yang sudah terjual tidak bisa diubah!")

                    print("Data lama:", data_hp[id_hp]["merk"], data_hp[id_hp]["tipe"],
                          "|", data_hp[id_hp]["kondisi"], "| Rp",
                          format_rupiah(data_hp[id_hp]["harga"]))
                    print("(Kosongkan input jika tidak ingin mengubah)")
                    merk_baru = input("Merk baru    : ").strip()
                    tipe_baru = input("Tipe baru    : ").strip()
                    print("Kondisi: [1] Mulus  [2] Baik  [3] Minus")
                    kondisi_baru = input("Kondisi baru : ").strip()
                    harga_baru = input("Harga baru   : ").strip()

                    if kondisi_baru != "" and kondisi_baru not in daftar_kondisi:
                        raise ValueError("Kondisi harus 1, 2, atau 3!")
                    if harga_baru != "":
                        if not cek_angka(harga_baru):
                            raise ValueError("Harga harus berupa angka bulat positif!")
                        if int(harga_baru) <= 0:
                            raise ValueError("Harga harus lebih dari 0!")
                except ValueError as pesan_error:
                    print("Error:", pesan_error)
                except KeyError:
                    print("Error: ID tidak ditemukan!")
                else:
                    if merk_baru != "":
                        data_hp[id_hp]["merk"] = merk_baru
                    if tipe_baru != "":
                        data_hp[id_hp]["tipe"] = tipe_baru
                    if kondisi_baru != "":
                        data_hp[id_hp]["kondisi"] = daftar_kondisi[kondisi_baru]
                    if harga_baru != "":
                        data_hp[id_hp]["harga"] = int(harga_baru)
                    print("Data HP berhasil diubah.")
                finally:
                    input("Tekan Enter untuk kembali...")

         
            elif menu == "4":
                bersihkan_layar()
                print("=== HAPUS HP ===")
                try:
                    id_input = input("Masukkan ID HP yang ingin dihapus : ").strip()
                    if not cek_angka(id_input):
                        raise ValueError("ID harus berupa angka!")
                    id_hp = int(id_input)
                    if role_aktif != "Admin" and data_hp[id_hp]["penjual"] != nama_aktif:
                        raise ValueError("Anda hanya boleh menghapus HP milik sendiri!")

                    yakin = input("Yakin ingin menghapus? (Y/T) : ").upper().strip()
                    if yakin != "Y" and yakin != "T":
                        raise ValueError("Pilihan harus Y atau T!")
                except ValueError as pesan_error:
                    print("Error:", pesan_error)
                except KeyError:
                    print("Error: ID tidak ditemukan!")
                else:
                    if yakin == "Y":
                        data_hp_baru = {}
                        for id_lama, h in data_hp.items():
                            if id_lama != id_hp:
                                data_hp_baru[id_lama] = h
                        data_hp = data_hp_baru
                        print("Data HP berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                finally:
                    input("Tekan Enter untuk kembali...")

            elif menu == "5" and role_aktif == "Admin":
                bersihkan_layar()
                print("=== KELOLA PENGGUNA ===")
                print("No | Username | Role")
                print("-" * 35)
                nomor = 1
                for nama, info in users.items():
                    print(nomor, "|", nama, "|", info["role"])
                    nomor += 1
                print("-" * 35)
                try:
                    hapus = input("Username yang ingin dihapus (kosong = batal) : ").strip()
                    if hapus != "":
                        if users[hapus]["role"] == "Admin":
                            raise ValueError("Akun Admin tidak boleh dihapus!")
                except ValueError as pesan_error:
                    print("Error:", pesan_error)
                except KeyError:
                    print("Error: Username tidak ditemukan!")
                else:
                    if hapus != "":
                        users_baru = {}
                        for nama, info in users.items():
                            if nama != hapus:
                                users_baru[nama] = info
                        users = users_baru

                      
                        data_hp_baru = {}
                        for id_lama, h in data_hp.items():
                            if h["penjual"] != hapus:
                                data_hp_baru[id_lama] = h
                        data_hp = data_hp_baru
                        print("Pengguna dan HP miliknya berhasil dihapus.")
                finally:
                    input("Tekan Enter untuk kembali...")

          
            elif menu == "5" and role_aktif != "Admin":
                bersihkan_layar()
                print("=== BELI HP ===")
                print("Daftar HP yang tersedia:")
                print("-" * 70)
                ada = False
                for id_hp, h in data_hp.items():
                    if h["status"] == "Tersedia" and h["penjual"] != nama_aktif:
                        print(id_hp, "|", h["penjual"], "|", h["merk"], h["tipe"],
                              "|", h["kondisi"], "| Rp", format_rupiah(h["harga"]))
                        ada = True
                print("-" * 70)

                if not ada:
                    print("Belum ada HP yang bisa dibeli.")
                else:
                    try:
                        id_input = input("Masukkan ID HP yang ingin dibeli : ").strip()
                        if not cek_angka(id_input):
                            raise ValueError("ID harus berupa angka!")
                        id_hp = int(id_input)
                        if data_hp[id_hp]["penjual"] == nama_aktif:
                            raise ValueError("Anda tidak bisa membeli HP sendiri!")
                        if data_hp[id_hp]["status"] == "Terjual":
                            raise ValueError("HP sudah terjual!")

                        yakin = input("Yakin ingin membeli? (Y/T) : ").upper().strip()
                        if yakin != "Y" and yakin != "T":
                            raise ValueError("Pilihan harus Y atau T!")
                    except ValueError as pesan_error:
                        print("Error:", pesan_error)
                    except KeyError:
                        print("Error: ID tidak ditemukan!")
                    else:
                        if yakin == "Y":
                            data_hp[id_hp]["status"] = "Terjual"
                            nomor_baru = buat_nomor_transaksi()
                            transaksi[nomor_baru] = {
                                "id_hp": id_hp,
                                "nama_hp": data_hp[id_hp]["merk"] + " " + data_hp[id_hp]["tipe"],
                                "penjual": data_hp[id_hp]["penjual"],
                                "pembeli": nama_aktif,
                                "harga": data_hp[id_hp]["harga"],
                                "jenis": "Terjual"
                            }
                            print("Pembelian berhasil!")
                        else:
                            print("Pembelian dibatalkan.")
                input("Tekan Enter untuk kembali...")

         
            elif menu == "6":
                bersihkan_layar()
                print("=== RIWAYAT TRANSAKSI ===")
                print("-" * 70)
                print("ID HP | Nama HP | Penjual | Pembeli | Harga | Jenis")
                print("-" * 70)
                jumlah = 0
                for no, t in transaksi.items():
                    if role_aktif == "Admin" or t["penjual"] == nama_aktif or t["pembeli"] == nama_aktif:
                        print(t["id_hp"], "|", t["nama_hp"], "|", t["penjual"], "|",
                              t["pembeli"], "| Rp", format_rupiah(t["harga"]), "|", t["jenis"])
                        jumlah += 1
                if jumlah == 0:
                    print("Belum ada transaksi.")
                input("Tekan Enter untuk kembali...")

            elif menu == "0":
                sudah_login = False

            else:
                print("Error: Menu tidak tersedia!")
                input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        bersihkan_layar()
        print("=== REGISTER ===")
        try:
            user_baru = input("Username baru : ").strip()
            pass_baru = input("Password baru (min. 3 karakter) : ").strip()

            if user_baru == "" or " " in user_baru:
                raise ValueError("Username tidak boleh kosong atau mengandung spasi!")
            if user_baru in users:
                raise ValueError("Username sudah dipakai!")
            if len(pass_baru) < 3:
                raise ValueError("Password minimal 3 karakter!")
        except ValueError as pesan_error:
            print("Error:", pesan_error)
        else:
            users[user_baru] = {"password": pass_baru, "role": "Pengguna Biasa"}
            print("Registrasi berhasil! Silakan login.")
        finally:
            input("Tekan Enter untuk kembali...")

    elif pilih == "3":
        print("Terima kasih. Program selesai.")
        program_jalan = False

    else:
        print("Error: Menu tidak tersedia!")
        input("Tekan Enter untuk kembali...")