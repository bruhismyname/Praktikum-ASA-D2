def cari_energi(n, klts):
    min_klty = min(klts)
    max_klty = max(klts)
    
    min_energi = float('inf')
    
    for i in range(min_klty, max_klty + 1):
        ttl_energi = 0
        for j in klts:
            ttl_energi += abs(j - i)
        min_energi = min(min_energi, ttl_energi)
    return min_energi

n = int(input())
klts = list(map(int, input().split()))
print(cari_energi(n, klts))