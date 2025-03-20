def cari_nilai_maksimum(N, A):
    nilai_maksimum = A[0]
    nilai_maksimum_saat_ini = A[0]

    for i in range(1, N):
        nilai_maksimum_saat_ini = max(A[i], nilai_maksimum_saat_ini + A[i])
        nilai_maksimum = max(nilai_maksimum, nilai_maksimum_saat_ini)
    return nilai_maksimum

N = int(input())
A = list(map(int, input().split()))
print(cari_nilai_maksimum(N, A))