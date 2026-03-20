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


