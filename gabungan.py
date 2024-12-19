# TUGAS BESAR BERPIKIR KOMPUTASIONAL
# Semua library yang dipakai dalam projek ini adalah library built-in
# AI hanya digunakan untuk generasi produk
# Hal tambahan : Menggunakan string.format() untuk mempermudah penulisan, menggunakan len() karena diperbolehkan saat praktikum

import random # Library untuk generasi kemungkinan gagal saat melakukan pembuatan QRIS, sangat susah digantikan sendiri sehingga harus dipakai
import os # Library untuk melakukan clear console, hanya sebagai visual, tidak mempengaruhi logika
import time # Library untuk menunggu, hanya sebagai visual, tidak mempengaruhi logika

# Selain yang diberikan di atas, seluruh program ini hanya menggunakan Modul 01 dan Modul 02

# List produk
list_produk = [
    "Snack Bar",       # Camilan dalam bentuk batangan
    "Chips",           # Keripik
    "Candy",           # Permen
    "Soda",            # Minuman soda
    "Water",           # Air mineral
    "Juice",           # Jus
    "Cookies",         # Kue kering
    "Chocolate",       # Cokelat
    "Energy Drink",    # Minuman energi
    "Gum",             # Permen karet
    "Nuts",            # Kacang
    "Crackers",        # Biskuit
    "Ice Cream",       # Es krim
    "Hot Coffee",      # Kopi panas
    "Tea",             # Teh
    "Fruit Cup",       # Buah potong
    "Sandwich",        # Roti lapis
    "Instant Noodles", # Mie instan
    "Cup Soup"         # Sup dalam cup
]

# List harga (kelipatan 5000)
list_harga = [
    15000,   # Harga Snack Bar
    10000,   # Harga Chips
    5000,    # Harga Candy
    10000,   # Harga Soda
    5000,    # Harga Water
    10000,   # Harga Juice
    15000,   # Harga Cookies
    20000,   # Harga Chocolate
    25000,   # Harga Energy Drink
    5000,    # Harga Gum
    10000,   # Harga Nuts
    10000,    # Harga Crackers
    20000,   # Harga Ice Cream
    15000,   # Harga Hot Coffee
    10000,   # Harga Tea
    10000,   # Harga Fruit Cup
    20000,   # Harga Sandwich
    10000,   # Harga Instant Noodles
    15000    # Harga Cup Soup
]

# List jumlah produk (stok)
list_jumlah_produk = [
    0,  # Stok Snack Bar
    20,  # Stok Chips
    30,  # Stok Candy
    15,  # Stok Soda
    25,  # Stok Water
    12,  # Stok Juice
    18,  # Stok Cookies
    8,   # Stok Chocolate
    5,   # Stok Energy Drink
    50,  # Stok Gum
    10,  # Stok Nuts
    25,  # Stok Crackers
    10,  # Stok Ice Cream
    5,   # Stok Hot Coffee
    15,  # Stok Tea
    20,  # Stok Fruit Cup
    1,   # Stok Sandwich
    30,  # Stok Instant Noodles
    25   # Stok Cup Soup
]

# List index produk (angka)
list_produk_angka = range(len(list_produk))

colorList = ['\033[0m',"\033[95m","\033[94m",'\033[96m','\033[92m', '\033[93m', '\033[91m','\033[1m','\033[4m']

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
    print("╔═══════════════════════════════════╗")
    print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
    print("╠════╦════════════════════╦═════════╣")
    print("║ Id ║ Product            ║ Price   ║")
    print("╠════╬════════════════════╬═════════╣")

    for i in range(len(list_produk)):
        if list_jumlah_produk[i] >= 1:
            print("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
        else :
            print("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))

    print("╠════╩════════════════════╩═════════╣")
    print("║{}{:^35}{}║".format(colorList[4],"Balance : Rp"+str(balance),colorList[0]))
    print("╚═══════════════════════════════════╝")
    masukan = int(input("{}{:^36}{}\n\n > ".format(colorList[1],"Masukkan Id Produk",colorList[0])))
    n=len(list_produk)
    for i in range(n):
        if list_produk_angka[i] == masukan :
            produk_pilih = i
            if list_jumlah_produk[produk_pilih] >= 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("╔═══════════════════════════════════╗")
                print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
                print("╠════╦════════════════════╦═════════╣")
                print("║ Id ║ Product            ║ Price   ║")
                print("╠════╬════════════════════╬═════════╣")
                for i in range(len(list_produk)):
                    if(i==produk_pilih):
                        print("{}║ {:<2} ║ {:<18} ║ Rp{:<5} ║{}".format(colorList[1],list_produk_angka[i],"["+ list_produk[i]+"]",formatted_prices[i], colorList[0]))
                    elif list_jumlah_produk[i] >= 1:
                        print("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
                    else :
                        print("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))

                print("╠════╩════════════════════╩═════════╣")
                print("║{}{:^35}{}║".format(colorList[4],"Balance : Rp"+str(balance),colorList[0]))
                print("╚═══════════════════════════════════╝")
                print("{:^35}".format("Pilih metode pembayaran"))
                metode_pembayaran = int(input("{:^45}\n\n> ".format(colorList[1]+"QRIS (1) / Cash (2)"+colorList[0])))
                if metode_pembayaran == 1:
                    paymentReceived = True
                    print ("\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    print("{}{:^35}{}".format(colorList[0],f"Creating QRIS with price: {list_harga[produk_pilih]}",colorList[0]))
                    time.sleep(3)
                    print ("\033[A                                                        \033[A")
                    percentFail = 1
                    if random.randint(1,100)<=percentFail:
                        print("{}{:^35}{}".format(colorList[6],"Failed to create QRIS",colorList[0]))
                        time.sleep(3)
                        produk_pilih = -1
                        break
                    else:
                        print("{}{:^35}{}".format(colorList[0],"QRIS created successfully",colorList[0]))
                        print ("\033[A                                                        \033[A")
                        print("    █▀▀▀▀▀█ ▀▀▄▄▀▄▀▀▀ █▀▀▀▀▀█    ")
                        print("    █ ███ █ ▄▄▄ ▄▄▄█▀ █ ███ █    ")
                        print("    █ ▀▀▀ █ ██ ███▀▀█ █ ▀▀▀ █    ")
                        print("    ▀▀▀▀▀▀▀ █ █ █ █▄▀ ▀▀▀▀▀▀▀    ")
                        print("    █  ▄▀ ▀▀▀▀█▄▀ ██▄█▀▀██ ▄▀    ")
                        print("    ▄▀█▀█▀ █▀█ ▄▀▀█▄ ▄█▀▀█▄      ")
                        print("    ▄▀▄█ ▄▀████ ▀▄▄▄▄█▀ ▄▀▀█▀    ")
                        print("      █▀▄▀  ▄▄ ▄▀▄██ ▄██▀█▄      ")
                        print("    ▀▀▀▀ ▀▀ ▄█▀▀▄ ▄██▀▀▀█▀▀      ")
                        print("    █▀▀▀▀▀█ ▀  █▀▀█ █ ▀ █▄▄ ▄    ")
                        print("    █ ███ █ ▀▀▄ ▀ ▄▄▀▀██▀▀███    ")
                        print("    █ ▀▀▀ █  ██ ▄ █▄▀▀█▄▄█▄█     ")
                        print("    ▀▀▀▀▀▀▀ ▀  ▀▀▀▀▀      ▀▀▀    ")
                        input("{}{:^35}{}".format(colorList[1],"Press Enter To Pay",colorList[0]))
                        if(paymentReceived):
                            for _ in range(12):
                                print ("\033[A                                                        \033[A")
                            animation_list = [[""]*len(list_produk) for _ in range(len(list_produk)-(produk_pilih+1)+1)]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("╔═══════════════════════════════════╗")
                            print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
                            print("╠════╦════════════════════╦═════════╣")
                            print("║ Id ║ Product            ║ Price   ║")
                            print("╠════╬════════════════════╬═════════╣")
                            for j in range(len(animation_list)):
                                for l in range(len(animation_list[j])):
                                    i = l
                                    if(i==produk_pilih):
                                        animation_list[j][l] = ("║ {:<2} ║ {:<18} ║ {:<5}   ║").format("","","")
                                        if(l+j>len(animation_list[j])-1):
                                            break
                                        animation_list[j][l+j] = ("{}║ {:<2} ║ {:<18} ║ Rp{:<5} ║{}".format(colorList[1],list_produk_angka[i],"["+ list_produk[i]+"]",formatted_prices[i], colorList[0]))
                                    elif list_jumlah_produk[i] >= 1 and animation_list[j][l]=='':
                                        animation_list[j][l] =("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
                                    elif list_jumlah_produk[i]<1 and animation_list[j][l]=='':
                                        animation_list[j][l] = ("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))
                            for j in range(len(animation_list)):
                                for l in range(len(animation_list[j])):
                                    print(animation_list[j][l])
                                print("╠════╩════════════════════╩═════════╣")
                                print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance)),colorList[0]))
                                print("╚═══════════════════════════════════╝")
                                time.sleep(0.5)
                                for l in range(len(animation_list[j])+3):
                                    print ("\r\033[A                                                                  \033[A")
                            for i in range(len(list_produk)):
                                if list_jumlah_produk[i] >= 1:
                                    print("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
                                else :
                                    print("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))

                            print("╠════╩════════════════════╩═════════╣")
                            print("║{}{:^35}{}║".format(colorList[4],"Balance : Rp"+str(balance),colorList[0]))
                            print("╚═══════════════════════════════════╝")
                            print("{}{:^35}{}".format(colorList[1],"Thank you and enjoy!",colorList[0]))
                            time.sleep(5)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            produk_pilih = -1
                            break
                elif metode_pembayaran == 2:
                    readable = True
                    
                    isTambahUang = 'y'

                    harga = list_harga[produk_pilih]

                    print ("\r\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    print ("\033[A                                                        \033[A")
                    if balance<harga :
                        while isTambahUang == 'y' or isTambahUang == 'Y' or isTambahUang == '' :
                            print("{:^38}".format("Masukkan Uang"))
                            cash = int(input("{:^44}\n\n > ".format(colorList[6]+"Hanya kelipatan Rp. 5.000"+colorList[0])))
                            print ("\r\033[A                                                        \033[A")
                            print ("\033[A                                                        \033[A")
                            print ("\033[A                                                        \033[A")
                            print ("\033[A                                                        \033[A")
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
                                else: 
                                    print("{}{:^36}{}".format(colorList[1],"Uang bukan kelipatan Rp5000.",colorList[0]))
                                    print("{}{:^36}{}".format(colorList[1],"atau tidak legal",colorList[0]))
                                    time.sleep(2)
                                    print ("\r\033[A                                                                  \033[A")
                                    print ("\r\033[A                                                                  \033[A")
                                    print("{:^38}".format("Mengeluarkan Uang."))
                                    time.sleep(1)
                                    print ("\r\033[A                                                                  \033[A")
                                    print("{:^38}".format("Mengeluarkan Uang.."))
                                    time.sleep(1)
                                    print ("\r\033[A                                                                  \033[A")
                                    print("{:^38}".format("Mengeluarkan Uang..."))
                                    time.sleep(1)
                                    print ("\r\033[A                                                                  \033[A")
                            else: print("Tidak bisa membaca uang. Mengeluarkan uang..")
                            for i in range(len("Balance : Rp"+str(balance))):
                                print ("\r\033[A                                                                  \033[A")
                                print ("\r\033[A                                                                  \033[A")
                                print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance))[:i+1],colorList[0]))
                                print("╚═══════════════════════════════════╝")
                                time.sleep(0.1)
                            if(balance<harga):
                                print("{}{:^36}{}".format(colorList[0],f"Balance kurang Rp{harga-balance}.",colorList[0]))
                                isTambahUang = input("{}{:^36}{}\n\n > ".format(colorList[1],"Tambahkan Uang? (Y/n)",colorList[0]))
                                print ("\r\033[A                                                        \033[A")
                                print ("\r\033[A                                                        \033[A")
                                print ("\r\033[A                                                        \033[A")
                                print ("\r\033[A                                                        \033[A")
                            else:
                                isTambahUang = 'n'
                    if balance>=harga :
                        print("{}{:^36}{}".format(colorList[0],"Uang telah diterima.",colorList[0]))
                        time.sleep(2)
                        print ("\033[A                                                        \033[A")
                        print("{}{:^36}{}".format(colorList[0],"Pesanan sedang diproses.",colorList[0]))
                        time.sleep(2)
                        print ("\033[A                                                        \033[A")
                        kembalian=balance-harga
                        if balance>harga:
                            print("{}{:^36}{}".format(colorList[0],"Total kembalian Anda Rp"+str(kembalian),colorList[0]))
                            time.sleep(2)
                            print ("\033[A                                                        \033[A")
                            for i in range(len(amountOfBalance),0,-1):
                                while kembalian>=typeOfBalance[i-1] and amountOfBalance[i-1]>0:
                                    print("{}{:^36}{}".format(colorList[0],"Mengeluarkan uang kembalian sebesar",colorList[0]))
                                    print("{}{:^36}{}".format(colorList[4],"Rp"+str(typeOfBalance[i-1]),colorList[0]))
                                    amountOfBalance[i-1] -= 1
                                    kembalian -= typeOfBalance[i-1]
                                    time.sleep(2)
                                    print ("\033[A                                                        \033[A")
                                    time.sleep(1)
                                    print ("\033[A                                                        \033[A")

                            if(kembalian>0):
                                print("{}{:^36}{}".format(colorList[0],"Kembalian tidak tersedia.",colorList[0]))
                                print("{}{:^36}{}".format(colorList[1],"Uang anda tersimpan sebagai balance.",colorList[0]))
                                time.sleep(5)
                                print ("\033[A                                                        \033[A")
                                print ("\033[A                                                        \033[A")
                        balance=kembalian
                        for i in range(len("Balance : Rp"+str(balance))):
                            print ("\r\033[A                                                                  \033[A")
                            print ("\r\033[A                                                                  \033[A")
                            print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance))[:i+1],colorList[0]))
                            print("╚═══════════════════════════════════╝")
                            time.sleep(0.1)
                        list_jumlah_produk[produk_pilih] -= 1
                        print("{}{:^35}{}".format(colorList[1],"Payment Received",colorList[0]))
                        time.sleep(1)
                        print ("\r\033[A                                                                  \033[A")
                        print("{}{:^35}{}".format(colorList[1],"Dropping Product",colorList[0]))
                        animation_list = [[""]*len(list_produk) for _ in range(len(list_produk)-(produk_pilih+1)+1)]
                        for l in range(24):
                            print ("\r\033[A                                                                  \033[A")
                        for j in range(len(animation_list)):
                            for l in range(len(animation_list[j])):
                                i = l
                                if(i==produk_pilih):
                                    animation_list[j][l] = ("║ {:<2} ║ {:<18} ║ {:<5}   ║").format("","","")
                                    if(l+j>len(animation_list[j])-1):
                                        break
                                    animation_list[j][l+j] = ("{}║ {:<2} ║ {:<18} ║ Rp{:<5} ║{}".format(colorList[1],list_produk_angka[i],"["+ list_produk[i]+"]",formatted_prices[i], colorList[0]))
                                elif list_jumlah_produk[i] >= 1 and animation_list[j][l]=='':
                                    animation_list[j][l] =("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
                                elif list_jumlah_produk[i]<1 and animation_list[j][l]=='':
                                    animation_list[j][l] = ("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))
                        for j in range(len(animation_list)):
                            for l in range(len(animation_list[j])):
                                print(animation_list[j][l])
                            print("╠════╩════════════════════╩═════════╣")
                            print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance)),colorList[0]))
                            print("╚═══════════════════════════════════╝")
                            time.sleep(0.5)
                            for l in range(len(animation_list[j])+3):
                                print ("\r\033[A                                                                  \033[A")
                        for i in range(len(list_produk)):
                            if list_jumlah_produk[i] >= 1:
                                print("║ {:<2} ║ {:<18} ║ Rp{:<5} ║".format(list_produk_angka[i], list_produk[i],formatted_prices[i]))
                            else :
                                print("║ {:<2} ║ {:<18} ║ {:<6}   ║".format(list_produk_angka[i], list_produk[i],colorList[6]+"Habis"+colorList[0]))

                        print("╠════╩════════════════════╩═════════╣")
                        print("║{}{:^35}{}║".format(colorList[4],"Balance : Rp"+str(balance),colorList[0]))
                        print("╚═══════════════════════════════════╝")
                        print("{}{:^35}{}".format(colorList[1],"Thank you and enjoy!",colorList[0]))
                        time.sleep(5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        produk_pilih = -1
                        break
            else:
                print("Stock untuk produk tersebut habis, harap pilih produk lain")
                produk_pilih = -1
                time.sleep(1)
                break
        elif i == n-1:
            print("{}{:^36}{}".format(colorList[6],"Angka yang Anda input tidak valid",colorList[0]))
            time.sleep(2)
            print ("\r\033[A                                                                  \033[A")
            produk_pilih = -1
            break
