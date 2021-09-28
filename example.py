def capital(s):
    return sum(1 for x in s if x.isupper())


def transform(s, style):
    if style == "upper":
        return s.upper()
    elif style == "lower":
        return s.lower()
    else:
        return s


def isprime(n):
    if n%2==0:
        return False
    else:
        return True
