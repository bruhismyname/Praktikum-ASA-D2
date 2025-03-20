def kekuatan(N, K, benteng):
    if K > N:
        return "Banyaknya benteng tidak cukup dengan yang dibutuhkan"
    if K == 0:
        return "Luffy Kalah"

    jmlh_skrg = sum(benteng[:K])
    maks_kekuatan = jmlh_skrg
    for i in range(K, N):
        jmlh_skrg = jmlh_skrg - benteng[i-K] + benteng[i]
        maks_kekuatan = max(maks_kekuatan, jmlh_skrg)
    return maks_kekuatan

N = int(input())  
K = int(input())  
benteng = list(map(int, input().replace(',', '').split()))
hasil = kekuatan(N, K, benteng)
print(hasil)