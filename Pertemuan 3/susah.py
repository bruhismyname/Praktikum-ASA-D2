def tipe_pola(bil1, bil2, bil3):
    if bil2 - bil1 == bil3 - bil2:
        return "barisan_aritmatika"
    elif bil2 / bil1 == bil3 / bil2:
        return "barisan_geometri"
    elif bil1 + bil2 == bil3:
        return "deret_fibonacci"
    elif (bil1*2 == bil2) and (bil2*2) == bil3:
        return "pangkat_dua"
    elif semua_prima([bil1, bil2, bil3]):
        return "bilangan_prima"
    return None

def semua_prima(urutan):
    return all(isPrima(nilai) for nilai in urutan)

def isPrima(nilai):
    if nilai < 2:
        return False
    for bagi in range(2, int(nilai**0.5) + 1):
        if nilai % bagi == 0:
            return False
    return True

def cari_anomali(barisan, mulai, selesai, tipe):
    if selesai - mulai < 2:
        if tipe_pola(barisan[mulai - 1], barisan[mulai], barisan[mulai + 1]) != tipe:
            return mulai
        if tipe_pola(barisan[selesai - 1], barisan[selesai], barisan[selesai + 1]) != tipe:
            return selesai
        return -1

    tengah = (mulai + selesai) // 2
    if tipe_pola(barisan[tengah - 1], barisan[tengah], barisan[tengah + 1]) != tipe:
        return tengah

    hasil_kiri = cari_anomali(barisan, mulai, tengah, tipe)
    if hasil_kiri != -1:
        return hasil_kiri
    return cari_anomali(barisan, tengah + 1, selesai, tipe)

def solusi(barisan):
    return cari_anomali(barisan, 1, len(barisan) - 2, tipe_pola(barisan[0], barisan[1], barisan[2])) + 1

deretan = list(map(int, input().split()))
print(solusi(deretan))