import random
import os
import time

list_produk = ["pocari", "coke", "sosro"]
list_harga = [5000,10000, 200000]
list_jumlah_produk = [5,0,2]
list_produk_angka = [20,12,0]

typeOfBalance = [5000,10000, 20000, 50000, 100000]
amountOfBalance = [0,2,5,1,1]
produk_pilih = -1

formatted_prices = [
f"{int(price / 1000)}k" 
for price in list_harga
]

balance =0

while produk_pilih == -1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔═══════════════════════╗")
    print("║    Vending Machine    ║")
    print("╠════╦════════╦═════════╣")
    print("║ Id ║ Product║ Price   ║")
    print("╠════╬════════╬═════════╣")

    for i in range(len(list_produk)):
        print("║ {:<2} ║ {:<6} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i], formatted_prices[i]))

    print("╚════╩════════╩═════════╝")


    n = list_produk_angka.__len__()
    print("Balance anda sekarang Rp", balance)
    masukan = int(input("Masukkan Id: "))
    for i in range(n):
        if list_produk_angka[i] == masukan :
            produk_pilih = i
            if list_jumlah_produk[produk_pilih] >= 1:
                print(list_produk[produk_pilih])
                print("Pilih metode pembayaran : ")
                metode_pembayaran = int(input("Qris (1) / Cash (2) : "))
                if metode_pembayaran == 1:
                    ownerId = "92983812389123"
                    paymentReceived = True
                    print(f"creating QRIS with price: {list_harga[produk_pilih-1]} to account {ownerId}")
                    time.sleep(1)
                    percentFail = 1
                    if random.randint(1,100)<=percentFail:
                        print("QRIS failed to create, please try again")
                        time.sleep(1)
                        produk_pilih=-1
                        break
                    else:
                        print("QRIS created successfully")
                        print("displaying QR")
                        print("waiting for payment...")
                        time.sleep(1)
                        if(paymentReceived):
                            list_jumlah_produk[produk_pilih] -= 1
                            print("payment received")
                            print("Product is spinning")
                            n = 3
                            while n > 0 : 
                                print (n)
                                time.sleep(1)
                                n -= 1
                            print ("latch is unlocked, thank you end enjoy!")
                            produk_pilih = -1
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                elif metode_pembayaran == 2:
                    readable = True
                    
                    isTambahUang = 'y'

                    harga = list_harga[produk_pilih]

                    while isTambahUang == 'y' or isTambahUang == 'Y' or isTambahUang == '' or balance>=harga:
                        print("Hanya dapat memasukan uang kelipatan Rp. 5.000")
                        cash =  int(input("Masukan Uang : "))
                        if readable == True: 
                            if cash == 5000:
                                amountOfBalance[0] += 1
                                balance += cash
                            elif cash == 10000:
                                amountOfBalance[1] += 1
                                balance += cash
                            elif cash == 20000:
                                amountOfBalance[2] += 1
                                balance += cash
                            elif cash == 50000:
                                amountOfBalance[3] += 1
                                balance += cash
                            elif cash == 100000:
                                amountOfBalance[4] += 1
                                balance += cash
                            else: print("Uang bukan kelipatan Rp5000 atau tidak legal. Mengeluarkan uang..")
                        else: print("Tidak bisa membaca uang. Mengeluarkan uang..")

                        print("Balance anda sekarang Rp", balance)
                        time.sleep(1)
                        if(balance<harga):
                            isTambahUang = input(f"Uang kurang {harga-balance}, tambah uang? (Y/n) : ")
                        else:
                            isTambahUang = 'n'
                    if balance>=harga :
                        kembalian=balance-harga
                        if balance>harga:
                            print("Kembalian anda Rp", kembalian)
                            time.sleep(1)
                            for i in range(len(amountOfBalance),0,-1):
                                while kembalian>=typeOfBalance[i-1] and amountOfBalance[i-1]>0:
                                    print("mengeluarkan uang kembalian "+str(typeOfBalance[i-1]))
                                    amountOfBalance[i-1] -= 1
                                    kembalian -= typeOfBalance[i-1]
                                    time.sleep(1)

                            if(kembalian>0):
                                print("Kembalian tidak tersedia, uang anda masih tersisa Rp",kembalian)
                                balance=kembalian
                        list_jumlah_produk[produk_pilih] -= 1
                        print("payment received")
                        time.sleep(1)
                        print("Product is spinning")
                        n = 3
                        while n > 0 : 
                            print (n)
                            time.sleep(1)
                            n -= 1
                        print ("latch is unlocked, thank you and enjoy!")
                        produk_pilih = -1
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

            else:
                print("Stock untuk produk tersebut habis, harap pilih produk lain")
                produk_pilih = -1
                time.sleep(1)
                break
        elif i == n-1:
            print("Angka yang anda input tidak ada")
            time.sleep(1)
            break
