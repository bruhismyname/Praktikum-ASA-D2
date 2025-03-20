def prediksi_juara(arr):
    def optimal(kiri, kanan, giliran):
        if kiri > kanan:
            return 0
        
        if giliran:
            return max(
                arr[kiri] + optimal(kiri + 1, kanan, False),
                arr[kanan] + optimal(kiri, kanan - 1, False)
            )
        else:
            return min(
                optimal(kiri + 1, kanan, True),
                optimal(kiri, kanan - 1, True)
            )

    total = sum(arr)
    chuuya_skor = optimal(0, len(arr) - 1, True)
    akutagawa_skor = total - chuuya_skor

    return chuuya_skor >= akutagawa_skor

arr = list(map(int, input().split()))
print(prediksi_juara(arr))