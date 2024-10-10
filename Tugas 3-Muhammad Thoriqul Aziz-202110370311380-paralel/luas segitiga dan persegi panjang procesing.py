from multiprocessing import Process

# Fungsi menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'Luas Segitiga: {luas}')

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f'Luas Persegi Panjang: {luas}')

def main():
    process1 = Process(target=luas_segitiga, args=(20, 3))
    
    process2 = Process(target=luas_persegi_panjang, args=(30, 6))
    

    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

if __name__ == "__main__":
    main()
