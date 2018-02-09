import numpy as np

def rand_word(file_path:str):
    word_list = []
    with open(file_path,'r') as hang_man:
         for line in hang_man.readlines():
             word_list.append(line)

    random_word = np.random.choice(word_list)
    random_word = list(random_word)
    del random_word[-1]
    random_word = ''.join(random_word)

    return random_word

def check(user_input:str):
    input_caps = user_input.upper()
    chosen_letters.append(input_caps)

    if input_caps not in word:
        print('INCORRECT!!!')
        print('Chosen letters: ',' '.join(chosen_letters))
        print('What you have so far: {}'.format(' '.join(answer)))

        global strike
        strike +=1

        out = 'Strikes: ' + str(strike)

        return out

    for idx,char in enumerate(word):
        if input_caps == char:
            answer[idx] = input_caps

    output = ' '.join(answer)
    print('Chosen letters: ',' '.join(chosen_letters))
    return output

def game_restart():
    word = rand_word('Hang_man_words.txt')
    print('\n--------------------\n'
          'THE GAME HAS RESTARTED\n'
          '----------------------\n')


    global chosen_letters
    chosen_letters = []

    global answer
    answer = ['_' for x in range(len(word))]
    global strike
    strike = 0

    print('your word has {} letters'.format(len(word)-1))
    print(' '.join(answer), '\n')

word = rand_word('Hang_man_words.txt')
chosen_letters = []

answer = ['_' for x in range(len(word))]

strike = 0
number_of_tries = float('6')

print('Welcome to hang man')
print('-------------------')
print('your word has {} letters'.format(len(word)-1))
print(' '.join(answer),'\n')



while '_' in answer:

    if strike < number_of_tries:

        user_input = input('Please Choose your letter:')
        print()
        print(check(user_input))

    else:
        if strike == number_of_tries:
            print('--------------------------------------------------')
            print('the word you were trying to get way {}'.format(word))

            restart = input('Would you like to try again with a new word? (y/n)')
            print('--------------------------------------------------')
            restart = restart.upper()

            if restart == 'Y':
                game_restart()

            elif restart == 'N':
                print('\n---------\n'
                      'GAME OVER')
                break
            else:
                print('you did not put in a valid Entry, assumed No')
                break

full_answer = ''.join(answer)
if full_answer == word:
    print('\ncongratulations YOU WIN!!!!')