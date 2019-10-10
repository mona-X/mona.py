import time

s = time.time()

while True:
    if ((time.time() - s) >= 5):
        print ("over 5 sec")
        break