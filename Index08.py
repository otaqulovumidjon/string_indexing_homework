def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)<=5:
        if len(s)>=1 and s[0]=="*":
            return 0

        elif len(s)>=2 and s[1]=="*":
            return 1

        elif len(s)>=3 and s[2]=="*":
            return 2

        elif len(s)>=4 and s[3]=="*":
            return 3

        elif len(s)==5 and s[4]=="*":
            return 4
        else:
            return False

print(main("kej*d"))