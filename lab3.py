def by_powers(x: int) -> list[int]:
    """
    Тройной цикл по K, L, M.
    """
    result = []
    p3 = 1
    while p3 <= x:
        p5 = p3
        while p5 <= x:
            p7 = p5
            while p7 <= x:
                result.append(p7)
                p7 *= 7
            p5 *= 5
        p3 *= 3
    result.sort()
    return result


def main():
    print("Лаба 3: числа вида 3^K * 5^L * 7^M")
    try:
        x = int(input("Введите число x: "))
    except ValueError:
        print("Нужно целое число")
        return
    if x < 1:
        print("Число должно быть >= 1")
        return
    print("Вывод:  ", *by_powers(x))


if __name__ == "__main__":
    main()
