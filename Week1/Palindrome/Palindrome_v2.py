def is_palindrome_v2(s):

    n = len(s)
    return s[: n//2] == reverse(s[n - n//2:])


def reverse(s):
    rev = ''
    for ch in s:
        rev = ch + rev

    return rev
