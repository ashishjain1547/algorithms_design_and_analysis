from collections import Counter

def can_convert(s, t):
    if len(s) != len(t):
        return "No"
    count_s = Counter(s)
    count_t = Counter(t)

    wildcards_s = count_s.get('?', 0)

    for char in count_t:
        if count_t[char] > count_s.get(char, 0):
            needed = count_t[char] - count_s.get(char, 0)
            wildcards_s -= needed
            if wildcards_s < 0:
                return "No"
        elif count_s.get(char, 0) > count_t[char]:
            return "No"
    return "Yes"

    

T = int(input())
for _ in range(T):
    N = int(input())
    s = input().strip()
    t = input().strip()
    print(can_convert(s, t))