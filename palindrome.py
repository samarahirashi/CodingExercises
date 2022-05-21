# Palindrome

def isPalindrome(text):
    return text == text[::-1]


if __name__ == '__main__':
    str = 'level'
    result = isPalindrome(str)

    if result:
        print("Yes it is")
    else:
        print("No it isn't")

