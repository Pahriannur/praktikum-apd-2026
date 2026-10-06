
username_benar ="pahri"
pin_benar ="82"   

saldo = 2000000

print("=" * 35)
print("     SELAMAT DATANG DI ATM")
print("=" * 35)

sisa_login = 0
login_berhasil = False

while sisa_login < 3:
    username = input("Username : ")
    pin = input("PIN      : ")

    if username == username_benar and pin == pin_benar:
        print("Login Berhasil!")
        login_berhasil = True
        break
    else:
        sisa_login = sisa_login + 1
        sisa = 3 -sisa_login
        print("Login Gagal! Sisa percobaan Login:", sisa)

if login_berhasil == False:
    print("Akun Anda Terblokir!")
else:
   
    menu = 0
    while menu != 4:
        print()
        print("=" * 35)
        print("          MENU ATM")
        print("=" * 35)
        print("[1] Cek Saldo")
        print("[2] Tarik Tunai")
        print("[3] Setor Tunai")
        print("[4] Keluar")
        print("-" * 35)
        menu = int(input("Pilih menu (1-4): "))

        if menu == 1:
            print("Saldo Anda saat ini: Rp", saldo)

        elif menu == 2:
            print("Pilih kelipatan penarikan:")
            print("[1] Kelipatan Rp 50.000")
            print("[2] Kelipatan Rp 100.000")
            pilih = int(input("Pilih (1/2): "))

            if pilih == 1:
                kelipatan = 50000
            else:
                kelipatan = 100000

            tarik = int(input("Masukkan nominal tarik tunai: Rp "))

            if tarik > saldo:
                print("Saldo tidak mencukupi!")
            elif tarik <= 0 or tarik % kelipatan != 0:
                print("Nominal harus kelipatan Rp", kelipatan)
            else:
                saldo = saldo - tarik
                print("Transaksi berhasil!")
                print("Nominal ditarik : Rp", tarik)
                print("Sisa saldo      : Rp", saldo)

        elif menu == 3:
            setor = int(input("Masukkan nominal setor tunai: Rp "))

            if setor <= 0:
                print("Nominal setor harus lebih dari 0!")
            elif setor % 50000 != 0:
                print("Nominal harus kelipatan Rp 50.000")
            else:
                saldo = saldo + setor
                print("Setor tunai berhasil!")
                print("Nominal disetor : Rp", setor)
                print("Total saldo     : Rp", saldo)

        elif menu == 4:
            print("Terima kasih telah menggunakan ATM kami!")

        else:
            print("Pilihan tidak valid, masukkan angka 1-4.") 