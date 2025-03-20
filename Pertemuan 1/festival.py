def foto_vestival():
    baris, kolom = map(int, input().strip().split())
    matriks = [list(map(int, input().strip().split())) for _ in range(baris)]
    
 
    hasil = [-float('inf'), 0, 0, 0] 
    psum = [[0]*(kolom + 1) for _ in range(baris + 1)]
    
    for i in range(baris):
        for j in range(kolom):
            psum[i+1][j+1] = (matriks[i][j] + psum[i+1][j] + 
                             psum[i][j+1] - psum[i][j])

    for uk in range(1, min(baris, kolom) + 1):
        for i in range(baris - uk + 1):
            for j in range(kolom - uk + 1):
                kualitas = (psum[i+uk][j+uk] - psum[i][j+uk] - 
                          psum[i+uk][j] + psum[i][j])
                
                if (kualitas > hasil[0] or 
                    (kualitas == hasil[0] and uk > hasil[1]) or
                    (kualitas == hasil[0] and uk == hasil[1] and i < hasil[2]) or
                    (kualitas == hasil[0] and uk == hasil[1] and 
                     i == hasil[2] and j < hasil[3])):
                    hasil = [kualitas, uk, i, j]
    
    print(hasil[0], hasil[1], hasil[2] + 1, hasil[3] + 1)
foto_vestival()