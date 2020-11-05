#  Work on project. Stage 6/6: Escaping 

## Description

Since ^, $, ?, *, + and . are now reserved as metacharacters, they cannot be used as literals. This might be a problem, for example, when you want to match the end of sentences. In this case, you would look for words that are succeeded by a period or a question mark. Since these characters have a special meaning in the regex notation, they would not get matched the way you want it.
To solve this problem, the regex notation has a so called escape sequence: if a metacharacter is preceded by a backward slash (\), it is considered as a normal literal and can be matched.
Objectives

Just like it was with the metacharacters, some more conditions should be added to the recursive function to handle the escape symbols.

The semantics of the backward slash is really simple: the character that follows it should be interpreted as a literal. This way, a simple string comparison is enough to determine a match. You should also take care of skipping the escape sequence before continuing the recursion. This can be done using the same logic that we used to handle the repetition operators ?, *, and +.

There is also a technical fact you should keep in mind: the \ symbol is an escape sequence not only in the regex notation but also in strings. This means that typing \ opens a string escape sequence that can be followed by some specific command of the programming language. For example, \n signifies a new line, like Enter. Strangely enough, to get a literal \ in most programming languages, you should repeat the backslash twice, like this: \\. For example, a literal period for the regex engine looks like this \\., a question mark looks like this \\?, and an asterisk looks like this \\*.

Here is another riddle. If the backward slash \ is now an escape sequence, how can it be matched as a literal in a string? What if you want to find every string that ends with the character \? Check out the examples below to see what the engine does in this case.
## Examples

    Input:      '\.$|end.'              Output: True
    Input:     '3\+3|3+3=6'             Output: True
    Input:       '\?|Is this working?'  Output: True
    Input:       '\\|\'                 Output: True
    Input: 'colou\?r|color'             Output: False
    Input: 'colou\?r|colour'            Output: False