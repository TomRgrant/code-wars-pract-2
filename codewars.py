def spin_words(sentence):
    index = 0
    new_sentence = []
    new_word = []
    sentence = sentence.split()

    for word in sentence:

        if len(word) >= 5:
            for letter in word:
                new_word.insert(0, letter)

            new_word = "".join(new_word)
            new_sentence.insert(index, new_word)
            new_word = []
            index += 1

        else:
            new_sentence.insert(index,word)
            index += 1

    new_sentence = " ".join(new_sentence)

    return new_sentence




assert spin_words('Hello my name is Timothy') == 'olleH my name is yhtomiT'