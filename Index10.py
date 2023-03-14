def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit() and len(s)==5:
        return int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])

print(main("12345"))