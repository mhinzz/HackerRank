from itertools import groupby
if True:
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
