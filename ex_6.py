def solve_equation() -> None:
    """
        Find and print all solutions to the equation HOD + HOD + HOD = MAT.

        HOD is a three-digit number (from 100 to 333) where H, O, D are its digits.
        MAT = 3 * HOD is also a three-digit number (from 300 to 999) with digits M, A, T.
        The function prints all cases where all six digits H, O, D, M, A, T are distinct.

        Returns:
            None
        """
    for hod in range(100, 334):
        mat = 3 * hod
        h, o, d = map(int, str(hod))
        m, a, t = map(int, str(mat))
        if len({h, o, d, m, a, t}) == 6:
            print(f'{hod}+{hod}+{hod}={mat}')


if __name__ == '__main__':
    solve_equation()
