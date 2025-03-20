def find_egg_cartons(target_sum, n, cartons):
    complement_dict = {}

    for i in range(n):
        current = cartons[i]
        complement = target_sum - current
        if complement in complement_dict:
            return [complement_dict[complement], i]
        complement_dict[current] = i
    return []  

X = int(input())  
N = int(input())  
A = list(map(int, input().split())) 

result = find_egg_cartons(X, N, A)
print(f"{result[0]} {result[1]}")