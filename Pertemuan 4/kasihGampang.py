def cari_biner(daftar, target):
    if not daftar:
        return '"Tidak ditemukan"'
    
    urut_naik = len(daftar) <= 1 or daftar[0] <= daftar[-1]
    
    kiri, kanan = 0, len(daftar) - 1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        
        if daftar[tengah] == target:
            return tengah
        
        if urut_naik:
            if daftar[tengah] < target:
                kiri = tengah + 1
            else:
                kanan = tengah - 1
        else:
            if daftar[tengah] < target:
                kanan = tengah - 1
            else:
                kiri = tengah + 1
    
    return '"Tidak ditemukan"'

input_daftar = input().strip()
target = int(input().strip())

if input_daftar == "[]":
    daftar = []
else:
    daftar = [int(x) for x in input_daftar[1:-1].split(",")]

hasil = cari_biner(daftar, target)
print(hasil)