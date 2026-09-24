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

def by_powers(x: int) -> list[int]:
    """
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
    print("Вывод:  ", *by_powers(x))


if __name__ == "__main__":
    main()
