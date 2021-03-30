# The version they want

def get_num_of_non_WS_characters(usr_str):
    cnt = 0
    for i in range(len(usr_str)):
        if usr_str[i] != ' ':
            cnt += 1
    return cnt

def get_num_of_words(usr_str):
    cnt = 0
    str_words = usr_str.split()
    for i in range(len(str_words)):
        cnt += 1
    return cnt


def fix_capitalization(usr_str):
    cnt = 0
    final_str = ''
    usr_list = usr_str.split('. ')
    for i in range(len(usr_list)):
        cnt += 1
        final_str += ''.join(usr_list[i].capitalize())
        if i != len(usr_list) - 1:
            final_str += '. '
    return final_str, cnt



def replace_punctuation(usr_str, exclamation_count, semicolon_count):
    final_str = ''
    for i in range(len(usr_str)):
        if usr_str[i] == ';':
            final_str += ','
        elif usr_str[i] == '!':
            final_str += '.'
        else:
            final_str += usr_str[i]
    return final_str

def shorten_space(usr_str):
    final_str = ''
    for i in range(len(usr_str)):
        if usr_str[i] == ' ':
            if usr_str[i-1] == ' ':
                final_str += ''
            else:
                final_str += ' '
        else:
            final_str += usr_str[i]
    return final_str


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
        menu_op = input('Choose an option:\n')
        if menu_op == 'q':
            break
        elif menu_op == 's':
            print('Edited text:', shorten_space(usr_str))
            print('')
        elif menu_op == 'r':
            exclamation = 0
            semicolon = 0
            for i in range(len(usr_str)):
                if usr_str[i] == ';':
                    semicolon += 1
                if usr_str[i] == '!':
                    exclamation += 1
            print('Punctuation replaced')
            print('exclamation_count:', exclamation)
            print('semicolon_count:', semicolon)
            print('Edited text:', replace_punctuation(usr_str, exclamation, semicolon))
            print('')
        elif menu_op == 'f':
            fix_capitalization(usr_str)
        elif menu_op == 'w':
            print('Number of words:', get_num_of_words(usr_str))
            print('')
        elif menu_op == 'c':
            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(usr_str))
            print('')
        else: # if user enters incorrect input
            continue

    return menu_op, usr_str



if __name__ == '__main__':
    input_str = input('Enter a sample text:\n\n')
    print('You entered:', input_str)
    print('')
    print_menu(input_str)