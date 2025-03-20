def petualangan(angka):
    if len(angka) == 0:
        return 1
    if len(angka) == 1:
        return 1 if angka[0] != '0' else 0

    if angka[0] == '0':
        return 0

    hasil = petualangan(angka[1:])

    if int(angka[:2]) <= 26:
        hasil += petualangan(angka[2:])
    return hasil

print(petualangan(input().strip()))