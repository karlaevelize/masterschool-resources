# SET counter to 0
# For each character in the string:
#     If current char is not space:
#         If last char is space OR current char is first char:
#             COUNTER += 1
# return COUNTER

# Solution 1
def count_words(s):
    counter = 0
    for i in range(len(s)):
        if s[i] != ' ':
            if i == 0 or s[i - 1] == ' ':
                counter += 1
    return counter

print(count_words("The quick brown fox jumps over the lazy dog."))

# Solution 2
def count_words_split(s):
    words = s.split()
    return len(words)

print(count_words_split("The quick brown fox jumps over the lazy dog."))