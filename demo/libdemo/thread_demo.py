import threading


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 20):
            print(f"Print: {i}")


print(threading.main_thread())
t = PrintThread()
t.start()

for i in range(1, 20):
    print(f"Main {i}")


