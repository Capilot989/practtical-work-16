def find_number_in_intersection(
        set1: set, set2: set, numb: str
) -> bool:
    """
        Check if a given number is present in the intersection of two sets.

        The function computes the intersection of two sets and determines
        whether the specified number belongs to that intersection.

        Args:
            set1 (set): The first set of elements (strings).
            set2 (set): The second set of elements (strings).
            numb (str): The number (as a string) to search for.

        Returns:
            bool: True if the number is in the intersection, False otherwise.
        """
    return numb in (set1 & set2)


if __name__ == '__main__':
   set1 = set(
       input('Enter elements of the first subsequense: ').split()
   )
   set2 = set(
       input('Enter elements of the second subsequense: ').split()
   )
   number = input('Enter the desired number: ')
   result = find_number_in_intersection(set1, set2, number)
   print(result)
