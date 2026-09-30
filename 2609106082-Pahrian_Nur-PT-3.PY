
user_benar = "pahri"
pass_benar = "82"

print("=" * 40)
print("        SISTEM TOP UP GAME")
print("=" * 40)

username = input("Username : ")
password = input("Password : ")

if username == user_benar and password == pass_benar:
    print("Login Berhasil")
    print()

    id_player = input("ID Player : ")
    game = input("Nama Game (Genshin Impact / Minecraft / Mobile Legends) : ")
    kategori = input("Kategori Top Up (Kecil / Menengah / Besar) : ")
    metode = input("Metode Pembayaran (pulsa / E-Wallet) : ")

    if kategori == "kecil":
        harga = 15000
    elif kategori == "menengah":
        harga = 50000
    elif kategori == "besar":
        harga = 150000
    else:
        harga = 0
        print("Kategori tidak ada!")
    
    admin = 2500 if metode == "pulsa" else 500

    total_bayar = harga + admin

    print()
    print("Total yang harus dibayar : Rp", total_bayar)
    uang = int(input("Masukkan uang kamu : Rp "))

    if uang < total_bayar:
        print("Transaksi Gagal Saldo tidak mencukupi")
    else:
        kembalian = uang - total_bayar

        print()
        print("=" * 40)
        print("           STRUK PEMBELIAN")
        print("=" * 40)
        print("ID Player         :", id_player)
        print("Nama Game         :", game)
        print("Kategori Top Up   :", kategori)
        print("Metode Pembayaran :", metode)
        print("Biaya Admin       : Rp", admin)
        print("Total Bayar       : Rp", total_bayar)
        print("Uang Dibayar      : Rp", uang)
        print("Kembalian         : Rp", kembalian)
        print("=" * 40)
        print("       Terima kasih sudah top up!")
        print("=" * 40)
else:
    print("Login Gagal")