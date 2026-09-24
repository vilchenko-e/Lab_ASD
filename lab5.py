def insertion_sort(arr: list[float]) -> list[float]:
    """
    Сортировка вставками.
    Для каждого i от 1 до n-1 вставляем arr[i] в уже
    отсортированный arr[0..i-1], сдвигая большие элементы вправо.

    Время: лучший O(n) (почти отсортированный массив),
           средний и худший O(n²).
    Память: O(1).
    Устойчивая: порядок равных элементов сохраняется.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    print("=== Лаба №5: сортировка вставками ===")
    raw = input("Введите числа через пробел: ")
    try:
        data = list(map(float, raw.split()))
    except ValueError:
        print("Нужны числа")
        return
    print("Отсортировано:", insertion_sort(data))


if __name__ == "__main__":
    main()
