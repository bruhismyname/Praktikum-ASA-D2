def koefisien_ketidakbahagiaan_minimum(n, k, kuda):
    jumlah_hitam = [0] * k
    jumlah_putih = [0] * k
    
    for i in range(n):
        indeks_kandang = i % k
        if kuda[i] == 1:  
            jumlah_hitam[indeks_kandang] += 1
        else:  
            jumlah_putih[indeks_kandang] += 1
    
    total_ketidakbahagiaan = 0
    for i in range(k):
        total_ketidakbahagiaan += jumlah_hitam[i] * jumlah_putih[i]
    
    return total_ketidakbahagiaan

n, k = map(int, input().split())
kuda = []
for _ in range(n):
    kuda.append(int(input()))
print(koefisien_ketidakbahagiaan_minimum(n, k, kuda))