# Observations:

- a = b\*k -> gcd(a, b) = b
- a = b\*t + r -> gcd(a, b) = gcd(bt + r, b) = gcd(r, b)

# Extended Euclidean Algorithm

- compute gcd(a, b)
- find integers x, y such that a.x + b.y = gcd(a, b)

# Solution

- we have gcd(a, b) = gcd(b, a') where a' = a - a // b
- assume we know x' and y' such that b.x' + a'.y' = gcd(b, a)
- substitute a' into the equation

```
b.x' + (a - a // b).y' = gcd(b, a)
a.y' + b.(x' - a // b).y' = gcd(b, a)
```

-> x and y can be computed recursively

- basis case: a.1 + 0.0 = gcd(a, 0)

# Implementation

`gcd_extended.py`
