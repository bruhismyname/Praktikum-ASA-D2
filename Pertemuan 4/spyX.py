def waktu_minimum(ranks, clue):
    def bisa_kumpulkan(waktu):
        petunjuk_terkumpul = 0
        for r in ranks:
            n = 0
            while (r * (n + 1) ** 2) <= waktu:
                n += 1
                petunjuk_terkumpul += 1
                if petunjuk_terkumpul >= clue:
                    return True
        return False
    
    kiri, kanan = 1, max(ranks) * clue ** 2
    hasil = kanan
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if bisa_kumpulkan(tengah):
            hasil = tengah
            kanan = tengah - 1
        else:
            kiri = tengah + 1
    return hasil

ranks = list(map(int, input().split()))
clue = int(input())
print(waktu_minimum(ranks, clue))