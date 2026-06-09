def remove_fourth_character(word: str) -> str:
    first_three_char = word[:3]
    remaining_char = word[4:]
    resultant_char = first_three_char + remaining_char
    return resultant_char

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
