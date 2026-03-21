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

