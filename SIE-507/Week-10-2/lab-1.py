highway_number = int(input())

if highway_number == 0:
    print('0 is not a valid interstate highway number.')
elif highway_number < 0:
    print('0 is not a valid interstate highway number.')
elif highway_number < 100:
    if (highway_number%2) == 0:
        print('I-{} is primary, going east/west.'.format(highway_number))
    else:
        print('I-{} is primary, going north/south.'.format(highway_number))
elif highway_number > 100:
    str_hw = str(highway_number)
    str_hw_removed_digit = str_hw[1] + str_hw[2]
    if (int(str_hw_removed_digit)%2) == 0:
        print('I-{highway_number} is auxiliary, serving I-{str_hw_removed_digit}, going east/west.'.format(highway_number,str_hw_removed_digit))
    else:
        print('I-{highway_number} is auxiliary, serving I-{str_hw_removed_digit}, going east/west.'.format(highway_number,str_hw_removed_digit))
