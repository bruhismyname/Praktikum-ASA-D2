def hitung_inversi(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_dan_hitung(arr, temp_arr, 0, len(arr) - 1)

def merge_sort_dan_hitung(arr, temp_arr, kiri, kanan):
    jumlah_inversi = 0
    
    if kiri < kanan:
        tengah = (kiri + kanan) // 2
        jumlah_inversi += merge_sort_dan_hitung(arr, temp_arr, kiri, tengah)
        jumlah_inversi += merge_sort_dan_hitung(arr, temp_arr, tengah + 1, kanan)
        jumlah_inversi += gabung_dan_hitung(arr, temp_arr, kiri, tengah, kanan)
    
    return jumlah_inversi

def gabung_dan_hitung(arr, temp_arr, kiri, tengah, kanan):
    i = kiri      
    j = tengah + 1   
    k = kiri      
    jumlah_inversi = 0
    
    while i <= tengah and j <= kanan:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            jumlah_inversi += (tengah - i + 1)
            j += 1
        k += 1
    
    while i <= tengah:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= kanan:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(kiri, kanan + 1):
        arr[i] = temp_arr[i]
    
    return jumlah_inversi

n = int(input())
nilai = list(map(int, input().split()))
print(hitung_inversi(nilai))