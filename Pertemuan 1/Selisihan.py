def find_min_difference(numbers):
    numbers.sort()

    min_diff = float('inf')

    for i in range(1, len(numbers)):
        current_diff = numbers[i] - numbers[i-1]
        min_diff = min(min_diff, current_diff)
    
    return min_diff

numbers = list(map(int, input().strip().split()))
print(find_min_difference(numbers))