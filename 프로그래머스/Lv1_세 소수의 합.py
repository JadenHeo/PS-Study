def get_prime_numbers(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    for number in range(2, n+1):
        if not is_prime[number]:
            continue
        for multiple in range(number ** 2, n+1, number):
            is_prime[multiple] = False
    return [number for number in range(n+1) if is_prime[number]]
    
def solution(n):
    answer = 0
    prime_numbers = get_prime_numbers(n)
    if len(prime_numbers) < 3:
        return 0
    if n % 2 == 0:
        for i in range(1, len(prime_numbers)-1):
            for j in range(i+1, len(prime_numbers)):
                if prime_numbers[i] + prime_numbers[j] == n - 2:
                    # print(primeNumbers[i], primeNumbers[j])
                    answer += 1
        return answer
    for i in range(len(prime_numbers)-2):
        for j in range(i+1, len(prime_numbers)-1):
            for k in range(j+1, len(prime_numbers)):
                if prime_numbers[i] + prime_numbers[j] + prime_numbers[k] == n:
                    # print(primeNumbers[i], primeNumbers[j], primeNumbers[k])
                    answer += 1
    return answer