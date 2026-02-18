from itertools import combinations


def find_subsets(set_of_numbers: set[int]) -> list[set[int]]:
    """
    Generate all possible subsets of the given set.

    The function creates every possible subset of the input set, including
    the empty set and the set itself. For a set of size n, this returns
    2^n subsets.

    Args:
        set_of_numbers (set[int]): A set of integers for which to generate all subsets.

    Returns:
        list[set[int]]: A list containing all subsets as sets. The list includes
        the empty set, all proper subsets, and the original set itself.
    """
    result = []
    for r in range(0, len(set_of_numbers)):
        for combo in combinations(set_of_numbers, r):
            result.append(set(combo))
    result.append(set_of_numbers)
    return result


if __name__ == '__main__':
    set_of_numbers = set(
        map(int, input('Enter the numbers of set: ').split())
    )
    print(find_subsets(set_of_numbers))
