def check_char(regex, char):
    if not char:
        return False
    if regex == '.':
        return True
    return regex == char


def check_question(regex, string):
    if check_char(regex[0], string[0:1]) and check_str(regex[2:], string[1:]):
        return True
    return check_str(regex[2:], string)


def check_star(regex, string):
    if check_char(regex[0], string[0:1]) and check_str(regex, string[1:]):
        return True
    return check_str(regex[2:], string)


def check_plus(regex, string):
    return check_char(regex[0], string[0:1]) and (check_str(regex, string[1:]) or check_str(regex[2:], string[1:]))


def check_str(regex, string):
    if not regex:
        return True
    if regex == '$' and not string:
        return True
    if regex[1:2] == '?':
        return check_question(regex, string)
    if regex[1:2] == '*':
        return check_star(regex, string)
    if regex[1:2] == '+':
        return check_plus(regex, string)
    return check_char(regex[0], string[0:1]) and check_str(regex[1:], string[1:])


def search(regex, string):
    if not regex:
        return True
    if regex[0:1] == '^':
        return check_str(regex[1:], string)
    return check_str('.*' + regex, string)

if __name__ == "__main__":
    print(search(*input().split('|')))
