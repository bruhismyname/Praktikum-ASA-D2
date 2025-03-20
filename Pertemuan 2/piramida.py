def piramid(base):
    n = len(base)
    if n == 1:
        return [base]
    
    level_slnjtny = []
    for i in range(n-1):
        level_slnjtny.append(base[i] + base[i+1])
    
    level_ats = piramid(level_slnjtny)
    level_ats.append(base)
    
    return level_ats

n = int(input())
base = list(map(int, input().split()))
pyramid = piramid(base)
for level in pyramid:
    print(*level)