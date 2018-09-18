import re


def hey(phrase):
    ''' test phrase to determine output  '''
    only_whitespace = re.search(r'^[\s]+$', phrase)
    q_with_number = re.search(r'\d+.*\?$', phrase)
    q_ends_with_whitespace = re.search(r'\?\s*$', phrase)
    q_all_caps_with_whitespace = re.search(r'^[A-Z\s]+\?\s*$', phrase)
    numbers_comma_whitespace = re.search(r'^[0-9\,\s]+$', phrase)
    everything_not_lower_case = re.search(r'^[^a-z]+[\!\s]*$', phrase)

    if only_whitespace or len(phrase) == 0:
        return 'Fine. Be that way!'
    elif q_with_number or (q_ends_with_whitespace and
                           not q_all_caps_with_whitespace):
        return 'Sure.'
    elif q_ends_with_whitespace and q_all_caps_with_whitespace:
        return "Calm down, I know what I'm doing!"
    elif everything_not_lower_case and not numbers_comma_whitespace:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
