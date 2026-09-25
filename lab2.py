from stack import Stack
from lab1 import check_all_types


def apply_op(a: float, b=None, op=None) -> float:
    if b is None:
        if op == '+':
            return a
        elif op == '-':
            return -a
        raise ValueError("Недопустимая операция")
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return a / b
    raise ValueError(f"Неизвестная операция: {op}")


def priority(op: str) -> int:
    """+,- = 1; *,/ = 2; скобка = 0."""
    if op in '+-': return 1
    if op in '*/': return 2
    return 0


def calc_expression(expr: str) -> float:
    """
    Алгоритм Дейкстры с двумя стеками.
    values — числа, ops — операции и '('.

    Перед push новой операции выталкиваем из ops все операции
    с приоритетом >= текущей. Закрывающая скобка выталкивает
    до ближайшей '('.

    Время: O(n). Память: O(n).
    """
    values = Stack()
    ops = Stack()
    i, n = 0, len(expr)

    while i < n:
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        # --- число ---
        if ch.isdigit() or ch == '.' or (ch in "+-" and (i==0 or expr[i-1] in "([{+-*/")):
            j = i
            if ch in "+-":
                j+=1
            while j < n and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            try:
                values.push(float(expr[i:j]))
            except ValueError:
                raise ValueError(f"Некорректное число: {expr[i:j]}")
            i = j
            continue

        # --- открывающая скобка ---
        if ch == '(':
            ops.push(ch)
            i += 1
            continue

        # --- закрывающая скобка ---
        if ch == ')':
            while not ops.is_empty() and ops.peek() != '(':
                b = values.pop(); a = values.pop()
                values.push(apply_op(a, b, ops.pop()))
            if ops.is_empty():
                raise ValueError("Лишняя закрывающая скобка")
            ops.pop()                     # выбрасываем '('
            i += 1
            continue

        # --- операция ---
        if ch in '+-*/':
            if ch in "+-" and (i==0 or expr[i-1] in "([{+-*/"):
                if i+1 < n and (expr[i+1].isdigit() or expr[i+1] == "."):
                    i+=1
                    continue
                else:
                    raise ValueError()
            while (not ops.is_empty() and ops.peek() != '('
                   and priority(ops.peek()) >= priority(ch)):
                b = values.pop(); a = values.pop()
                values.push(apply_op(a, b, ops.pop()))
            ops.push(ch)
            i += 1
            continue

        raise ValueError(f"Недопустимый символ: {ch}")

    # доcчитываем оставшиеся операции
    while not ops.is_empty():
        op = ops.pop()
        if op == '(':
            raise ValueError("Не закрыта скобка")
        b = values.pop(); a = values.pop()
        values.push(apply_op(a, b, op))

    if len(values) != 1:
        raise ValueError("Некорректное выражение")
    return values.pop()


def main():
    print("Лаба 2: арифметическое выражение")
    expr = input("Введите выражение (оканчивается '='): ").strip()

    if not expr.endswith('='):
        print("Выражение должно оканчиваться '='")
        return
    expr = expr[:-1]

    # проверка скобок (из лабы 1)
    if not check_all_types(expr):
        print("Скобки расставлены неверно")
        return

    try:
        print(f"Результат: {calc_expression(expr)}")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
