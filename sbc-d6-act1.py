word = input("Enter a word: ")
orig_word = ''.join(word.split()).lower()
is_palindrome = True

for i in range(len(orig_word) // 2):
    if orig_word[i] != orig_word[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")