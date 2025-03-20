def cek_baik(s):
    for c in set(s.lower()):
        if c.isalpha() and (c.lower() not in s or c.upper() not in s):
            return False
    return True

def solusi(s):
    terpanjang = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if cek_baik(substring) and len(substring) > len(terpanjang):
                terpanjang = substring
    return terpanjang

s = input().strip()
print(solusi(s))