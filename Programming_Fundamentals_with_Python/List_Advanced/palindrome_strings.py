"""
# Read the input
strings = input().split(" ")
searched_palindrome = input()

# List to store found palindromes
palindromes = []

# Loop through each word in the input
for word in strings:
    # Check if the word is a palindrome
    if word == word[::-1]:  # Reverse the word and check equality
        palindromes.append(word)

# Output the list of palindromes
print(palindromes)

# Output the count of the searched palindrome
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")


# second solution
strings = input().split(" ")
searched_palindrome = input()
palindromes = [word for word in strings if word == word[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")"""

# third solution
words = input().split()
special_palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]
count_of_special_palindrome = palindrome_list.count(special_palindrome)

print(palindrome_list)
print(f"Found palindrome {count_of_special_palindrome} times")



