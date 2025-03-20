def buat_kode(n, kode="", angka_sblmy='0'):
    if len(kode) == n:
        return [kode]
    
    hasil = []

    hasil.extend(buat_kode(n, kode + "0", '0'))
    
    if angka_sblmy != '1':
        hasil.extend(buat_kode(n, kode + "1", '1'))
    return hasil

def program():
    n = int(input())
    hasil = buat_kode(n)
    hasil.sort()
    print(" ".join(hasil))

program()