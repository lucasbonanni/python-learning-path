import sys
sys.setrecursionlimit(10000)

# write your code here
def text_crawler(test_reg, string):
    if len(test_reg) > len(string):
        return False
    elif not regex_str(test_reg, string):
        return text_crawler(test_reg, string[1:])
    else:
        return True

def regex_str(test_reg, test_string):
    if not test_reg:
        return True
    else:
        if not test_string or test_reg[0] not in [".", "", test_string[0]]:
            return False
        return regex_str(test_reg[1:], test_string[1:])

regex, string = input().split('|')
print(text_crawler(regex, string))