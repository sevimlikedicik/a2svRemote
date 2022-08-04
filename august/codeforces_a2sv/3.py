from sys import stdin

input = stdin.readline


def fibo(n):
    fib = [1, 2]
    for i in range(2, n):
        fib.append((fib[i - 2] + fib[i - 1]) % 1000000007)
    return fib[n - 1]


def solution():
    s = input()
    total = 1
    count = 1
    if s and s[0] in {"m", "w"}:
        print(0)
        return
    for i in range(1, len(s)):
        if s[i] in {"m", "w"}:
            print(0)
            return
        if s[i] == s[i-1] and s[i] in {"u", "n"}:
            count += 1
        else:
            total = (total * fibo(count)) % 1000000007
            count = 1

    total = (total * fibo(count)) % 1000000007
    print(total)
    return


solution()
