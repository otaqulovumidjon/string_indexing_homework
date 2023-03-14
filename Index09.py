def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)==1:
        if s.isdigit():
            return int(s)
        else:
            return -1

print(main("a"))