def get_num_of_non_WS_characters(usr_str):
    cnt = 0
    for i in range(len(usr_str)):
        if usr_str[i] != ' ':
            cnt += 1
    print('Number of non-whitespace characters: ', cnt)

def get_num_of_words(usr_str):
    cnt = 0
    str_words = usr_str.split()
    for i in range(len(str_words)):
        cnt += 1
    print('Number of words: ', cnt)


def fix_capitalization(usr_str):
    cnt = 0
    #print('. '.join(i.capitalize() for i in usr_str.split('. ')))
    final_str = ''
    usr_list = usr_str.split('. ')
    for i in range(len(usr_list)):
        cnt += 1
        final_str += ''.join(usr_list[i].capitalize())
        if i != len(usr_list) - 1:
            final_str += '. '


    print('Number of letters capitalized:', cnt)
    print('Edited text:', final_str)



def replace_punctuation(usr_str):
    pass

def shorten_space(usr_str):
    pass

def print_menu(usr_str):
    menu_op = ' '
   
    # Infinite loop until quit
    while True:
        print('MENU')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('f - Fix capitalization')
        print('r - Replace punctuation')
        print('s - Shorten spaces')
        print('q - Quit')
        print('')
        menu_op = input('Choose an option: ')
        if menu_op == 'q':
            break
        elif menu_op == 's':
            shorten_space(usr_str)
        elif menu_op == 'r':
            replace_punctuation(usr_str)
        elif menu_op == 'f':
            fix_capitalization(usr_str)
        elif menu_op == 'w':
            get_num_of_words(usr_str)
        elif menu_op == 'c':
            get_num_of_non_WS_characters(usr_str)
        else: # if user enters incorrect input
            continue

    return menu_op, usr_str



if __name__ == '__main__':
    input_str = input('Enter a sample text: ')
    print('You entered:', input_str)
    print_menu(input_str)