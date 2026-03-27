# 1 Tính

```python
a = input("Nhập a: ")
b = input("Nhập b: ")
```

## a. (a + b)

```python
print("a + b = ", a + b)
```

## b. a/b

```python
print("a/b = ", a/b)
```

## c. a^b

```ptython
print("a^b = ", a ** b)
```

# 2 Diện tích hình chữ nhật

```python
a = input("Nhập chiều dài : ")
b = input("Nhập chiều rộng : ")

s = a *b

print("Diện tích hình chữ nhật: S = ", s)
```

# 3 Xuất tất cả các số nguyên tố trong 1 khoảng cho trước

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input("Nhập số bắt đầu: "))
b = int(input("Nhập số kết thúc: "))

print("Các số nguyên tố trong khoảng là:")
for i in range(a, b + 1):
    if is_prime(i):
        print(i, end=" ")
```

# 4 fibonacci 5n^2 +4 Or 5n^2 -4 = số chihs phương

```python
import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

n = int(input("Nhập n: "))

if is_fibonacci(n):
    print("Là số Fibonacci")
else:
    print("Không phải số Fibonacci")
```

# 5 Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)

## Dùng đệ quy

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

n = int(input("Nhập n: "))
print("Fibonacci thứ", n, "=", fib_recursive(n))
```

## Không dùng dệ quy

```python
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("Nhập n: "))
print("Fibonacci thứ", n, "=", fib_iterative(n))
```


# 6 Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)

## Đệ quy

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def sum_fib_recursive(n):
    if n == 0:
        return 0
    return sum_fib_recursive(n-1) + fib(n-1)

n = int(input("Nhập n: "))
print("Tổng =", sum_fib_recursive(n))
```

## Không đệ quy

```python
def sum_fib_iterative(n):
    a, b = 0, 1
    total = 0
    
    for _ in range(n):
        total += a
        a, b = b, a + b
        
    return total

n = int(input("Nhập n: "))
print("Tổng =", sum_fib_iterative(n))
```

# 7 Tính tổng căn bậc 2 của n số nguyên đầu tiên

```python
import math

n = int(input("Nhập n: "))

S = 0
for i in range(1, n + 1):
    S += math.sqrt(i)

print("Tổng =", S)
```

# 8 Giải phương trình bậc 2: ax2 + bx + c=0

```python
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình bậc nhất, nghiệm:", -c / b)
else:
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm phân biệt:", x1, x2)
        
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép:", x)
        
    else:
        print("Phương trình vô nghiệm (trong R)")
```

# 9 Tính n!

```python
n = int(input("Nhập n: "))

result = 1
for i in range(1, n + 1):
    result *= i

print("n! =", result)
```

# 10 In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)

```pyhton
n = int(input("Nhập n: "))

for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

# 11 Đổi giờ - phút – giây

```pyhton
soGiay = int(input("Nhập số giây: "))

gio = soGiay // 3600
du = soGiay % 3600
phut = du // 60
giay = du % 60

print(f"{gio}:{phut}:{giay}")
```

# 12 arr = [...]

## a.

```pyhton
print([x for x in arr if x % 2 != 0 and x % 5 != 0])
```

## b.

```python
def is_fibo(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

print([x for x in arr if is_fibo(x)])
```

## c.

```pyhton
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in arr if is_prime(x)]
print(max(primes) if primes else "Không có")
```

## d.

```pyhton
fibo_nums = [x for x in arr if is_fibo(x)]
print(min(fibo_nums) if fibo_nums else "Không có")
```

## e.

```python
odd = [x for x in arr if x % 2 != 0]
print(sum(odd)/len(odd) if odd else 0)
```

## f.

```python
result = 1
found = False

for x in arr:
    if x % 2 != 0 and x % 3 != 0:
        result *= x
        found = True

print(result if found else 0)
```

## g.

```python
i, j = 1, 3  # vị trí muốn đổi
arr[i], arr[j] = arr[j], arr[i]
print(arr)
```


## h.

```python
print(arr[::-1])
```

## i.

```python
unique = list(set(arr))
unique.sort(reverse=True)
print(unique[1] if len(unique) > 1 else "Không có")
```

## j.

```python
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

print(sum(sum_digits(x) for x in arr))
```


## k.

```python
x = 5
print(arr.count(x))
```

## l.

```python
n = 2
result = [x for x in set(arr) if arr.count(x) == n]
print(result)
```

## m.

```python
from collections import Counter

count = Counter(arr)
max_freq = max(count.values())

result = [x for x in count if count[x] == max_freq]
print(result)
```
