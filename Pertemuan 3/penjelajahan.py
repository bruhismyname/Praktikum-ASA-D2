def cari_jalur(data, kiri, kanan):
    if kanan - kiri == 1:
        return abs(data[kiri][0] - data[kanan][0]), min(data[kiri][1], data[kanan][1])

    tengah = (kiri + kanan) // 2

    sel_kiri, idx_kiri = cari_jalur(data, kiri, tengah)
    sel_kanan, idx_kanan = cari_jalur(data, tengah, kanan)  

    if sel_kiri < sel_kanan:
        return sel_kiri, idx_kiri
    elif sel_kiri > sel_kanan:
        return sel_kanan, idx_kanan
    else:
        return sel_kiri, min(idx_kiri, idx_kanan)

def analisis(n, tinggi):
    titik = [(tinggi[i], i + 1) for i in range(n)]
    titik.sort()

    sel_min, idx_min = cari_jalur(titik, 0, n - 1)
    print(sel_min, idx_min)

n = int(input())
tinggi = list(map(int, input().split()))
analisis(n, tinggi)