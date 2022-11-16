import re

text = input('\n\tВведите текст: ')
lower_text = text.lower()
split_text = re.split('[ ,.!?;:()\[\]"\'`\-_|/]+', lower_text)

popular_words = {}
popular_letters = {}

for word in split_text:
    if word in popular_words:
        popular_words[word] += 1
    else:
        popular_words[word] = 1

    for letter in word:
        if letter in popular_letters:
            popular_letters[letter] += 1
        else:
            popular_letters[letter] = 1

print('\n\tСловарь популярных слов: {0}'.format(popular_words))
print(f'\tСловарь популярных букв: {popular_letters}')