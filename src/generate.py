import string

lower_case_alphabets = list(string.ascii_lowercase)
upper_case_alphabets = list(string.ascii_uppercase)
numbers = list(string.digits)
punctuation = list(string.punctuation)


length = int(input("What is the length of the password you want ? "))


characters_list = lower_case_alphabets + upper_case_alphabets + numbers + punctuation

import random

password_characters = random.sample(characters_list, length)

password = "".join(password_characters)

print(password)
