def count_preferences(siroezhkin_likes: set, friends_like: set) -> int:
    """
     Count the number of preferences unique to Siroezhkin.

     The function calculates the size of the set difference between
     Siroezhkin's likes and the combined likes of his friends.
     This represents how many preferences Siroezhkin has that none
     of his friends share.

     Args:
         siroezhkin_likes (set): A set of strings representing Siroezhkin's preferences.
         friends_like (set): A set of strings representing the union of friends' preferences.

     Returns:
         int: The number of preferences that are only in Siroezhkin's set.
     """
    return len(siroezhkin_likes - friends_like)


if __name__ == '__main__':
    siroezhkin_likes = set(
        list(input('Enter the preferences of Siroezhkin: ').split())
    )
    n = int(input('Enter the number of friends: '))
    all_preferences = []
    for number in range(1, n + 1):
        all_preferences += list(input(
            f'Enter the preferences of {number} friend: '
        ).split())
    friends_like = set(all_preferences)
    
    result = count_preferences(siroezhkin_likes, friends_like)
    print(result)
