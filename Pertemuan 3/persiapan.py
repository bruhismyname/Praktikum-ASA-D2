def hitung_kombinasi(nums1, nums2):
    n = len(nums1)
    posisi1 = {}
    posisi2 = {}
    for i in range(n):
        posisi1[nums1[i]] = i
        posisi2[nums2[i]] = i
    
    hasil = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                nilai_i = nums1[i]
                nilai_j = nums1[j]
                nilai_k = nums1[k]
                
                if posisi2[nilai_i] < posisi2[nilai_j] < posisi2[nilai_k]:
                    hasil += 1
    
    return hasil

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(hitung_kombinasi(nums1, nums2))