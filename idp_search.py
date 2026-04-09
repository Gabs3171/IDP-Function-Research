def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_distance_to_prime(n):
    if is_prime(n): return 0
    offset = 1
    while True:
        if is_prime(n + offset) or (n - offset >= 0 and is_prime(n - offset)):
            return offset
        offset += 1

def fast_search_for_counterexample(limit):
    last_prime = 2
    # We are looking for a gap >= 54 to potentially find d2(n) = 4
    print(f"Scanning prime gaps up to {limit}...")
    
    for p in range(3, limit, 2):
        if is_prime(p):
            gap = p - last_prime
            if gap >= 8: # Only check gaps large enough to potentially yield d2(n) >= 3
                # Test the midpoint(s) of the gap
                # If gap is 54, the midpoint m = last_prime + 27
                # We check all integers in the "middle" of the gap
                for m in range(last_prime + 1, p):
                    d1 = get_distance_to_prime(m)
                    d2 = get_distance_to_prime(d1)
                    
                    if d2 >= 4:
                        print(f"\nSUCCESS! Counter-example found.")
                        print(f"Integer n: {m}")
                        print(f"Distance to prime d(n): {d1}")
                        print(f"Distance to prime d(d(n)): {d2}")
                        return m
            last_prime = p
    print("\nNo counter-example found. The conjecture holds for this range.")
    return None

# This will run much faster because it skips the 'boring' numbers near primes
fast_search_for_counterexample(1000000)
