from itertools import combinations


def find_subsets(set_of_numbers: set[int], k: int) ->list[set[int]]:
    """
        Generate all subsets of a specific size from the given set.

        The function creates every possible subset of the input set that has
        exactly k elements. For a set of size n, this returns C(n, k) subsets
        (combinations).

        Args:
            set_of_numbers (set[int]): A set of integers from which to generate subsets.
            k (int): The desired size of each subset. Must be between 0 and the size of the set.

        Returns:
            list[set[int]] | None: A list containing all subsets of size k as sets.
            Returns None if k is greater than the size of the set.
        """

    result = []
    if k > len(set_of_numbers):
        return None

    for combo in combinations(set_of_numbers, k):
        result.append(set(combo))
    return result


if __name__ == '__main__':
    set_of_numbers = set(
        map(int, input('Enter the numbers of set: ').split())
    )
    k = int(input('Enter the capacity of subset: '))
    print(find_subsets(set_of_numbers, k))
