def infinity_kost(n):
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    kolom = []

    for j in range(1, n):
        x = int((j*(j+1))/2)
        kolom.append(x)

    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idxFibonaci = 0
    idxHuruf = 0
    hasil = []
    if n == 2:
        return "1 A"
    else:
        for k in range(1, n + 1):
            if k + 1 in kolom:
                hasil.append(str(huruf[idxHuruf]))
                idxHuruf += 1
            else:
                hasil.append(str(fibonacci[idxFibonaci]))
                idxFibonaci += 1
        return " ".join(hasil)

n = int(input().strip())
print(infinity_kost(n))