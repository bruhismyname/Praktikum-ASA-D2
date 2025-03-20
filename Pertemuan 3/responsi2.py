def banyak_gold(N, K, peti_emas):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = dp[i-1][j]
            
            if j >= peti_emas[i-1]:
                dp[i][j] = max(dp[i][j], 
                             dp[i-1][j-peti_emas[i-1]] + peti_emas[i-1])
    
    return dp[N][K]

N, K = map(int, input().split())
peti_emas = list(map(int, input().split()))

print(banyak_gold(N, K, peti_emas))