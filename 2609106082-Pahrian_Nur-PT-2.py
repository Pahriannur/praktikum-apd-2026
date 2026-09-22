komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

harga_komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]

biaya_admin = 15000
total_biaya = (komponen_1 + komponen_2 + komponen_3 +  komponen_4 + komponen_5 + komponen_6 + biaya_admin)

rata_rata = total_biaya / len(harga_komponen)

nim = 82

bolean = nim != rata_rata

kurs_gbp = 23850
total_biaya_gbp = total_biaya / kurs_gbp

slice_negatif = harga_komponen[-6:-2]

print("program pahri")
print("semua kompenen")
print("komponen_1 :", komponen_1)
print("komponen_2 :", komponen_2)
print("komponen_3 :", komponen_3)
print("komponen_4 :", komponen_4)
print("komponen_5 :", komponen_5)
 
print(" List Harga Komponen")
print("harga_komponen        :", harga_komponen)    
print(" Hasil Perhitungan")
print("total_biaya (IDR)     :", total_biaya)
print("total_biaya (GBP)     :", round(total_biaya_gbp, 2))
print("rata_rata             :", rata_rata)
print("nim                   :", nim)
print("bolean (nim != rata)  :", bolean)
 
print("Poin Plus: Slice Index Negatif ")
print("slice_negatif (komponen_1 - komponen_4):", slice_negatif)
 
