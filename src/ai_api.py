from sql import connect,update
from threading import Thread
import time

def fc():
    while True:
        update(20)
        time.sleep(5)

def main():
    connect()
    t = Thread(target=fc)
    t.start()