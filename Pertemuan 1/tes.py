def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh pemanggilan fungsi
n = 1000  # Menampilkan 10 angka pertama dalam deret Fibonacci
for i in range(n):
    print(fibonacci(i), end="|")