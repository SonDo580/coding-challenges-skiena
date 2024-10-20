# Observation

- lcm(x, y) >= max(x, y)
- lcm(x, y) <= x.y

# Formula

lcm(x, y) = x.y / gcd(x, y)

# Avoid overflow

lcm(x, y) = (x / gcd(x, y)).y

# Proof

- prime factorization:

```
x = p1^a1 . p2^a2 . ... . pk^ak
y = p1^b1 . p2^b2 . ... . pk^bk
```

- LCM:

for primes that are present in both x and y, take the maximum exponent.

for primes that are not common, take the exponent of that number.

```
lcm(x, y) = p1^max(a1, b1) . p2^max(a2, b2) . ... . pk^max(ak, bk)
```

- GCD:
  take the minimum exponent of each common prime

```
gcd(x, y) = p1^min(a1, b1) . p2^min(a2, b2) . ... . pk^min(ak, bk)
```

- combining:

```
gcd(x, y).lcm(x, y)
= p1^(min(a1, b1) + max(a1, b1)) . ...
= p1^(a1 + b1) . ...
= p1^a1 . p1^b1 . ...
= x.y
```
