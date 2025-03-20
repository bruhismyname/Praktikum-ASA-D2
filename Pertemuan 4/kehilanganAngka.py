def cari_angka_terbesar_yang_hilang(n, arr):
    set_yang_diharapkan = set(range(n + 1))
    set_yang_ada = set(arr)
    angka_yang_hilang = set_yang_diharapkan - set_yang_ada
    return max(angka_yang_hilang)

n = int(input())
arr = list(map(int, input().split()))
hasil = cari_angka_terbesar_yang_hilang(n, arr)
print(hasil)