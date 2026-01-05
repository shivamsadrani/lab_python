Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=("hello")
print(x)
hello
x=10
print(x)
10
x=True
y=False
peinr(x>y)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    peinr(x>y)
NameError: name 'peinr' is not defined. Did you mean: 'print'?
x=True
y=False
print(x<y)
False
x=("apple","banana","cherry.")
x=("apple","banana","cherry:")
print(x)
('apple', 'banana', 'cherry:')
x=["apple","banana","cherry"]
print(x)
['apple', 'banana', 'cherry']
x={"name":,"john","age":36}
SyntaxError: expression expected after dictionary key and ':'
x={"name":"john","age":36}
print(x)
{'name': 'john', 'age': 36}
x=20.5
print(x)
20.5
a=
SyntaxError: invalid syntax
print(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
