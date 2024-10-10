import multiprocessing
from multiprocessing import Barrier, Lock
from time import time
from datetime import datetime

# Fungsi yang akan dijalankan oleh proses
def test_dengan_barrier(synchronizer, serializer, i):
    # Menunggu semua proses mencapai barrier
    synchronizer.wait()
    
    # Mendapatkan waktu sekarang
    now = time()
    
    with serializer:
        # Hanya mencetak angka genap
        if i % 2 == 0:
            print(f"Dengan Barrier process ke: {i}, waktu: {datetime.fromtimestamp(now)}")

if __name__ == '__main__':
    # Menjalankan eksekusi 3 kali
    for execution in range(3):
        print(f"Eksekusi ke-{execution + 1}")
        
        # Membuat barrier untuk 10 proses dan lock untuk serialisasi output
        synchronizer = Barrier(10)
        serializer = Lock()

        processes = []

        # Membuat dan memulai 10 proses
        for i in range(10):
            p = multiprocessing.Process(target=test_dengan_barrier, args=(synchronizer, serializer, i))
            p.start()
            processes.append(p)  # Menambahkan proses ke dalam list

        for p in processes:
            p.join()
        
        print("-" * 40)  # Pemisah antar eksekusi
