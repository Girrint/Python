# 1

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

# 2

```python
a = input("Nhập chiều dài : ")
b = input("Nhập chiều rộng : ")

s = a *b

print("Diện tích hình chữ nhật: S = ", s)
```

# 3

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

# 5

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


# 6

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

# 7

```python
import math

n = int(input("Nhập n: "))

S = 0
for i in range(1, n + 1):
    S += math.sqrt(i)

print("Tổng =", S)
```

# 8

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

# 9

```python
n = int(input("Nhập n: "))

result = 1
for i in range(1, n + 1):
    result *= i

print("n! =", result)
```

