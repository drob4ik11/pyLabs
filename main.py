def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def is_even(n):
    return n % 2 == 0

def product_of_even_numbers(n):
    product = 1
    for i in range(2, n + 1, 2):
        product *= i
    return product

def print_multiplication_table(n):
    print(f"Таблиця множення для {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main():
    n = get_integer_input("Введіть число: ")

    if is_even(n):
        print(f"Число {n} є парним.")
    else:
        print(f"Число {n} є непарним.")

    product = product_of_even_numbers(n)
    print(f"Добуток всіх парних чисел від 1 до {n}: {product}")

    print_multiplication_table(n)

if __name__ == "__main__":
    main()
