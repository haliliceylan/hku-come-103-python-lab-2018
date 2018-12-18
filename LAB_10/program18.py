def main():
    file_variable = open('words.txt', 'w')
    word_count = int(input('how many word want you enter:'))

    for x in range(word_count):
        current_word = input('Enter Word:')
        file_variable.write(current_word + "\n")
    file_variable.close()


main()
