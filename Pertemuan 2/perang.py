def hitung_minimum_boss(target_lantai, batas_loncatan, lantai_sekarang, memo):
    if lantai_sekarang == target_lantai:
        return 0
    if lantai_sekarang in memo:
        return memo[lantai_sekarang]
    
    loncatan_tersedia = False
    hasil_terbaik = float('inf')
    faktor = 2

    while True:
        lantai_tujuan = lantai_sekarang * faktor
       
        if lantai_tujuan > target_lantai or (lantai_tujuan - lantai_sekarang) > batas_loncatan:
            break
        loncatan_tersedia = True
        hasil_terbaik = min(hasil_terbaik, 1 + hitung_minimum_boss(target_lantai, batas_loncatan, lantai_tujuan, memo))
        faktor += 1

    if not loncatan_tersedia:
        hasil_terbaik = target_lantai - lantai_sekarang

    memo[lantai_sekarang] = hasil_terbaik
    return hasil_terbaik


jumlah_lantai, batas_loncatan, posisi_awal = map(int, input().split())
print(hitung_minimum_boss(jumlah_lantai, batas_loncatan, posisi_awal, {}))