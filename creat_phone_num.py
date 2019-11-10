'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parenthesis!

'''


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
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*num_list)