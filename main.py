def parse_expression(expression):
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Неправильный формат. Используйте: число оператор число")
    
    try:
        a = float(parts[0])
        b = float(parts[2])
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    
    op = parts[1]
    return a, op, b

from utils import OPERATIONS
user_input = input()
a, op, b = parse_expression(user_input)
if op in OPERATIONS:
    result = OPERATIONS[op](a, b)
    print(f"Результат: {result}")
else:
    print(f"Ошибка: Неподдерживаемая операция: {op}")
