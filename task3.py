import timeit
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    last = {pattern[i]: i for i in range(m)}

    i = m - 1  
    j = m - 1 

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  
            i -= 1
            j -= 1
        else:
            i += m - min(j, 1 + last.get(text[i], -1))
            j = m - 1

    return -1


def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    lps = [0] * m
    j = 0 

 
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    i, j = 0, 0  

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j 
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1
