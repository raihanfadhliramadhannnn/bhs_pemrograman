def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Error: Division by zero is not allowed."

angka1 = float(input("Masukkan angka pertama untuk dijumlahkan: "))
angka2 = float(input("Masukkan angka kedua untuk dijumlahkan: "))

print("\nMENU")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Pengkalian")
print("4. Pembagian")

pilihan = int(input("Masukkan Pilihan: "))

if pilihan == 1:
    hasil = tambah(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == 2:
    hasil = kurang(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == 3:
    hasil = kali(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == 4:
    hasil = bagi(angka1, angka2)
    print("Hasil:", hasil)
else:
    print("Pilihan tidak valid.")
