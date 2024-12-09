def add_everything_up(a, b):
    try:
        # Пытаемся сложить a и b стандартным способом
        result = a + b
        # Если результат - float, округляем до 3 знаков после запятой
        if isinstance(result, float):
            return round(result, 3)
        return result
    except TypeError:
        # Если возникает ошибка, проверяем типы
        if isinstance(a, (int, float)) and isinstance(b, str):
            return f"{a}{b}"
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return f"{a}{b}"
        else:
            raise  # Если это не предусмотренные типы, выбрасываем исключение дальше

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456