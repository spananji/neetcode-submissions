def first_n_characters(s: str, n: int) -> str:
    my_string = s[:n]
    return my_string
def last_n_characters(s: str, n: int) -> str:
    my_string =s[len(s)-n:]
    return my_string


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
