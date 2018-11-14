instead of modulus on index, could use following pattern:

`newchars = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]`

this returns an alphabet in cipher order

then use `str.maketrans(old_sequence_as_string, new_sequence_as_string)`
and `text.translate(trans_table)`


