def cari_beda_ketinggian(n, ketinggian):
    titik_ekstrim = []
    
    if n < 2:
        return 0
    
    titik_ekstrim.append((ketinggian[0], 'puncak' if ketinggian[0] >= ketinggian[1] else 'lembah'))
    
    for i in range(1, n-1):
        if ketinggian[i] >= ketinggian[i-1] and ketinggian[i] >= ketinggian[i+1]:
            if ketinggian[i] > ketinggian[i-1] or ketinggian[i] > ketinggian[i+1]:
                titik_ekstrim.append((ketinggian[i], 'puncak'))
        elif ketinggian[i] <= ketinggian[i-1] and ketinggian[i] <= ketinggian[i+1]:
            if ketinggian[i] < ketinggian[i-1] or ketinggian[i] < ketinggian[i+1]:
                titik_ekstrim.append((ketinggian[i], 'lembah'))
    
    titik_ekstrim.append((ketinggian[-1], 'puncak' if ketinggian[-1] >= ketinggian[-2] else 'lembah'))

    return max(abs(titik_ekstrim[i][0] - titik_ekstrim[i+1][0]) 
              for i in range(len(titik_ekstrim)-1))

n = int(input())
ketinggian = list(map(int, input().split()))
print(cari_beda_ketinggian(n, ketinggian))