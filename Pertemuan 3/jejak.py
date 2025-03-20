def cari_jejak(arr, target):
    indeks_awal = -1
    indeks_akhir = -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            if indeks_awal == -1:
                indeks_awal = i + 1  
            indeks_akhir = i + 1
    
    return indeks_awal, indeks_akhir

n, k = map(int, input().split())
log_kedatangan = list(map(int, input().split()))
awal, akhir = cari_jejak(log_kedatangan, k)

if awal == -1:
    print("-1 -1")
else:
    print(f"{awal} {akhir}")