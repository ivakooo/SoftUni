def characters_between(first, second):
    all_characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        all_characters.append(chr(current_character))
    return all_characters


first_character = input()
second_character = input()
result = characters_between(first_character, second_character)
print(" ".join(result))
