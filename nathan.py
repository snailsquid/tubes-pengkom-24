list_produk = ["pocari", "coke", "sosro"]
list_harga = [5000,10000, 200000]
list_jumlah_produk = [5,0,2]
list_produk_angka = [20,12,0]

typeOfBalance = [5000,10000, 20000, 50000, 100000]
amountOfBalance = [0,0,0,0,0]
produk_pilih = 0



print(list_produk)
print(list_harga)
print(list_produk_angka)
masukan = int(input("Masukkan angka untuk produk berkoresponding : "))


n = list_produk_angka.__len__()
for i in range(n):
    if list_produk_angka[i] == masukan :
        produk_pilih = i
        break
    elif i == n-1:
        print("Angka yang anda input salah")


if list_jumlah_produk[produk_pilih] >= 1:
    print(list_produk[produk_pilih])
    print("Pilih metode pembayaran : ")
    metode_pembayaran = input("Qris atau Cash")
    if metode_pembayaran == "Qris":
        print("go to qris")
    elif metode_pembayaran == "Cash":
        print("go to cash")
else:
    print("Stock untuk produk tersebut habis, harap pilih produk lain")
