def taylor(x: float, eps: float = 10e-5) -> float:
    if abs(x) >= 1:
        raise ValueError("Series diverges for |x| ≥ 1")
    res = 1
    term = 1
    n = 2

    while abs(term) > eps:
        term = -n / (n-1) * term * x
        res += term
        n += 1

    return res


if __name__ == "__main__":
    print(taylor(0.5)- 1/(1+0.5)**2)


