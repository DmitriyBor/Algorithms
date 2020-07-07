    # # Подсчитать число фибаначи 1 <= n <= 40

# def fib(n):
#     if (n < 1) or (n > 40):
#         return 'Ошибка'
#     elif n in (1, 2):
#         return 1
#     else:
#         a = 1
#         b = 1
        # for i in range(2, n):
        #     a, b = b, a + b   # Не получилось реализовать массивом и поэтому решил сделать сложением 
        # return b
            
# def main():
#     n = int(input())
#     print(fib(n))


# if __name__ == "__main__":
#     main()


    # Дано число  1 <= n <= 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.

# def fib_digit(n):
#     if (n < 1):
#         return 'Ошибка'
#     elif n in (1, 2):
#         return 1
#     else:
#         a = 1
#         b = 1
#         for i in range(2, n):
#             a, b = b, (a + b) % 10    # Поставил остаток деления на 10, чтобы получить последнюю цифру
#         return b 


# def main():
#     n = int(input())
#     print(fib_digit(n))


# if __name__ == "__main__":
#     main()



  # Даны целые числа 1 <= n <= 10^18 и 1 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

def fib_mod(n, m):
    if (n < 1) or (m <= 1):
        return 'Ошибка'
    elif n in (1, 2):
        return 1
    else:
        a, b = 1, 1
        for i in range(2, n):
            a, b = b, (a + b) % m  # Заменил на остаток деления от m
        return b
        # s = b
        # c = 0 
        # while b > m:
        #     b = b - m
        #     c = c + m     
        # return (s - c)


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()













