def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a = 0
    if len(s)==5:
        if s[0].isdigit():
            a+=1
        if s[1].isdigit():
            a+=1
        if s[2].isdigit():
            a+=1
        if s[3].isdigit():
            a+=1
        if s[4].isdigit():
            a+=1
    return a

print(main("32x3z"))