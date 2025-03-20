def cariPosisiAwal(arr, target):
    kiri, kanan = 0, len(arr) - 1
    posisi_awal = -1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] < target:
            kiri = tengah + 1
        elif arr[tengah] > target:
            kanan = tengah - 1
        else: 
            posisi_awal = tengah
            kanan = tengah - 1  
    
    return posisi_awal

def cariPosisiAkhir(arr, target):
    kiri, kanan = 0, len(arr) - 1
    posisi_akhir = -1
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] < target:
            kiri = tengah + 1
        elif arr[tengah] > target:
            kanan = tengah - 1
        else:  
            posisi_akhir = tengah
            kiri = tengah + 1 
    
    return posisi_akhir

novel = list(map(int, input().split()))
volume_target = int(input())
awal = cariPosisiAwal(novel, volume_target)
akhir = cariPosisiAkhir(novel, volume_target)
print(f"[{awal}, {akhir}]")