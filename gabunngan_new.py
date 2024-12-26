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

list_topup = [
    "Mobile Legends", 
    "Free Fire",
    "PUBG Mobile",
    "GoPay",
    "ShopeePay",
    "OVO"
]

list_topup_category = [
    "Game",
    "Game",
    "Game",
    "E-Wallet",
    "E-Wallet",
    "E-Wallet",
]

list_topup_harga_base = [ # harga per Rp10.000
    36,  # Mobile Legends
    72,  # Free Fire
    96, # PUBG Mobile
]

list_topup_names = [
    "diamonds", 
    "diamonds",
    "UC",
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
list_topup_angka = range(len(list_topup))

colorList = ['\033[0m',"\033[95m","\033[94m",'\033[96m','\033[92m', '\033[93m', '\033[91m','\033[1m','\033[4m']

typeOfBalance = [5000,10000, 20000, 50000, 100000]
amountOfBalance = [0,2,5,1,1]
produk_pilih = -1

formatted_prices = [
f"{int(price / 1000)}k" 
for price in list_harga
]

balance =0

discount = [
    0,
    5,
    10,
    15,
    20,
    25
]
discount_quantity = [
    0,
    10,
    20,
    50,
    100,
    150
]
def get_price(index, price):
    quantity= price/10000
    for i in range(len(discount_quantity)):
        if quantity <= discount_quantity[i]:
            return list_topup_harga_base[index]*(1-discount[i]/100)*quantity
        else:
            return list_topup_harga_base[index]*(1-discount[len(discount)-1]/100)*quantity
def clearLines(times):
    for i in range(times):
        print ("\r\033[A                                                        \033[A")
def reset(error, sleep, resetProduk = True):
    global colorList, produk_pilih
    print("{}{:^36}{}".format(colorList[6],error,colorList[0]))
    time.sleep(sleep)
    clearLines(1)
    if resetProduk:
        produk_pilih = -1
def animateDrop():
    global colorList, list_produk, list_produk_angka, list_jumlah_produk, list_harga, balance, formatted
    animation_list = [[""]*len(list_produk) for _ in range(len(list_produk)-(produk_pilih+1)+1)]
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
def printVendingMachine():
    global colorList, list_produk, list_produk_angka, list_jumlah_produk, list_harga, balance, formatted
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
def printTopupMachine():
    global colorList, list_topup, list_topup_angka, list_topup_category, list_topup_shop, balance
    print("╔═══════════════════════════════════╗")
    print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
    print("╠════╦══════════════════════════════╣")
    print("║ Id ║ Product                      ║")
    print("╠════╬══════════════════════════════╣")
    for i in range(len(list_topup)):
        if(i==produk_pilih):
            print("{}║ {:<2} ║ {:<28} ║{}".format(colorList[1],list_topup_angka[i],"["+ list_topup[i]+"]", colorList[0]))
        else :
            print("║ {:<2} ║ {:<28} ║".format(list_topup_angka[i], list_topup[i]))
    print("╠════╩══════════════════════════════╣")
    print("║{}{:^35}{}║".format(colorList[4],"Balance : Rp"+str(balance),colorList[0]))
    print("╚═══════════════════════════════════╝")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def EMoneyPayment(harga):
    clearLines(4)
    print("{}{:^35}{}".format(colorList[0],f"Biaya yang dikenakan adalah Rp{harga}",colorList[0]))
    color = 2
    while True :
        color = 4 if color == 2 else 2
        press = input("{}{:^35}{}".format(colorList[color],f"Silakan tempelkan kartu E-Money",colorList[0]))
        if press == "" : break
        time.sleep(1)
        clearLines(1)
        if press == "" : break
    clearLines(2)
    print("{}{:^37}{}".format(colorList[5],f"Processing Payment",colorList[0]))
    total = 20
    for i in range(total + 1):
        bar = '#' * i + '-' * (total - i)
        print(f'\r{('['+bar+']').center(35)}')
        time.sleep(.1) 
        clearLines(1)
    clearLines(1)
    print("{}{:^37}{}".format(colorList[5],f"Payment Complete",colorList[0]))
    print(f'\r{("["+'#'*total+"]").center(35)}')
    time.sleep(1)
    clearLines(2)

def QrisPayment(harga):
    global colorList, list_produk, list_produk_angka, list_jumlah_produk, list_harga, balance, formatted
    clearLines(4)
    print("{}{:^35}{}".format(colorList[0],f"Creating QRIS with price: {harga}",colorList[0]))
    time.sleep(3)
    clearLines(1)
    percentFail = 1
    if random.randint(1,100)<=percentFail:
        reset("Failed to create QRIS",2)
        return True
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
def CashPayment(harga):
    global colorList, list_produk, list_produk_angka, list_jumlah_produk, list_harga, balance, formatted
    readable = True
    
    isTambahUang = 'y'


    clearLines(4)
    if balance<harga :
        while isTambahUang == 'y' or isTambahUang == 'Y' or isTambahUang == '' :
            print("{:^38}".format("Masukkan Uang"))
            cash = int(input("{:^44}\n\n > ".format(colorList[6]+"Hanya kelipatan Rp. 5.000"+colorList[0])))
            clearLines(4)
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
                    clearLines(2)
                    print("{:^38}".format("Mengeluarkan Uang."))
                    time.sleep(1)
                    clearLines(1)
                    print("{:^38}".format("Mengeluarkan Uang.."))
                    time.sleep(1)

                    clearLines(1)
                    print("{:^38}".format("Mengeluarkan Uang..."))
                    time.sleep(1)
                    clearLines(1)
            else: print("Tidak bisa membaca uang. Mengeluarkan uang..")
            for i in range(len("Balance : Rp"+str(balance))):
                clearLines(2)
                print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance))[:i+1],colorList[0]))
                print("╚═══════════════════════════════════╝")
                time.sleep(0.1)
            if(balance<harga):
                print("{}{:^36}{}".format(colorList[0],f"Balance kurang Rp{harga-balance}.",colorList[0]))
                isTambahUang = input("{}{:^36}{}\n\n > ".format(colorList[1],"Tambahkan Uang? (Y/n)",colorList[0]))
                clearLines(4)
            else:
                isTambahUang = 'n'
    if balance>=harga :
        print("{}{:^36}{}".format(colorList[0],"Uang telah diterima.",colorList[0]))
        time.sleep(2)
        clearLines(1)
        print("{}{:^36}{}".format(colorList[0],"Pesanan sedang diproses.",colorList[0]))
        time.sleep(2)
        clearLines(1)
        kembalian=balance-harga
        if balance>harga:
            print("{}{:^36}{}".format(colorList[0],"Total kembalian Anda Rp"+str(kembalian),colorList[0]))
            time.sleep(2)
            clearLines(1)
            for i in range(len(amountOfBalance),0,-1):
                while kembalian>=typeOfBalance[i-1] and amountOfBalance[i-1]>0:
                    print("{}{:^36}{}".format(colorList[0],"Mengeluarkan uang kembalian sebesar",colorList[0]))
                    print("{}{:^36}{}".format(colorList[4],"Rp"+str(typeOfBalance[i-1]),colorList[0]))
                    amountOfBalance[i-1] -= 1
                    kembalian -= typeOfBalance[i-1]
                    time.sleep(2)
                    clearLines(1)
                    time.sleep(1)
                    clearLines(1)

            if(kembalian>0):
                print("{}{:^36}{}".format(colorList[0],"Kembalian tidak tersedia.",colorList[0]))
                print("{}{:^36}{}".format(colorList[1],"Uang anda tersimpan sebagai balance.",colorList[0]))
                time.sleep(5)
                clearLines(2)
        balance=kembalian
        for i in range(len("Balance : Rp"+str(balance))):
            clearLines(2)
            print("║{}{:^35}{}║".format(colorList[4],("Balance : Rp"+str(balance))[:i+1],colorList[0]))
            print("╚═══════════════════════════════════╝")
            time.sleep(0.1)
        list_jumlah_produk[produk_pilih] -= 1
        print("{}{:^35}{}".format(colorList[1],"Payment Received",colorList[0]))
        time.sleep(1)
        clearLines(1)
while(produk_pilih == -1):
    clear()

    print("╔═══════════════════════════════════╗")
    print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
    print("╠═══════════════════════════════════╣")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║{}{:^35}{}║".format(colorList[1],"Topup (1) / Konsumsi (2) ?",colorList[0]))
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("║                                   ║")
    print("╚═══════════════════════════════════╝")
    
    opsi = int(input("\n > "))
    clear()
    if opsi == 1 :
        printTopupMachine()

        produk_pilih = int(input("{}{:^36}{}\n\n > ".format(colorList[1],"Masukkan Id Produk",colorList[0])))
        jumlah = 0
        clearLines(3)
        clear()
        printTopupMachine()
        if list_topup_category[produk_pilih] == "Game":
            userId = int(input("{}{:^36}{}\n\n > ".format(colorList[1],"Masukkan User Id",colorList[0])))
            while True:
                clear()
                printTopupMachine()
                print("{:^35}".format("Masukkan nominal kelipatan Rp5000"))
                jumlah = int(input("{}{:^36}{}\n\n > ".format(colorList[1],f"yang akan ditukar menjadi {list_topup_names[produk_pilih]}",colorList[0])))
                if jumlah%5000 != 0:
                    reset("Uang bukan kelipatan Rp5.000",2, False)
                else:
                    clearLines(4)
                    print("{:^38}".format(f"Anda akan mendapatkan {list_topup_names[produk_pilih]} sebanyak {get_price(produk_pilih,jumlah)}"))
                    time.sleep(5)
                    break
        elif list_topup_category[produk_pilih] == "E-Wallet":
            noTlp = int(input("{}{:^36}{}\n\n > ".format(colorList[1],"Masukkan Nomor Telepon",colorList[0])))
            while True:
                clear()
                printTopupMachine()
                jumlah = int(input("{}{:^36}{}\n\n > ".format(colorList[1],f"Masukkan nominal kelipatan Rp5000",colorList[0])))
                if jumlah%5000 != 0:
                    reset("Nominal bukan kelipatan Rp5.000",2, False)
                else:
                    break
        clear()
        printTopupMachine()
        time.sleep(1)
        print("{:^35}".format("Pilih metode pembayaran"))
        metode_pembayaran = int(input("{:^45}\n\n> ".format(colorList[1]+"QRIS (1) / Cash (2) / E-Money (3)"+colorList[0])))
        if metode_pembayaran == 1:
            if QrisPayment(jumlah) == True:
                continue
            clear()
            printTopupMachine()
        elif metode_pembayaran == 2:
            CashPayment(jumlah) 
        elif metode_pembayaran == 3:
            EMoneyPayment(jumlah)
        else :
            reset("Input tidak valid",2)
            continue
        reset("Thank you and enjoy!",5)
        continue

    elif opsi == 2:
        printVendingMachine()
        masukan = int(input("{}{:^36}{}\n\n > ".format(colorList[1],"Masukkan Id Produk",colorList[0])))
        n=len(list_produk)
        for i in range(n):
            if list_produk_angka[i] == masukan :
                produk_pilih = i
                if list_jumlah_produk[produk_pilih] >= 1:
                    clear()
                    printVendingMachine()
                    print("{:^35}".format("Pilih metode pembayaran"))
                    metode_pembayaran = int(input("{:^45}\n\n> ".format(colorList[1]+"QRIS (1) / Cash (2)"+colorList[0])))
                    if metode_pembayaran == 1:
                        if QrisPayment(list_harga[produk_pilih]) == True:
                            break
                        clear()
                        print("╔═══════════════════════════════════╗")
                        print("║{}{:^35}{}║".format(colorList[2],"Vending Machine",colorList[0]))
                        print("╠════╦════════════════════╦═════════╣")
                        print("║ Id ║ Product            ║ Price   ║")
                        print("╠════╬════════════════════╬═════════╣")
                        animateDrop()
                        reset("Thank you and enjoy!",5)
                        break
                    elif metode_pembayaran == 2:
                        CashPayment(list_harga[produk_pilih]) 
                        clearLines(23)
                        animateDrop()
                        reset("Thank you and enjoy!",5)
                        break
                    elif metode_pembayaran == 3:
                        EMoneyPayment(list_harga[produk_pilih])
                        reset("Thank you and enjoy!",5)
                        break
                    else:
                        reset("Input tidak valid",2)
                        break
                else:
                    reset("Stok habis, silakan pilih produk lain",2)
                    break
            elif i == n-1:
                break
    else: 
        reset("Input tidak valid",2)
        continue
