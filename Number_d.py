def dlt(n):
    l = []
    for i in range(2, n):
        if n % i == 0:
            l.append(i)
    return l


def proper_fractions(n):
    m = 0
    q = dlt(n)
    for i in range(n):
        if not q:
            m = 1
        else:
            for el in q:
                if i % el == 0:
                    m += 1
                    break
    return n - m


if __name__ == '__main__':
    n = int(input())
    print(proper_fractions(n))  # Execution Timed Out (12000 ms)
