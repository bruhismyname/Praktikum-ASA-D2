def cari_murid_hilang(N, murid):
    kiri, kanan = 0, N
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        
        if tengah < len(murid) and murid[tengah] == tengah:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    
    return kiri

N = int(input())
murid = list(map(int, input().split()))
print(cari_murid_hilang(N, murid))