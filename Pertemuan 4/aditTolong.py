def jumlah_bola_minimum(nilai_bola, H):
    dp = [float('inf')] * (H + 1)
    dp[0] = 0  
    
    for bola in nilai_bola:
        for i in range(bola, H + 1):
            if dp[i - bola] != float('inf'):
                dp[i] = min(dp[i], dp[i - bola] + 1)
    
    return dp[H] if dp[H] != float('inf') else -1

N, H = map(int, input().split())
nilai_bola = list(map(int, input().split()))
print(jumlah_bola_minimum(nilai_bola, H))