def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def proses_array(arr, pilihan):
    total = 0
    for num in arr:
        if pilihan == 1:  
            total += fibonacci(num)
        else:  
            total += factorial(num)
    return total

n = int(input())
arr = list(map(int, input().split()))
pilihan = int(input())
print(proses_array(arr, pilihan))