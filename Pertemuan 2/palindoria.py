def cek_palindrom(kata):
    frek = {}
    for h in kata:
        if h in frek:
            frek[h] += 1
        else:
            frek[h] = 1
    
    ganjil = 0
    for nilai in frek.values():
        if nilai % 2 != 0:
            ganjil += 1
    if ganjil > 1:
        return ["Kabur!"]

    hasil = []

    def permutasi(sisa_huruf, saat_ini):
        if len(sisa_huruf) == 0:
            tengah = ""
            for h, n in frek.items():
                if n % 2 != 0:
                    tengah = h
            palindrom = saat_ini + tengah + saat_ini[::-1]
            hasil.append(palindrom)
            return
        
        pakai = set()
        for i in range(len(sisa_huruf)):
            if sisa_huruf[i] not in pakai:
                pakai.add(sisa_huruf[i])
                new_sisa = sisa_huruf[:i] + sisa_huruf[i+1:]
                permutasi(new_sisa, saat_ini + sisa_huruf[i])
    
    setengah = []
    for h in sorted(frek.keys()):
        setengah.extend([h] * (frek[h] // 2))
    
    permutasi(setengah, "")
    return sorted(hasil)

kata = input()
jawaban = cek_palindrom(kata)
print(" ".join(jawaban))