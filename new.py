def string_checker(x):
    return len(set(x)) == len(x)
print(string_checker("hello"))
print(string_checker("world"))