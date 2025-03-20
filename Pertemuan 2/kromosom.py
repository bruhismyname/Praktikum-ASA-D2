def hitung_pasangan(kromosom, index=0):
    if index >= len(kromosom) - 1:
        return 0
    if kromosom[index] == 'X' and kromosom[index + 1] == 'Y':
        return 1 + hitung_pasangan(kromosom, index + 2)
    return hitung_pasangan(kromosom, index + 1)

def cephalopod(kromosom):
    total_xy = hitung_pasangan(kromosom)
    return total_xy > 0 and total_xy % 2 == 0

kromosom = input().strip()
print(cephalopod(kromosom))