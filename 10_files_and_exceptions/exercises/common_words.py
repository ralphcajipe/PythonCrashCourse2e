def count_common_words(filename, word):
    """Count how many times the word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


filenames = ['davinci.txt', 'science_kitchen.txt', 'ten_thousand.txt']
for filename in filenames:
    count_common_words(filename, 'the')
    count_common_words(filename, 'the ')
    print()
