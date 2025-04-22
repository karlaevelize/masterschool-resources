# Pseudo code
## Task:

Count the number of words in a sentence

`"The quick brown fox jumps over the lazy dog."`

SET counter to 0
For each character in the string:
    If current char is not space:
        If last char is space OR current char is first char:
            COUNTER += 1
return COUNTER
