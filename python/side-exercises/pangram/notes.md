other answer used sets and .issubset method

```python
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(string):
    return ALPHABET.issubset(string.lower())
```


using all builtin

```python
def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)
```

using set to track letters used
```python
	letters = set(sub('[^a-z]','',phrase.lower()))
```

