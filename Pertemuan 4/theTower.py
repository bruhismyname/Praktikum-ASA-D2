def cek_mencapai_puncak(N, P, G):
    kekuatan_pahlawan = P
    
    for kekuatan_penjaga in G:
        if kekuatan_pahlawan >= kekuatan_penjaga:
            kekuatan_pahlawan += kekuatan_penjaga
        else:
            return "NO"
    
    return "YES"

N, P = map(int, input().split())
G = list(map(int, input().split()))
print(cek_mencapai_puncak(N, P, G))