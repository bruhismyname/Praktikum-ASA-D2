def cari_puncak(arr):
    kiri = 0
    kanan = len(arr) - 1
    
    while kiri < kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] < arr[tengah + 1]:
            kiri = tengah + 1
        else:
            kanan = tengah
    
    return kiri + 1

n = int(input())
arr = list(map(int, input().split()))
indeks_puncak = cari_puncak(arr)
print(indeks_puncak)