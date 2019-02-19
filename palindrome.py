import re
user_input = input("Enter a word or sentence to see if it's a palindrome:").lower()

new_sentence = re.sub(r'[^A-Za-z]', "", user_input)

print("You entered:", user_input)

def backwards(reverse):
    """
    This gives you the word spelled in reverse
    """
    print("The word backwards is:", (user_input)[::-1])
    return (user_input)[::-1]
backwards((user_input)[::-1])

def palindrome(p):
    """
    A word or phrase spelled the same way backwards and forwards.
    """

    if new_sentence == (new_sentence)[::-1]:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome")
    return user_input == backwards
palindrome (user_input == backwards)