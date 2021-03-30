def get_num_of_non_WS_characters():
    pass

def get_num_of_words():
    pass

def fix_capitalization():
    pass

def replace_punctuation():
    pass

def shorten_space():
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
            shorten_space()
        elif menu_op == 'r':
            replace_punctuation()
        elif menu_op == 'f':
            fix_capitalization()
        elif menu_op == 'w':
            get_num_of_words()
        elif menu_op == 'c':
            get_num_of_non_WS_characters()
        else: # if user enters incorrect input
            continue

    return menu_op, usr_str



if __name__ == '__main__':
    input_str = input('Enter a sample text: ')
    print('You entered:', input_str)
    print_menu(input_str)