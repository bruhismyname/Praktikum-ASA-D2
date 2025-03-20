def cari_selisih_minimum(n, berat):
    total = sum(berat)
    dp = [[False for j in range(total + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(total + 1):
            if berat[i-1] <= j:
                dp[i][j] = dp[i-1][j-berat[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    selisih_min = float('inf')
    for j in range(total // 2 + 1):
        if dp[n][j]:
            selisih_min = min(selisih_min, total - 2*j)
    
    return selisih_min

n = int(input())  
berat = list(map(int, input().split())) 
print(cari_selisih_minimum(n, berat))