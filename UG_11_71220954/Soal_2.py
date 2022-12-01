print("Pemeriksa Kelipatan 9")
angka = int(input("Masukkan Kelipatan 9 yang ingin diperiksa: "))
def kelipatan_sembilan(angka):
    jawaban = (angka % 9)
    return jawaban

if kelipatan_sembilan(angka)== 0:
    print ("Benar")
else:
    print ("Salah")