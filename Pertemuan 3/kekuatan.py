def cari(arr, awal, akhir):
    if awal == akhir:
        return arr[awal]
    
    tengah = (awal + akhir) // 2
    
    kiri = cari(arr, awal, tengah)
    kanan = cari(arr, tengah + 1, akhir)
    
    if kiri == kanan:
        return kiri
    
    hitung_kiri = sum(1 for i in range(awal, akhir + 1) if arr[i] == kiri)
    hitung_kanan = sum(1 for i in range(awal, akhir + 1) if arr[i] == kanan)
    
    return kiri if hitung_kiri > hitung_kanan else kanan

n = int(input())
arr = list(map(int, input().split()))

calon = cari(arr, 0, n - 1)
jumlah = arr.count(calon)

print(calon if jumlah > n//2 else -1)