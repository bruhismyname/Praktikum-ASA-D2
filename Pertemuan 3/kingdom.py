def cari_nilai_maksimum(arr, awal, akhir):
    if awal == akhir:
        return arr[awal]
    
    tengah = (awal + akhir) // 2
    maksimum_kiri = cari_nilai_maksimum(arr, awal, tengah)
    maksimum_kanan = cari_nilai_maksimum(arr, tengah + 1, akhir)
    return max(maksimum_kiri, maksimum_kanan)

n = int(input())
ukuran_gua = list(map(int, input().split()))
hasil = cari_nilai_maksimum(ukuran_gua, 0, n - 1)
print(hasil)