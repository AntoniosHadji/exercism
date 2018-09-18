import re


def hey(phrase):
    ''' test phrase to determine output  '''
    only_whitespace = re.search(r'^\s+$', phrase)

    question = re.search(r'.+\?\s*$', phrase)
    q_all_caps_with_whitespace = re.search(r'^[A-Z\s]+\?\s*$', phrase)
    numbers_comma_whitespace = re.search(r'^[0-9,\s]+$', phrase)
    everything_not_lower_case = re.search(r'^[^a-z]+[\!\s]*$', phrase)

    if only_whitespace or len(phrase) == 0:
        return 'Fine. Be that way!'
    elif q_all_caps_with_whitespace:
        return "Calm down, I know what I'm doing!"
    elif question:
        return 'Sure.'
    elif everything_not_lower_case and not numbers_comma_whitespace:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
