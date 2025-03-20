def pecahan_uang(hasil):
    pecahan = [50, 25, 10, 5, 1]
    
    count = 0

    for uang in pecahan:
        count += hasil // uang
        hasil = hasil % uang
    return count

X = int(input())
print(pecahan_uang(X))