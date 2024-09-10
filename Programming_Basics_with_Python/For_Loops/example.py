import random
from string import ascii_letters, digits, punctuation

# Combine all character sets
all_character = ascii_letters + digits + punctuation

password_length = 12

password = "".join(random.sample(all_character, password_length))

print(password)
