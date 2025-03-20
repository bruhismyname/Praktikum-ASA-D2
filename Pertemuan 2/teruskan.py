def cari_angka(arr, target, index=0):
    if index >= len(arr):
        return "Tidak ditemukan"
    if arr[index] == target:
        return index
    return cari_angka(arr, target, index + 1)

try:
    input_str = input().strip()
    arr = eval(input_str)  
    target = int(input()) 
    result = cari_angka(arr, target)
    print(result)

except:
    print("Tidak ditemukan")