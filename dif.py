import math

# Функция для нахождения наибольшего общего делителя (НОД)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для нахождения обратного элемента по модулю
def mod_inverse(a, m):
    g, x, y = extended_euclid(a, m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    return x % m

# Расширенный алгоритм Евклида для нахождения обратного элемента
def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Функция для решения диофантова уравнения ax + by = c
def solve_diophantine(a, b, c):
    g = gcd(a, b)
    if c % g != 0:
        return None  # Нет решений
    a, b, c = a // g, b // g, c // g
    _, x0, y0 = extended_euclid(a, b)
    x0 *= c
    y0 *= c
    return x0, y0  # Одно из решений

# Функция шифрования
def encrypt(message, a, b, m):
    encrypted_message = []
    for char in message:
        # Преобразуем символ в число (код ASCII)
        c = ord(char)
        # Решаем диофантово уравнение для каждого символа
        x, y = solve_diophantine(a, b, c)
        if x is None:
            raise Exception(f'Не удалось зашифровать символ: {char}')
        # Применяем модуль для получения зашифрованного символа
        encrypted_message.append((x % m))
    return encrypted_message

# Функция расшифровки
def decrypt(encrypted_message, a, b, m):
    decrypted_message = []
    for enc in encrypted_message:
        # Решаем диофантово уравнение для каждого зашифрованного числа
        x, y = solve_diophantine(a, b, enc)
        if x is None:
            raise Exception(f'Не удалось расшифровать символ: {enc}')
        # Преобразуем обратно в символ
        decrypted_message.append(chr(x % m))
    return ''.join(decrypted_message)