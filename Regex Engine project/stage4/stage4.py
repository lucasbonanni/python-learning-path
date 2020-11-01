# write your code here
class Regexp:

    def __init__(self, regexp):
        self.result = False
        regexp, text = regexp.split('|')
        self.check_parts(regexp, text)

    def evaluate(self, regexp, text):
        if (len(regexp) == 0) or (len(regexp) == 0 and len(text) == 0):
             self.result = True
        elif len(text) > 0 and ((regexp[0] == '.' and len(text[0]) == 1) or (regexp[0] == text[0])):
            self.evaluate(regexp[1:], text[1:])
        else:
            self.result = False

    def __str__(self):
        return str(self.result)

    def check_parts(self, regexp, text):
        """
        Takes a regexp and a text to evalueate
        """
        if len(text) == 0 and len(regexp) == 0:
            self.result = True
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
            print(regexp, text)
            self.evaluate(regexp, text)
        else:
            for i in range(len(text)):
                if not self.result:
                    part = text[i: i + len(regexp)]
                    self.evaluate(regexp, part)


#print(Regexp(input()))
