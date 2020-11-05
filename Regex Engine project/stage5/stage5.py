# write your code here
class Regexp:

    def __init__(self, regexp):
        self.result = False
        regexp, text = regexp.split('|')
        self.check_repetition_char(regexp, text)

    def evaluate(self, regexp, text):
        if len(regexp) == 0:
            self.result = True
        elif len(text) == 0:
            self.result = False
        elif (regexp[0] == text[0]) or (regexp[0] == '.'):
            self.evaluate(regexp[1:], text[1:])
        else:
            self.result = False

    def __str__(self):
        return str(self.result)

    def count_char_matches(self, text, starting_pos, final_letter):
        """
        it counts character matches
        """
        counter = 0
        for pos in range(starting_pos, len(text), 1):
            if text[pos] != final_letter:
                counter += 1
            else:
                break
        return counter

    def check_repetition_char(self, regexp, text):
        if len(text) == 0 and len(regexp) == 0:
            self.result = True
        if regexp.find('?') > -1:
            pos = regexp.find('?')
            if len(regexp) > 2:
                final_letter = regexp[pos+1]
                matches = self.count_char_matches(text, pos - 1, final_letter)
                if matches == 0 or matches == 1:
                    exp = regexp[pos - 1:pos + 1]
                    t_exp = text[0:pos - 1] + text[pos + matches - 1:len(text)]
                    self.check_parts(regexp.replace(exp, ''), t_exp)
                else:
                    self.result = False  # debería salir
            else:
                self.check_parts(regexp.replace('?',''),text)
        if regexp.find('*') > -1:

            pos = regexp.find('*')
            if len(regexp) > 2:
                final_letter = regexp[pos+1]
                matches = self.count_char_matches(text, pos - 1, final_letter)
                if matches >= 0 or matches == 1:
                    exp = regexp[pos - 1:pos + 1]
                    t_exp = text[0:pos - 1] + text[pos + matches - 1:len(text)]
                    self.check_parts(regexp.replace(exp, ''), t_exp)
                else:
                    self.result = False  # exit
            else:
                self.check_parts(regexp.replace('*',''),text)
            exp = regexp[pos - 1:pos + 1]
            regexp.replace(exp, '')
            text.replace(exp[0], '')
        if regexp.find('+') > -1:
            pos = regexp.find('+')
            if len(regexp) > 2:
                final_letter = regexp[pos+1]
                matches = self.count_char_matches(text, pos - 1, final_letter)
                if matches >= 1:
                    exp = regexp[pos - 1:pos + 1]
                    t_exp = text[0:pos - 1] + text[pos + matches - 1:len(text)]
                    self.check_parts(regexp.replace(exp, ''), t_exp)
                    print(matches, regexp, text)
                else:
                    self.result = False  # exit
            else:
                self.check_parts(regexp.replace('+',''),text)
        else:
            self.check_parts(regexp,text)

    def check_parts(self, regexp, text):
        """
        Takes a regexp and a text to evalueate
        """
        if regexp.startswith('^') and not regexp.endswith('$'):
            regexp = regexp.replace('^', '')
            part = text[0: 0 + len(regexp)]
            self.evaluate(regexp, part)
        elif regexp.endswith('$') and not regexp.startswith('^'):
            regexp = regexp.replace('$', '')
            part = text[len(text) - len(regexp): len(text)]
            self.evaluate(regexp, part)
        elif regexp.startswith('^') and regexp.endswith('$'):
            regexp = regexp.replace('^', '')
            regexp = regexp.replace('$', '')
            self.result = regexp == text
        else:
            for i in range(len(text)):
                if not self.result:
                    part = text[i: i + len(regexp)]
                    self.evaluate(regexp, part)


if __name__ == "__main__":
    print(Regexp(input()))
