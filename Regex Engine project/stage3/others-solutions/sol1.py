def regexp_engine(pattern, letter):
    return pattern in ('', '.', letter)


def match_regexp(pattern, substring):
    if not pattern:  # pattern is empty always True
        return True
    if substring:  # if string is not empty try the regexp engine
        if regexp_engine(pattern[0], substring[0]):  # if reg and letter match
            return match_regexp(pattern[1:], substring[1:])
    return False  # if reg and letter not match or string has been consumed


def regexp(pattern, word):
    # check if word is empty but catch the condition ' | '
    if not word and pattern:
        return False
    # if string is not empty so feeds params into regexp match
    if not match_regexp(pattern, word):
        # if regexp return False, try to cut the word
        return regexp(pattern, word[1:])
    return True


print(regexp(*(input().split('|'))))