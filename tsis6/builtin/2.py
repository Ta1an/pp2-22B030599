import re
def count_letters():
    string = str(input())
    lowercase = re.compile("[a-z]")
    uppercase = re.compile("[A-Z]")
    lowercase_letters = str.findall(lowercase)
    uppercase_letters = str.findall(uppercase)
    print(f'Number of lowercase letters = {len(lowercase_letters)}, Num of uppercase letters = {len(uppercase_letters)}')