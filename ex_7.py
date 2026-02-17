import itertools


def find_permutations(set_of_numbers: set[int]) -> list[tuple[int]]:
    """
       Generate all permutations of the elements in the given set.

       The function takes a set of integers, sorts them, and returns a list
       of all possible permutations as tuples of integers.

       Args:
           set_of_numbers (set): A set of integers representing numbers.

       Returns:
           list[tuple[int]]: A list of tuples, where each tuple is a permutation
           of the sorted elements from the input set.
       """
    result = list(itertools.permutations(
        sorted(set_of_numbers))
    )
    return result


if __name__ == '__main__':
    set_of__numbers = set(
        map(int, input('Enter the numbers separated by spaces: ').split())
    )
    print(find_permutations(set_of__numbers))
