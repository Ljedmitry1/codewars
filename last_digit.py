def last_digit(n1, n2):
    if (n1 and n2) < 100:
        n_s = n1 ** n2
    else:
        n_s = int(str(n1)[-2:]) ** int(str(n2)[-2:])
    return int(str(n_s)[-1]) if n1 % 10 != 0 else 0


def l_digit(n1, n2):
    return pow(n1, n2, 10)


if __name__ == '__main__':
    n1, n2 = map(int, input().split())
    print(last_digit(n1, n2))
    print(l_digit(n1, n2))
