# 7. Fibonacci Series

n = int(input("How many terms you want to in fibonacci series : "))
a, b = 0, 1

for i in range(n):
    print(a, end = " ")
    a, b = b, a+b