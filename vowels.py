vowel = ['a', 'e', 'i', 'o', 'u']
word = input("enter a word: ")
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

