# 1. Formatted Twinkle Poem

```python
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")
```

# 2 Python Version Checker

```python
import sys

print("Python version:")
print(sys.version)
```

# 3. Current DateTime Display

```python
import datetime

now = datetime.datetime.now()

print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

# 4. Circle Area Calculator

```python
import math

r = float(input("Nhập bán kính r = "))

area = math.pi * r * r

print("Area =", area)
```

# 5. Reverse Full Name

```python
first_name = input("Nhập tên: ")
last_name = input("Nhập họ: ")

print(last_name + " " + first_name)
```

# 6. List and Tuple Generator

```python
values = input("nhập dãy số (cách nhau bằng dấu cách): ")

lst = values.split(" ")

tup = tuple(lst)

print("List: ", lst)
print("Tuple: ", tup)
```

# 7. File Extension Extractor

```python
filename = input("Nhập tên file: ")

extension = filename.split(".")[-1]

print("Extension: ", extension)
```

# 8. First and Last Colors

```pyhton
color_list = ["Red", "Green", "white", "Black"]

print("First color: ", color_list[0])
print("Last color: ", color_list[-1])
```

# 9. Exam Schedule Formatter

```python
exam_st_date = (11, 12, 2014)

print("The examination will start from : %i / %i / %i" % exam_st_date)
```

# 10. Number Expansion Calculator

```python
n = input("n = ")
print(int(n) + int(n*2) + int(n*3))
```

# 11. Function Documentation Printer

```python
help(abs)
```

# 12. Monthly Calendar Display

```python
import calendar

year = int(input("Nhập năm: "))
month = int(input("Nhập tháng (1-12): "))

print("\n", calendar.month(year, month))
```

# 13. Multi-line Here Document

```python
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")
```

# 14. Days Between Dates

```python
from datetime import date

d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)

delta = d2 - d1

print(delta.days, "days")
```

# 15. Sphere Volume Calculator

```python
import math

r = 6

volume = (4/3) * math.pi * r**3

print("Volume =", volume)
```

# 16. Difference from 17

```python
n = int(input("Nhập số: "))

if n <= 17:
    result = 17 - n
else:
    result = 2 * (n - 17)

print("Kết quả =", result)
```

# 17. Number Range Tester

```python
n = int(input("Nhập số: "))

if abs(n - 1000) <= 100 or abs(n - 2000) <= 100:
    print("True")
else:
    print("False")
```

# 18. Triple Sum Calculator

```python
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

sum_ = a + b + c

if a == b == c:
    result = sum_ * 3
else:
    result = sum_

print("Kết quả =", result)
```

# 19. Prefix "Is" String Modifier

```python
s = input("Nhập chuỗi: ")

if s.startswith("Is"):
    result = s
else:
    result = "Is " + s

print("Kết quả:", result)
```

# 20. String Copy Generator

```python
s = input("Nhập chuỗi: ")
n = int(input("Nhập số lần lặp: "))

result = s * n

print("Kết quả:", result)
```

# 21. Even or Odd Checker

```python
n = int(input("Nhập số: "))

if n % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
```

# 22. Count 4 in List

```python
lst = list(map(int, input("Nhập danh sách số (cách nhau bằng dấu cách): ").split()))

count = lst.count(4)

print("Số lần xuất hiện của 4:", count)
```

# 23. String Prefix Copies

```python
s = input("Nhập chuỗi: ")
n = int(input("Nhập số lần lặp: "))

if len(s) < 2:
    result = s * n
else:
    result = s[:2] * n

print("Kết quả:", result)
```

# 24. Vowel Tester

```python
ch = input("Nhập một chữ cái: ").lower()

if ch in "aeiou":
    print("Là nguyên âm")
else:
    print("Không phải nguyên âm")
```

# 25. Value in Group Tester

```python
lst = list(map(int, input("Nhập danh sách: ").split()))
value = int(input("Nhập giá trị cần kiểm tra: "))

if value in lst:
    print("True")
else:
    print("False")
```
