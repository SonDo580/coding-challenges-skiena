# Addition

(x + y) mod n = ((x mod n) + (y mod n)) mod n

# Subtraction

(x - y) mod n = ((x mod n) - (y mod n)) mod n

# Multiplication

xy mod n = (x mod n)(y mod n) mod n

# Exponentiation

x^y mod n = (x mod n)^y mod n

# Finding last digit

Example:

- what is the last digit of 2^100
- rephrase: what is 2^100 mod 10

Solution: repeated squaring, take the remainder mod 10 at each step

```
2^3 mod 10 = 8
2^6 mod 10 = (2^3 mod 10)(2^3 mod 10) mod 10 = 8.8 mod 10 = 4
2^12 mod 10 = (2^6 mod 10)(2^6 mod 10) mod 10 = 4.4 mod 10 = 6
2^24 mod 10 = (2^12 mod 10)(2^12 mod 10) mod 10 = 6.6 mod 10 = 6
2^48 mod 10 = (2^24 mod 10)(2^24 mod 10) mod 10 = 6.6 mod 10 = 6
2^96 mod 10 = (2^48 mod 10)(2^48 mod 10) mod 10 = 6.6 mod 10 = 6
2^100 mod 10 = 2^96.2^3.2^1 mod 10 = 6.8.2 mod 10 = 6
```

# RSA Encryption Algorithm

# Calendrical Calculations

Example:

- your birthday this year falls on a Wednesday
- what day of the week it will fall on next year

Solution:

- number of day between now and then: 365 or 366 (check leap year)
- take the remainder of number of days divided by 7 days per week
- 365 % 7 = 1, 366 % 7 = 2 -> Thursday or Friday

# Proof

x = n.q1 + r1
y = n.q2 + r2

1. Addition

```
x + y = n(q1 + q2) + (r1 + r2)
=> (x + y) mod n = (r1 + r2) mod n = ((x mod n) + (y mod n)) mod n
```

2. Subtraction

```
x - y = n(q1 - q2) + (r1 - r2)
=> (x - y) mod n = (r1 - r2) mod n = ((x mod n) - (y mod n)) mod n
```

3. Multiplication

```
x.y = (n.q1 + r1)(n.q2 + r2) = n.(q1.q2 + q1.r2 + q2.r1) + r1.r2
=> x.y mod n = r1.r2 mod n = (x mod n)(y mod n) mod n
```

4. Exponentiation

```
x^a = (n.q1 + r1)^a
= r1^a + <terms divisible by n>
=> x^a mod n = r1^a mod n = (x mod n)^a mod n
```
