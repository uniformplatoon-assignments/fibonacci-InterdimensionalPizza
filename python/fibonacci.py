def fibonacci(n):
  a = 0
  b = 1
  c = 0
  for _ in range(0, n-1, 1):
    c = a + b
    a = b
    b = c
  return c



print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(8))
print(fibonacci(11))
print(fibonacci(14))
print(fibonacci(17))
print(fibonacci(20))