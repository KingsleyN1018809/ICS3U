S = []

def fib(n):
    if n == 1:
        S.append(1)
        return S
    elif n == 2:
        fib(1)
        S.append(1)
        return S
    else:
        fib(n - 1)
        S.append(S[-1] + S[-2])
        return S

seq = fib(45)
print(seq)
