def sum_of_even_numbers(numbers: list) -> int:
    """
    This function takes a list of integers and returns the sum of the even numbers in the list.

    :param numbers: List of integers
    :return: Sum of even integers in the list
    """
    return sum(number for number in numbers if number % 2 == 0)


if __name__ == '__main__':
    print(sum_of_even_numbers([1, 2, 3, 4, 5]))
    print(sum_of_even_numbers([2, 4, 6, 8, 10]))
    print(sum_of_even_numbers([1, 3, 5, 7, 9]))
    print(sum_of_even_numbers([-2, -3, -4, -5, -6]))
    print(sum_of_even_numbers([]))
    print(sum_of_even_numbers([0, 1, 2, 3, 4, 5]))
    print(sum_of_even_numbers([1000000, 2000000, 3000000]))