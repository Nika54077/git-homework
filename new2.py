def string_counter(x):
    string_count = {}
    for i in x:
        if i in string_count:
            string_count[i] += 1
        else:
            string_count[i] = 1
    return string_count
print(string_counter("hello"))