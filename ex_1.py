def find_number(sequense: set, numb: str) -> bool:
    """
       Check if a given number is present in the sequence.

       Args:
           sequence (set): A set of strings representing numbers.
           numb (str): The number to search for.

       Returns:
           bool: True if the number is in the sequence, False otherwise.
       """
    return numb in sequense


if __name__ == '__main__':
    sequense = set(
        input('Enter the numbs separated by spaces: ').split()
    )
    numb = input('Enter the desired bumber: ')
    print()
    print(find_number(sequense, numb))
