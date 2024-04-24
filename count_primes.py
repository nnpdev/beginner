import time 
def count_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    count = 0
    for i in range(2, n + 1):
        if primes[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return count

start_time = time.time()
result = count_primes(10**9)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Số số nguyên tố là: {result}")
print(f"Thời gian là: {elapsed_time} s")



