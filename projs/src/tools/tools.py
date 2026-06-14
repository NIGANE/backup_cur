
def in_string(sub: str, sen: str) -> bool:
    if sub is None or sen is None:
        return False
    i = 0
    j = 0
    sub = sub.lower()
    sen = sen.lower()
    while i < len(sen):
        if sub[j] == sen[i]:
            while j < len(sub) and i + j < len(sen):
                if sub[j] != sen[i + j]:
                    break
                j += 1
            if (j == len(sub)):
                return True
            j = 0
        i += 1
    return False
