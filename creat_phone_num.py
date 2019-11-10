def create_phone_number(num_list):
    output = '('
    for idx, num in enumerate(num_list):
        if idx == 3:
            output += ') '
        elif idx == 6:
            output += '-'
        output += str(num)
    return output

def create_phone_number_improved(num_list):
    return "({}{}{}) {}{}{}-{}{}{}".format(*num_list)