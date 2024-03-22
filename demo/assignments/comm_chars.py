
def common(*values):
    chars = set(values[0])
    for v in values[1:]:
        chars &= set(v)

    print(chars)


common("java", "javascript", "ada")
common("java", "python")

