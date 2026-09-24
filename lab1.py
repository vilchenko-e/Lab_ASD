from stack import Stack


def check_one_type(s: str) -> bool:
    """
    Проверка строки со скобками одного типа.
    Тип определяется по первой встреченной открывающей скобке.

    Алгоритм: стек. Открывающая — push, закрывающая — pop при совпадении.
    """
    pairs = {'(': ')', '{': '}', '[': ']'}
    opener = closer = None
    for ch in s:
        if ch in pairs:
            opener, closer = ch, pairs[ch]
            break

    if opener is None:               # скобок нет — выражение корректно
        return True

    stack = Stack()
    for ch in s:
        if ch == opener:
            stack.push(ch)
        elif ch == closer:
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


def check_all_types(s: str) -> bool:
    """
    Проверка строки со скобками (), {}, [] одновременно.
    Стек: открывающая — push, закрывающая — сверяем с вершиной.

    Время: O(n). Память: O(n).
    """
    matching = {')': '(', '}': '{', ']': '['}
    openers = set('({[')
    stack = Stack()

    for ch in s:
        if ch in openers:
            stack.push(ch)
        elif ch in matching:
            if stack.is_empty() or stack.peek() != matching[ch]:
                return False
            stack.pop()
    return stack.is_empty()


def _ask_string() -> str | None:
    s = input("Введите строку: ")
    if not s:
        print("Строка не существует")
        return None
    return s


def main():
    while True:
        print("\nЛаба №1: задача о скобках")
        print("1 — пункт 1 (один тип скобок)")
        print("2 — пункт 2 (все три вида)")
        print("0 — выход")
        choice = input("Выбор: ").strip()

        if choice == "0":
            break

        if choice == "1":
            s = _ask_string()
            if s is None:
                continue
            print("Строка существует" if check_one_type(s)
                  else "Строка не существует")

        elif choice == "2":
            s = _ask_string()
            if s is None:
                continue
            print("Строка существует" if check_all_types(s)
                  else "Строка не существует")
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
