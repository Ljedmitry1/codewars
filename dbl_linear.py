def d_l(n):
    l = [1]
    for i in range(n):
        l.append(2 * l[i] + 1)
        l.append(3 * l[i] + 1)
        l.sort()

        if len(l) == n:
            break
    print(l)
    return l[0: n + n//10]


def dbl_linear(n):
    l = sorted(set(d_l(n)))
    print(l)
    return l[n]


if __name__ == '__main__':
    n = int(input())
    print(dbl_linear(n))
