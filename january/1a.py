inputs = [int(num) for num in input().split(' ')]
n = int(inputs[0])
m = int(inputs[1])
a = int(inputs[2])

k = n // a
if n % a != 0:
    n = (k + 1) * a

k = m // a
if m % a != 0:
    m = (k + 1) * a

squares = (n // a) * (m // a)
print(squares)
