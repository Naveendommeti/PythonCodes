def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = input("Enter the string: ")
if palindrome(string):
    print("The string is palindrome")
else:
    print("Is not a palindrome")