word = input('Enter your word: ')
reverse = ""
n = 1

for i in word:
    reverse += word[-n]
    n += 1

if reverse == word:
    print('It is a palindrome.')
else:
    print('It is not palindrome.')
