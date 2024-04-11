import threading
from threading import Thread


def print_numbers():
    for i in range(1, 20):
        print(f"Print: {i}")


print(threading.main_thread())
t = Thread(target=print_numbers)
t.start()

for i in range(1, 20):
    print(f"Main {i}")
