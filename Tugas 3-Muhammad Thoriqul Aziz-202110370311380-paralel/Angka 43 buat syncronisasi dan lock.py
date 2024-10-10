import multiprocessing
import time

# Inisialisasi awal lock
kunci = multiprocessing.Lock()
# Variabel awal
x = multiprocessing.Value('d', 334.0)  # 'd' untuk tipe data double (float)

def double(x):
    while True:
        kunci.acquire()
        if x.value < 1634:
            x.value *= 2
            print(f"Double: {x.value}")
        else:
            print("Maksimum")
            kunci.release()
            break
        kunci.release()
        time.sleep(2)

def halve(x):
    while True:
        kunci.acquire()
        if x.value > 1:
            x.value /= 2
            print(f"Halve: {x.value}")
        else:
            print("Minimum")
            kunci.release()
            break
        kunci.release()
        time.sleep(3)


if __name__ == '__main__':
    # Membuat dua proses
    p1 = multiprocessing.Process(target=halve, args=(x,))
    p2 = multiprocessing.Process(target=double, args=(x,))
    
    # Menjalankan proses
    p1.start()
    p2.start()
    
    # Menunggu kedua proses selesai
    p1.join()
    p2.join()
