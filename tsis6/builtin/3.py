def IsPalindrome(s):
    if s == str.join("", list(reversed(s))):
        print("It is palindrome")
    else:
        print("It is not palindrome")