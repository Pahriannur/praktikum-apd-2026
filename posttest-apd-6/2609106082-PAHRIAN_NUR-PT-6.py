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

program_jalan = True

while program_jalan:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 42)
    print("      TOKO JUAL BELI HP BEKAS")
    print("=" * 42)
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
            os.system("cls" if os.name == "nt" else "clear")
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
            os.system("cls" if os.name == "nt" else "clear")
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
                os.system("cls" if os.name == "nt" else "clear")
                print("=== JUAL HP ===")
                merk = input("Merk          : ").strip()
                tipe = input("Tipe          : ").strip()
                print("Kondisi: [1] Mulus  [2] Baik  [3] Minus")
                kondisi = input("Pilih kondisi : ").strip()
                harga = input("Harga (Rp)    : ").strip()

                harga_angka = True
                if harga == "":
                    harga_angka = False
                for huruf in harga:
                    if huruf not in "0123456789":
                        harga_angka = False

                if merk == "" or tipe == "":
                    print("Error: Merk dan tipe tidak boleh kosong!")
                elif kondisi not in daftar_kondisi:
                    print("Error: Kondisi harus 1, 2, atau 3!")
                elif not harga_angka:
                    print("Error: Harga harus berupa angka bulat positif!")
                elif int(harga) <= 0:
                    print("Error: Harga harus lebih dari 0!")
                else:
                    id_terakhir += 1
                    data_hp[id_terakhir] = {
                        "penjual": nama_aktif,
                        "merk": merk,
                        "tipe": tipe,
                        "kondisi": daftar_kondisi[kondisi],
                        "harga": int(harga),
                        "status": "Tersedia"
                    }
                    no_transaksi += 1
                    transaksi[no_transaksi] = {
               -         "id_hp": id_terakhir,
                        "nama_hp": merk + " " + tipe,
                        "penjual": nama_aktif,
                        "pembeli": "-",
                        "harga": int(harga),
                        "jenis": "Dijual"
                    }
                    print("HP berhasil didaftarkan dengan ID", id_terakhir)
                input("Tekan Enter untuk kembali...")

            elif menu == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== LIHAT / CARI HP ===")
                print("[1] Tampilkan semua")
                print("[2] Cari berdasarkan merk")
                sub = input("Pilih: ").strip()

                if sub != "1" and sub != "2":
                    print("Error: Pilihan tidak tersedia!")
                else:
                    kata = ""
                    if sub == "2":
                        kata = input("Masukkan merk : ").lower().strip()

                    print("-" * 78)
                    print("ID | Penjual | Merk | Tipe | Kondisi | Harga | Status")
                    print("-" * 78)
                    jumlah = 0
                    for id_hp, h in data_hp.items():
                        if kata in h["merk"].lower():
                            print(id_hp, "|", h["penjual"], "|", h["merk"], "|",
                                  h["tipe"], "|", h["kondisi"], "| Rp",
                                  h["harga"], "|", h["status"])
                            jumlah += 1
                    if jumlah == 0:
                        print("Data HP tidak ditemukan.")
                    else:
                        print("-" * 78)
                        print("Jumlah data:", jumlah)
                input("Tekan Enter untuk kembali...")

            elif menu == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== UBAH DATA HP ===")
                id_input = input("Masukkan ID HP yang ingin diubah : ").strip()

                # cek ID huruf per huruf
                id_angka = True
                if id_input == "":
                    id_angka = False
                for huruf in id_input:
                    if huruf not in "0123456789":
                        id_angka = False

                if not id_angka:
                    print("Error: ID harus berupa angka!")
                elif int(id_input) not in data_hp:
                    print("Error: ID tidak ditemukan!")
                else:
                    id_hp = int(id_input)
                    if role_aktif != "Admin" and data_hp[id_hp]["penjual"] != nama_aktif:
                        print("Error: Anda hanya boleh mengubah HP milik sendiri!")
                    elif data_hp[id_hp]["status"] == "Terjual":
                        print("Error: HP yang sudah terjual tidak bisa diubah!")
                    else:
                        print("Data lama:", data_hp[id_hp]["merk"], data_hp[id_hp]["tipe"],
                              "|", data_hp[id_hp]["kondisi"], "| Rp", data_hp[id_hp]["harga"])
                        print("(Kosongkan input jika tidak ingin mengubah)")
                        merk_baru = input("Merk baru    : ").strip()
                        tipe_baru = input("Tipe baru    : ").strip()
                        print("Kondisi: [1] Mulus  [2] Baik  [3] Minus")
                        kondisi_baru = input("Kondisi baru : ").strip()
                        harga_baru = input("Harga baru   : ").strip()

                        # cek harga baru huruf per huruf
                        harga_angka = True
                        for huruf in harga_baru:
                            if huruf not in "0123456789":
                                harga_angka = False

                        if kondisi_baru != "" and kondisi_baru not in daftar_kondisi:
                            print("Error: Kondisi harus 1, 2, atau 3!")
                        elif not harga_angka:
                            print("Error: Harga harus berupa angka bulat positif!")
                        elif harga_baru != "" and int(harga_baru) <= 0:
                            print("Error: Harga harus lebih dari 0!")
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
                input("Tekan Enter untuk kembali...")
                
            elif menu == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== HAPUS HP ===")
                id_input = input("Masukkan ID HP yang ingin dihapus : ").strip()

                id_angka = True
                if id_input == "":
                    id_angka = False
                for huruf in id_input:
                    if huruf not in "0123456789":
                        id_angka = False

                if not id_angka:
                    print("Error: ID harus berupa angka!")
                elif int(id_input) not in data_hp:
                    print("Error: ID tidak ditemukan!")
                else:
                    id_hp = int(id_input)
                    if role_aktif != "Admin" and data_hp[id_hp]["penjual"] != nama_aktif:
                        print("Error: Anda hanya boleh menghapus HP milik sendiri!")
                    else:
                        yakin = input("Yakin ingin menghapus? (Y/T) : ").upper().strip()
                        if yakin == "Y":
                            del data_hp[id_hp]
                            print("Data HP berhasil dihapus.")
                        elif yakin == "T":
                            print("Penghapusan dibatalkan.")
                        else:
                            print("Error: Pilihan harus Y atau T!")
                input("Tekan Enter untuk kembali...")

            elif menu == "5" and role_aktif == "Admin":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== KELOLA PENGGUNA ===")
                print("No | Username | Role")
                print("-" * 35)
                nomor = 1
                for nama, info in users.items():
                    print(nomor, "|", nama, "|", info["role"])
                    nomor += 1
                print("-" * 35)
                hapus = input("Username yang ingin dihapus (kosong = batal) : ").strip()

                if hapus != "":
                    if hapus not in users:
                        print("Error: Username tidak ditemukan!")
                    elif users[hapus]["role"] == "Admin":
                        print("Error: Akun Admin tidak boleh dihapus!")
                    else:
                        del users[hapus]

                        # hapus semua HP milik pengguna tersebut
                        id_dihapus = []
                        for id_hp, h in data_hp.items():
                            if h["penjual"] == hapus:
                                id_dihapus.append(id_hp)
                        for id_hp in id_dihapus:
                            del data_hp[id_hp]
                        print("Pengguna dan HP miliknya berhasil dihapus.")
                input("Tekan Enter untuk kembali...")

            elif menu == "5" and role_aktif != "Admin":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== BELI HP ===")
                print("Daftar HP yang tersedia:")
                print("-" * 70)
                ada = False
                for id_hp, h in data_hp.items():
                    if h["status"] == "Tersedia" and h["penjual"] != nama_aktif:
                        print(id_hp, "|", h["penjual"], "|", h["merk"], h["tipe"],
                              "|", h["kondisi"], "| Rp", h["harga"])
                        ada = True
                print("-" * 70)

                if not ada:
                    print("Belum ada HP yang bisa dibeli.")
                else:
                    id_input = input("Masukkan ID HP yang ingin dibeli : ").strip()

                    id_angka = True
                    if id_input == "":
                        id_angka = False
                    for huruf in id_input:
                        if huruf not in "0123456789":
                            id_angka = False

                    if not id_angka:
                        print("Error: ID harus berupa angka!")
                    elif int(id_input) not in data_hp:
                        print("Error: ID tidak ditemukan!")
                    else:
                        id_hp = int(id_input)
                        if data_hp[id_hp]["penjual"] == nama_aktif:
                            print("Error: Anda tidak bisa membeli HP sendiri!")
                        elif data_hp[id_hp]["status"] == "Terjual":
                            print("Error: HP sudah terjual!")
                        else:
                            yakin = input("Yakin ingin membeli? (Y/T) : ").upper().strip()
                            if yakin == "Y":
                                data_hp[id_hp]["status"] = "Terjual"
                                no_transaksi += 1
                                transaksi[no_transaksi] = {
                                    "id_hp": id_hp,
                                    "nama_hp": data_hp[id_hp]["merk"] + " " + data_hp[id_hp]["tipe"],
                                    "penjual": data_hp[id_hp]["penjual"],
                                    "pembeli": nama_aktif,
                                    "harga": data_hp[id_hp]["harga"],
                                    "jenis": "Terjual"
                                }
                                print("Pembelian berhasil!")
                            elif yakin == "T":
                                print("Pembelian dibatalkan.")
                            else:
                                print("Error: Pilihan harus Y atau T!")
                input("Tekan Enter untuk kembali...")

            elif menu == "6":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== RIWAYAT TRANSAKSI ===")
                print("-" * 70)
                print("ID HP | Nama HP | Penjual | Pembeli | Harga | Jenis")
                print("-" * 70)
                jumlah = 0
                for no, t in transaksi.items():
                    if role_aktif == "Admin" or t["penjual"] == nama_aktif or t["pembeli"] == nama_aktif:
                        print(t["id_hp"], "|", t["nama_hp"], "|", t["penjual"], "|",
                              t["pembeli"], "| Rp", t["harga"], "|", t["jenis"])
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
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        user_baru = input("Username baru : ").strip()
        pass_baru = input("Password baru (min. 3 karakter) : ").strip()

        if user_baru == "" or " " in user_baru:
            print("Error: Username tidak boleh kosong atau mengandung spasi!")
        elif user_baru in users:
            print("Error: Username sudah dipakai!")
        elif len(pass_baru) < 3:
            print("Error: Password minimal 3 karakter!")
        else:
            users[user_baru] = {"password": pass_baru, "role": "Pengguna Biasa"}
            print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    elif pilih == "3":
        print("Terima kasih. Program selesai.")
        program_jalan = False

    else:
        print("Error: Menu tidak tersedia!")
        input("Tekan Enter untuk kembali...")