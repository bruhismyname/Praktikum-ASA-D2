def jumlah_gol(N):
    jumlah = 0
    while N:
        jumlah += N & 1  
        N >>= 1         
    return jumlah

N = int(input())
print(jumlah_gol(N))