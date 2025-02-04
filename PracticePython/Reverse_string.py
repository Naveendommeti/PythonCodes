#using slicing concept s[::-1]
# def rev_string(a):
#     return a[::-1]
# text = input("Enter the string: ")
# print(f"reversed string is: {rev_string(text)}")

#using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])
# text = input("Enter string: ")
# print(f"Reverse string is {reverse_string(text)}")

#reverse each word
def reverse_each_word(sentence):
    words = sentence.split()
    reverse_word = [word[::-1] for word in words]
    return " ".join(reverse_word)
text = input("Enter the string: ")
print(f"Reverse of string: {reverse_each_word(text)}")

