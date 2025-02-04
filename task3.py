import timeit
import pandas as pd

# Алгоритм Бойера-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    shift = {c: m for c in set(text)}
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift.get(text[i + m - 1], m)
    
    return -1

# Алгоритм Кнута-Морріса-Пратта (KMP)
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

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            j = lps[j - 1] if j > 0 else 0
            i += 1
    
    return -1

# Алгоритм Рабина-Карпа
def rabin_karp_search(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    d = 256
    p_hash = 0
    t_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    
    return -1

# Чтение файлов
file1_path = "./article1.txt"
file2_path = "./article2.txt"

with open(file1_path, "r", encoding="Windows-1252") as f:
    text1 = f.read()

with open(file2_path, "r", encoding="utf-8") as f:
    text2 = f.read()

# Подстроки для поиска
existing_substring = "алгоритм"
fake_substring = "xyzabc"

def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=5)

# Сравнение времени выполнения
results = {
    "Boyer-Moore": {
        "Text 1 (existing)": measure_time(boyer_moore_search, text1, existing_substring),
        "Text 1 (fake)": measure_time(boyer_moore_search, text1, fake_substring),
        "Text 2 (existing)": measure_time(boyer_moore_search, text2, existing_substring),
        "Text 2 (fake)": measure_time(boyer_moore_search, text2, fake_substring),
    },
    "Knuth-Morris-Pratt": {
        "Text 1 (existing)": measure_time(kmp_search, text1, existing_substring),
        "Text 1 (fake)": measure_time(kmp_search, text1, fake_substring),
        "Text 2 (existing)": measure_time(kmp_search, text2, existing_substring),
        "Text 2 (fake)": measure_time(kmp_search, text2, fake_substring),
    },
    "Rabin-Karp": {
        "Text 1 (existing)": measure_time(rabin_karp_search, text1, existing_substring),
        "Text 1 (fake)": measure_time(rabin_karp_search, text1, fake_substring),
        "Text 2 (existing)": measure_time(rabin_karp_search, text2, existing_substring),
        "Text 2 (fake)": measure_time(rabin_karp_search, text2, fake_substring),
    },
}

# Вывод результатов

df = pd.DataFrame(results)
print("Результаты сравнения алгоритмов:")
print(df)