text = ""
words = text.split()

longest_word = ''
shortest_word = ''
longest_word_length = 0
shortest_word_length = 0

for word in words:
    print(word)
    current_word_length = len(word)
    print(current_word_length)

    if current_word_length > longest_word_length:
        longest_word_length = current_word_length
        longest_word = word

    if shortest_word_length == 0:
        shortest_word_length = current_word_length
        shortest_word = word

    if current_word_length < shortest_word_length:
        shortest_word_length = current_word_length
        shortest_word = word

print(f"{longest_word_length=} {longest_word=}")
print(f"{shortest_word_length=} {shortest_word=}")