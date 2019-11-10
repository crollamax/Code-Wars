def create_phone_number(num_list):
    output = '('
    for idx, num in enumerate(num_list):
        if idx == 3:
            output += ') '
        elif idx == 6:
            output += '-'
        output += str(num)
    return num