def is_357_smooth(k: int) -> bool:
    """
    True, если k = 3^K * 5^L * 7^M.
    Делим на 3, 5, 7, пока делится; если осталось 1 — да.
    Время: O(log k).
    """
    for p in (3, 5, 7):
        while k % p == 0:
            k //= p
    return k == 1


def by_divisibility(x: int) -> list[int]:
    """
    Вариант 1 — через признаки делимости.
    Перебираем все k от 1 до x.
    Время: O(x · log x). Память: O(1) (без вывода).
    """
    return [k for k in range(1, x + 1) if is_357_smooth(k)]


def by_powers(x: int) -> list[int]:
    """
    Вариант 2 — через перебор степеней.
    Тройной цикл по K, L, M, с ранним выходом за x.
    Количество чисел ~O(log³ x), столько же времени.
    Память: O(log³ x).
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
    print("=== Лаба №3: числа вида 3^K * 5^L * 7^M ===")
    try:
        x = int(input("Введите число x: "))
    except ValueError:
        print("Нужно целое число")
        return
    if x < 1:
        print("Число должно быть >= 1")
        return

    print("Через признаки делимости:", *by_divisibility(x))
    print("Через перебор степеней:  ", *by_powers(x))


if __name__ == "__main__":
    main()
