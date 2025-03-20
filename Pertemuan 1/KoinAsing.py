def temukan_koin_berbeda(koin):
    
    for i in range(len(koin)):
        if koin.count(koin[i]) == 1:
            return i + 1

koin = input().strip()
print(temukan_koin_berbeda(koin))