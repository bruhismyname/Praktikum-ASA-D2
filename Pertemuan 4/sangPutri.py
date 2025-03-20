def temukan_koin_palsu(koin_koin, awal, akhir):
    if awal == akhir:
        return awal
    
    if awal + 1 == akhir:
        if koin_koin[awal] < koin_koin[akhir]:
            return awal
        else:
            return akhir
    
    tengah = (awal + akhir) // 2
    
    koin_kiri_count = tengah - awal + 1
    koin_kanan_count = akhir - tengah
    
    berat_kiri = sum(koin_koin[awal:tengah + 1])
    berat_kanan = sum(koin_koin[tengah + 1:akhir + 1])
    
    rata_kiri = berat_kiri / koin_kiri_count
    rata_kanan = berat_kanan / koin_kanan_count
    
    if rata_kiri < rata_kanan:
        return temukan_koin_palsu(koin_koin, awal, tengah)
    else:
        return temukan_koin_palsu(koin_koin, tengah + 1, akhir)

N = int(input())
koin_koin = list(map(int, input().split()))
indeks_koin_palsu = temukan_koin_palsu(koin_koin, 0, N - 1)
print(indeks_koin_palsu)