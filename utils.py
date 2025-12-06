"""
Модуль с функциями для математических операций.
"""

def add(a, b):
    """Сложение: a + b"""
    return a + b

def subtract(a, b):
    """Вычитание: a - b"""
    return a - b

def multiply(a, b):
    """Умножение: a * b"""
    return a * b

def divide(a, b):
    """Деление: a / b"""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}