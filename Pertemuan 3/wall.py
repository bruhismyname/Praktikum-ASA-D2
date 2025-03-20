def wall(jadwal):
    if not jadwal:
        return 0
    
    def urutkan(data):
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i][0] > data[j][0]:
                    data[i], data[j] = data[j], data[i]
                    
    def tidak_bertabrakan(koleksi, objek_baru):
        for item in koleksi:
            for obj in objek_baru:
                if not (item[1] < obj[0] or obj[1] < item[0]):
                    return False
        return True
    
    def kombinasikan(bagian_awal, bagian_akhir):
        semua_kelompok = bagian_awal + bagian_akhir
        urutkan(semua_kelompok)
        
        kelompok_hasil = []
        for kelompok in semua_kelompok:
            sudah_ditempatkan = False
            for i in range(len(kelompok_hasil)):
                if tidak_bertabrakan(kelompok_hasil[i], kelompok):
                    kelompok_hasil[i] = kelompok_hasil[i] + kelompok
                    sudah_ditempatkan = True
                    break

            if not sudah_ditempatkan:
                kelompok_hasil.append(kelompok)  
        return kelompok_hasil

    def bagi_dan_kuasai(data):
        if len(data) == 1:
            return [[data[0]]]
        
        titik_tengah = len(data) // 2
        bagian_kiri = bagi_dan_kuasai(data[:titik_tengah])
        bagian_kanan = bagi_dan_kuasai(data[titik_tengah:])
        return kombinasikan(bagian_kiri, bagian_kanan)
    
    urutkan(jadwal)
    pembagian_akhir = bagi_dan_kuasai(jadwal)
    return len(pembagian_akhir)

data_jadwal = eval(input())
print(wall(data_jadwal))