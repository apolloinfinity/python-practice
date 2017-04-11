a = input("type a number:")
b = input("type another number:")
a = int(a)
b = int(b)
try:
    print(a/b)
except (ZeroDivisionError,
       ValueError):
        print("Invalid input")
print(a/b)
