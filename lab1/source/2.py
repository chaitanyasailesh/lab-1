def longest_substring(s):

    a = []                  # current list
    b = []                  # for all substrings
    for item in s:
        if item in a:
            b.append(''.join(a))            # finds a char already in the array, it maintains a copy of the array
            c = a.index(item) + 1
            a = a[c:]                       # cuts off beginning of it up to that character and keeps building it.
        a += item
    b.append(''.join(a))

    length = max(len(x) for x in b)
    for x in b:
        if len(x) == length:
            print(x, len(x))


longest = longest_substring("pwwkew")