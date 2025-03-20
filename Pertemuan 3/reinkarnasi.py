def nilai_total_maksimum(n, k, kue):
    nilai_kotak = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for mulai in range(n):
        jenis_unik = set()
        for akhir in range(mulai, n):
            jenis_unik.add(kue[akhir])
            nilai_kotak[mulai][akhir+1] = len(jenis_unik)
    dp = [[-float('inf') for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 0

    for j in range(1, k+1):  
        for i in range(1, n+1):  
            for prev in range(i): 
                if dp[prev][j-1] != -float('inf'):
                    dp[i][j] = max(dp[i][j], dp[prev][j-1] + nilai_kotak[prev][i])
    
    return dp[n][k]

n, k = map(int, input().split())
kue = list(map(int, input().split()))
print(nilai_total_maksimum(n, k, kue))