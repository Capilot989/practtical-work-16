def count_courses(all_courses: list) -> int:
    """
       Count the number of unique courses from a list of courses.

       The function takes a list of course names
       and returns the count of distinct courses.

       Args:
           all_courses (list): A list of strings, each representing a course name.

       Returns:
           int: The number of unique courses.
       """
    unique_courses = set(all_courses)
    return len(unique_courses)


if __name__ == '__main__':
    n = int(input('Enter the number of students: '))
    all_courses = []
    for number in range(1, n + 1):
        all_courses += list(input(
            f'Enter the courses of {number} student: '
        ).split())
    
    result = count_courses(all_courses)
    print(result)
