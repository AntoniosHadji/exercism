import re


def hey(phrase):
    # test for containing only whitespace
    a = re.search(r'^[\s]+$', phrase)
    if a or len(phrase) == 0:
        return 'Fine. Be that way!'

    # test contains number and ends in ?
    b = re.search(r'\d+.*\?$', phrase)
    # test ends with ? plus any number of whitespace characters
    c = re.search(r'\?\s*$', phrase)
    # test all caps and spaces,  ends in ? plus 0 or more spaces
    d = re.search(r'^[A-Z\s]{2,}\?\s*$', phrase)
    if b or (c and not d):
        return 'Sure.'
    if c and d:
        return "Calm down, I know what I'm doing!"

    # multiline
    e = re.search(r'\n', phrase)
    # does phrase contain ?
    f = re.search(r'\?', phrase)
    # does phrase end with whitespace
    g = re.search(r'\s+$', phrase)
    # does phrase start with whitespace
    j = re.search(r'^\s+', phrase)
    # only numbers commas whitespace
    h = re.search(r'^[0-9\,\s]+$', phrase)
    # contains ? in middle of statement
    k = re.search(r'.+\?.+', phrase)
    # ends in a period (statement)
    m = re.search(r'.+\.$', phrase)
    # ends in an exclamation mark
    n = re.search(r'\!$', phrase)
    # contains lower case letters
    o = re.search(r'[a-z]', phrase)

    if m or e or h or j or k or (not f and g) or (n and o):
        return 'Whatever.'

    # numbers and capital letters
    # i = re.search(r'^[A-Z\s0-9\,]{2,}\!*\s*$', phrase)
    # everything other than lower case
    i = re.search(r'^[^a-z]{2,}\!*\s*$', phrase)
    if i:
        return 'Whoa, chill out!'
