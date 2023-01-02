def concatenatio(*params):
    res: int = 0
    for item in params:
        res += item
    return res

print(concatenatio(1, 2, 3, 4))