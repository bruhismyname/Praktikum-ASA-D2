def hitung_max_gold(N, K, peti_emas):
    # Buat tabel DP berukuran N+1 x K+1
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Isi tabel DP
    for i in range(1, N + 1):
        for j in range(K + 1):
            # Tidak mengambil peti saat ini
            dp[i][j] = dp[i-1][j]
            
            # Ambil peti saat ini jika memungkinkan
            if j >= peti_emas[i-1]:
                dp[i][j] = max(dp[i][j], 
                             dp[i-1][j-peti_emas[i-1]] + peti_emas[i-1])
    
    return dp[N][K]

# Baca input
N, K = map(int, input().split())
peti_emas = list(map(int, input().split()))

# Cetak hasil
print(hitung_max_gold(N, K, peti_emas))