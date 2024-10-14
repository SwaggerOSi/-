numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for f in numbers:
    if f == 1:
        continue

    is_prime = True
    for r in range(1, f // 2):
        if f % numbers[r] == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(f)
    else:
        not_primes.append(f)

print('Primes:', primes)
print('Not Primes:', not_primes)