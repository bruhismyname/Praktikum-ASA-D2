def cari_energi(n, kualitas):
    min_kuality = min(kualitas)
    max_kuality = max(kualitas)

    min_energi = float('inf')

    for i in range(min_kuality, max_kuality + 1):
        total_energi = 0
        for kuality in kualitas:
            total_energi += abs(kuality - i)
        min_energi = min(min_energi, total_energi)
    return min_energi

n = int(input())
kualitas = list(map(int, input().split()))
print(cari_energi(n, kualitas))