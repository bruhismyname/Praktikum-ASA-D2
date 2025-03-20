def cek_ekuivalen(a, b):
    if len(a) % 2 == 1:
        return a == b

    if a == b:
        return True

    n = len(a)
    tengah = n // 2

    a1, a2 = a[:tengah], a[tengah:]
    b1, b2 = b[:tengah], b[tengah:]
    kondisi1 = cek_ekuivalen(a1, b1) and cek_ekuivalen(a2, b2)
    kondisi2 = cek_ekuivalen(a1, b2) and cek_ekuivalen(a2, b1)

    return kondisi1 or kondisi2

string1 = input().strip()
string2 = input().strip()

if len(string1) != len(string2):
    print("TIDAK")
else:
    hasil = cek_ekuivalen(string1, string2)
    print("YA" if hasil else "TIDAK")