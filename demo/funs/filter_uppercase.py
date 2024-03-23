names = ['Java', 'Python','sql', 'C', 'JavaScript', 'c#']


def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


for n in filter(has_upper, names):
    print(n)

