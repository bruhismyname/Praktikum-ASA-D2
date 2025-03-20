def kali_matriks(a, b, Mod):
    hasil = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                hasil[i][j] = (hasil[i][j] + a[i][k] * b[k][j]) % Mod
    return hasil

def pangkat_matriks(m, k, Mod):
    if k == 1:
        return [[m[i][j] % Mod for j in range(2)] for i in range(2)]
    setengah = k // 2
    pangkat_setengah = pangkat_matriks(m, setengah, Mod)

    hasil = kali_matriks(pangkat_setengah, pangkat_setengah, Mod)

    if k % 2 == 1:
        hasil = kali_matriks(hasil, m, Mod)
    return hasil

def main():
    k = int(input())
    m = []
    for _ in range(2):
        baris = list(map(int, input().split()))
        m.append(baris)

    mod = 10**9 + 7

    if k == 0:
        hasil = [[1, 0], [0, 1]]
    else:
        hasil = pangkat_matriks(m, k, mod)

    for baris in hasil:
        print(' '.join(map(str, baris)))

if __name__ == '__main__':
    main()