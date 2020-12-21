def cesar_cipher(sentence: str, step: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_sentence = ''

    for letter in sentence:
        if letter.isspace():
            new_sentence += ' '
            continue
        else:
            finder = (alphabet.find(letter.lower()) + step) % len(alphabet)
            new_sentence += alphabet[finder].upper() if letter.isupper() else alphabet[finder]
    
    return new_sentence


while True:
    print('##### CESAR CIPHER #####')
    print('EN: Type the word you need encrypt and the value of the lag for encrypt or type 0 to leave')
    print('Ex: uaStwT 2 or just type 0 to leave')
    
    sentence = input()
    if sentence == '0':
        print('Saiu/Leave')
        break
    step = int(input())

    print(cesar_cipher(sentence, step))
    print('')
