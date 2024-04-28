n = int(input("enter the positive no to calculate the sum till it :"))


def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)
