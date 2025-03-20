def cari_koin(daftar_koin, target):
    if len(daftar_koin) == 0:
        return '"Tidak ditemukan"'

    for i in range(len(daftar_koin)):
        if daftar_koin[i] == target:
            return i
    return '"Tidak ditemukan"'

input_str = input().strip()
daftar_koin = []
if input_str != "[]":  
    numbers = input_str[1:-1].split(',')
    daftar_koin = [int(x) for x in numbers]

target = int(input())

print(cari_koin(daftar_koin, target))