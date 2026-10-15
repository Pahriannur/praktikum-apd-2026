import os

users = [
    ["admin", "admin123", "Admin"],
    ["budi", "123", "Pengguna Biasa"],
    ["sari", "123", "Pengguna Biasa"]
]


daftar_kondisi = ("Mulus", "Baik", "Minus")


data_hp = [
    [1, "budi", "Samsung", "Galaxy A52", "Baik", 2500000, "Tersedia"],
    [2, "sari", "Xiaomi", "Redmi Note 10", "Mulus", 1800000, "Tersedia"]
]
id_terakhir = 2


transaksi = []

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

            for u in users:
                if u[0] == username and u[1] == password:
                    sudah_login = True
                    nama_aktif = u[0]
                    role_aktif = u[2]

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

                if merk.strip() == "" or tipe.strip() == "":
                    print("Error: Merk dan tipe tidak boleh kosong!")
                elif kondisi not in ("1", "2", "3"):
                    print("Error: Kondisi harus 1, 2, atau 3!")
                elif not harga.isdigit():
                    print("Error: Harga harus berupa angka bulat positif!")
                elif int(harga) <= 0:
                    print("Error: Harga harus lebih dari 0!")
                else:
                    id_terakhir += 1
                    data_hp.append([id_terakhir, nama_aktif, merk, tipe,
                                    daftar_kondisi[int(kondisi) - 1],
                                    int(harga), "Tersedia"])
                    transaksi.append([id_terakhir, merk + " " + tipe, nama_aktif,
                                      "-", int(harga), "Dijual"])
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
                    for h in data_hp:
                        if kata in h[2].lower():
                            print(h[0], "|", h[1], "|", h[2], "|", h[3], "|",
                                  h[4], "| Rp", h[5], "|", h[6])
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

                if not id_input.isdigit():
                    print("Error: ID harus berupa angka!")
                else:
                    posisi = -1
                    for i in range(len(data_hp)):
                        if data_hp[i][0] == int(id_input):
                            posisi = i

                    if posisi == -1:
                        print("Error: ID tidak ditemukan!")
                    elif role_aktif != "Admin" and data_hp[posisi][1] != nama_aktif:
                        print("Error: Anda hanya boleh mengubah HP milik sendiri!")
                    elif data_hp[posisi][6] == "Terjual":
                        print("Error: HP yang sudah terjual tidak bisa diubah!")
                    else:
                        print("Data lama:", data_hp[posisi][2], data_hp[posisi][3],
                              "|", data_hp[posisi][4], "| Rp", data_hp[posisi][5])
                        print("(Kosongkan input jika tidak ingin mengubah)")
                        merk_baru = input("Merk baru    : ").strip()
                        tipe_baru = input("Tipe baru    : ").strip()
                        print("Kondisi: [1] Mulus  [2] Baik  [3] Minus")
                        kondisi_baru = input("Kondisi baru : ").strip()
                        harga_baru = input("Harga baru   : ").strip()

                        if kondisi_baru != "" and kondisi_baru not in ("1", "2", "3"):
                            print("Error: Kondisi harus 1, 2, atau 3!")
                        elif harga_baru != "" and not harga_baru.isdigit():
                            print("Error: Harga harus berupa angka bulat positif!")
                        elif harga_baru != "" and int(harga_baru) <= 0:
                            print("Error: Harga harus lebih dari 0!")
                        else:
                            if merk_baru.strip() != "":
                                data_hp[posisi][2] = merk_baru
                            if tipe_baru.strip() != "":
                                data_hp[posisi][3] = tipe_baru
                            if kondisi_baru != "":
                                data_hp[posisi][4] = daftar_kondisi[int(kondisi_baru) - 1]
                            if harga_baru != "":
                                data_hp[posisi][5] = int(harga_baru)
                            print("Data HP berhasil diubah.")
                input("Tekan Enter untuk kembali...")

          
            elif menu == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== HAPUS HP ===")
                id_input = input("Masukkan ID HP yang ingin dihapus : ").strip()

                if not id_input.isdigit():
                    print("Error: ID harus berupa angka!")
                else:
                    posisi = -1
                    for i in range(len(data_hp)):
                        if data_hp[i][0] == int(id_input):
                            posisi = i

                    if posisi == -1:
                        print("Error: ID tidak ditemukan!")
                    elif role_aktif != "Admin" and data_hp[posisi][1] != nama_aktif:
                        print("Error: Anda hanya boleh menghapus HP milik sendiri!")
                    else:
                        yakin = input("Yakin ingin menghapus? (Y/T) : ").upper().strip()
                        if yakin == "Y":
                            data_hp.pop(posisi)
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
                for i in range(len(users)):
                    print(i + 1, "|", users[i][0], "|", users[i][2])
                print("-" * 35)
                hapus = input("Username yang ingin dihapus (kosong = batal) : ").strip()

                if hapus != "":
                    posisi = -1
                    for i in range(len(users)):
                        if users[i][0] == hapus:
                            posisi = i

                    if posisi == -1:
                        print("Error: Username tidak ditemukan!")
                    elif users[posisi][2] == "Admin":
                        print("Error: Akun Admin tidak boleh dihapus!")
                    else:
                        users.pop(posisi)
                   
                        hp_baru = []
                        for h in data_hp:
                            if h[1] != hapus:
                                hp_baru.append(h)
                        data_hp = hp_baru
                        print("Pengguna dan HP miliknya berhasil dihapus.")
                input("Tekan Enter untuk kembali...")

            
            elif menu == "5" and role_aktif != "Admin":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== BELI HP ===")
                print("Daftar HP yang tersedia:")
                print("-" * 70)
                ada = False
                for h in data_hp:
                    if h[6] == "Tersedia" and h[1] != nama_aktif:
                        print(h[0], "|", h[1], "|", h[2], h[3], "|", h[4], "| Rp", h[5])
                        ada = True
                print("-" * 70)

                if not ada:
                    print("Belum ada HP yang bisa dibeli.")
                else:
                    id_input = input("Masukkan ID HP yang ingin dibeli : ").strip()
                    if not id_input.isdigit():
                        print("Error: ID harus berupa angka!")
                    else:
                        posisi = -1
                        for i in range(len(data_hp)):
                            if data_hp[i][0] == int(id_input):
                                posisi = i

                        if posisi == -1:
                            print("Error: ID tidak ditemukan!")
                        elif data_hp[posisi][1] == nama_aktif:
                            print("Error: Anda tidak bisa membeli HP sendiri!")
                        elif data_hp[posisi][6] == "Terjual":
                            print("Error: HP sudah terjual!")
                        else:
                            yakin = input("Yakin ingin membeli? (Y/T) : ").upper().strip()
                            if yakin == "Y":
                                data_hp[posisi][6] = "Terjual"
                                transaksi.append([data_hp[posisi][0],
                                                  data_hp[posisi][2] + " " + data_hp[posisi][3],
                                                  data_hp[posisi][1], nama_aktif,
                                                  data_hp[posisi][5], "Terjual"])
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
                for t in transaksi:
                    if role_aktif == "Admin" or t[2] == nama_aktif or t[3] == nama_aktif:
                        print(t[0], "|", t[1], "|", t[2], "|", t[3], "| Rp", t[4], "|", t[5])
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

        sudah_ada = False
        for u in users:
            if u[0] == user_baru:
                sudah_ada = True

        if user_baru.strip() == "" or " " in user_baru:
            print("Error: Username tidak boleh kosong atau mengandung spasi!")
        elif sudah_ada:
            print("Error: Username sudah dipakai!")
        elif len(pass_baru) < 3:
            print("Error: Password minimal 3 karakter!")
        else:
            users.append([user_baru, pass_baru, "Pengguna Biasa"])
            print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    
    elif pilih == "3":
        print("Terima kasih. Program selesai.")
        program_jalan = False

    else:
        print("Error: Menu tidak tersedia!")
        input("Tekan Enter untuk kembali...")