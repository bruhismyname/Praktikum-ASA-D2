def penghitungan_spesial(angka):
    if len(angka) % 2 == 0:
        return sum(angka)
    else:
        index_tengah = len(angka) // 2
        angka_tengah = angka[index_tengah]
        sisa_penjumlahan = sum(angka[:index_tengah]) + sum(angka[index_tengah + 1:])
        return sisa_penjumlahan * angka_tengah

input_angka = list(map(int, input().strip().split()))
hasil = penghitungan_spesial(input_angka)
print(hasil)