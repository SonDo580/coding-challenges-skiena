# Extended Euclidean Algorithm
# - compute gcd(a, b)
# - find integers x, y such that a.x + b.y = gcd(a, b)   

def gcd_extended(p, q):
    if q == 0:
        return p, 1, 0
    
    g, x1, y1 = gcd_extended(q, p % q)
    x = y1
    y = x1 - (p // q) * y1

    return g, x, y

# Usage:
p = 30
q = 12
gcd_value, x, y = gcd_extended(p, q)
print(f"p: {p}, q: {q}")
print(f"GCD: {gcd_value}, x: {x}, y: {y}")