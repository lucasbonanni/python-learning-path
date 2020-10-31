# What you'll do in this stage 4/6: Implementing the operators ^ and $

## Description

Regular expressions are useful and flexible because they include a set of metacharacters. So far, the only metacharacter we can handle is the wild-card (.). Although it is certainly useful, our engine still lacks the flexibility we need.

Let's think of a case where we would want a pattern to match only if it happens in a certain part of the input string, for example, only the beginning or the end. Do you remember the example from the previous stage where we wanted to match only the nouns that end with the suffix tion? That's exactly the case where we need the metacharacter $. The regex tion$ will match the string section but not sections, even though tion is part of both strings.

The metacharacter ^ is the opposite: it only matches a pattern if it is located at the beginning of the input string. This way, the regex ^be will match the strings beware, become, behind, but not to be, even though it contains be.

## Objectives

Your task is to add some metacharacters to the already existing regex engine.

At this stage, you should add the following special cases:

    ^ can occur at the beginning of the regex, and it means that the following regex should be matched only at the beginning of the input string.
    $ can occur at the end of the regex, and it means that the preceding regex should be matched only at the end of the input string.

Actually, the engine already contains a function that matches only the beginning of the input string: you created one in the second stage! Yet you should directly invoke it from the current entry point only if the regex starts with the character ^. Also, do not forget that you shouldn’t pass the regex ^ itself to the function!

The case with $ is a bit more complicated. Don't worry: with a little thinking, we can get our heads around it. How do we know if the input string ends with the regex succeeded by $? Normally, if a regex matches the end of a string, they are consumed at the same iteration, and True is returned according to the terminating conditions. However, since $ is a metacharacter, it should be at the end of the regex when the input string has already been consumed. At the current state of the function, it should return False because the input string is consumed while the regex is not. Yet since we know that $ has a special meaning, if we see it as the last character of a string, we should assume that the input string is empty. It should be checked, and if that is the case, the function should return True.

    Note: the position of the terminating conditions can alter the behavior of the function! This condition should be added after the regex has been determined as empty or not, but before the same is determined for the input string.

## Examples

    Input:    '^app|apple'           Output: True
    Input:     'le$|apple'           Output: True
    Input:      '^a|apple'           Output: True
    Input:      '.$|apple'           Output: True
    Input:  'apple$|tasty apple'     Output: True
    Input:  '^apple|apple pie'       Output: True
    Input: '^apple$|apple'           Output: True
    Input: '^apple$|tasty apple'     Output: False
    Input: '^apple$|apple pie'       Output: False
    Input:    'app$|apple'           Output: False
    Input:     '^le|apple'           Output: False