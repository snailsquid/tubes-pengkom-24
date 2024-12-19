import random
import time
def end():
    print("restarting")
def createQris(price):
    ownerId = ""
    print(f"creating QRIS with price: {price} to account {ownerId}")
    time.sleep(1)
    percentFail = 1
    if random.randint(1,100)<=percentFail:
        end()
        return
    else:
        print("QRIS created successfully")
        display_qr()
        wait_payment()
def display_qr():
    print("displaying QR")
    return
def wait_payment():
    print("waiting for payment...")
    if(true):
        print("payment received")
        push_product()

