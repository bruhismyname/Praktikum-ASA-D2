def cek_pembentukan_kata(karakter_tersedia, kode_ascii):
    kata_target = ''
    for kode in kode_ascii:
        kata_target += chr(kode)
    
    dict_tersedia = {}
    for karakter in karakter_tersedia:
        if karakter in dict_tersedia:
            dict_tersedia[karakter] += 1
        else:
            dict_tersedia[karakter] = 1
    
    dict_target = {}
    for karakter in kata_target:
        if karakter in dict_target:
            dict_target[karakter] += 1
        else:
            dict_target[karakter] = 1
    
    bisa_dibentuk = True
    for karakter in dict_target:
        if karakter not in dict_tersedia or dict_tersedia[karakter] < dict_target[karakter]:
            bisa_dibentuk = False
            break
    print("Bisa" if bisa_dibentuk else "Tidak")
    
    if not bisa_dibentuk:
        hasil = ""
        hitung_karakter = {}
        for karakter in kata_target:
            if karakter not in hitung_karakter:
                hitung_karakter[karakter] = 0
            hitung_karakter[karakter] += 1
            if karakter in dict_tersedia and hitung_karakter[karakter] <= dict_tersedia[karakter]:
                hasil += karakter
            else:
                break
        print(hasil)
    else:
        print(kata_target)

karakter_tersedia = input().strip()
kode_ascii = list(map(int, input().strip().split()))
cek_pembentukan_kata(karakter_tersedia, kode_ascii)