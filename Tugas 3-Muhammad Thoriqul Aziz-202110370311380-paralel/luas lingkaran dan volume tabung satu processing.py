from multiprocessing import Process
import math

# Fungsi menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    luas = math.pi * (jari_jari ** 2)
    print(f'Luas Lingkaran: {luas}')

def volume_tabung(jari_jari, tinggi):
    volume = math.pi * (jari_jari ** 2) * tinggi
    print(f'Volume Tabung: {volume}')

def main():

    process1 = Process(target=luas_lingkaran, args=(21,))  # Misalkan jari-jari = 7
    
    process2 = Process(target=volume_tabung, args=(14, 5))  
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

if __name__ == "__main__":
    main()
