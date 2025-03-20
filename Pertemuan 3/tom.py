def cari_tikus_terberat_k(tikus, k):
    k = len(tikus) - k
    
    def partisi(arr, kiri, kanan):
        pivot = arr[kanan]
        i = kiri - 1
        
        for j in range(kiri, kanan):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[kanan] = arr[kanan], arr[i + 1]
        return i + 1
    
    def quickselect(arr, kiri, kanan, k):
        if kiri == kanan:
            return arr[kiri]
        
        pos_pivot = partisi(arr, kiri, kanan)
        
        if pos_pivot == k:
            return arr[k]
        elif k < pos_pivot:
            return quickselect(arr, kiri, pos_pivot - 1, k)
        else:
            return quickselect(arr, pos_pivot + 1, kanan, k)
    
    return quickselect(tikus, 0, len(tikus) - 1, k)

N, K = map(int, input().split())
berat_tikus = list(map(int, input().split()))
print(cari_tikus_terberat_k(berat_tikus, K))