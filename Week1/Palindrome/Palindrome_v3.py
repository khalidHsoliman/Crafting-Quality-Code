def is_palindrome_v3(s):
    """ (str) -> bool

    return true if and only if s is a palindrome
    """
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i+=1
        j-=1

    return j <= i
