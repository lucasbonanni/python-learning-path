# Work on project. Stage 5/6: Controlling repetition 
## Description

What could be better than metacharacters? More metacharacters! In this stage, you should add the following metacharacters to your engine:

    ? matches the preceding character zero times or once;
    * matches the preceding character zero or more times;
    + matches the preceding character once or more times.

Let's consider these in more detail. Basically, the most important feature of a regex engine is the presence of the repetition operators ?, *, and +. They are used to determine how many times a certain character or sequence can be repeated in the string. These operators can make a regular expression really compact and elegant.

Let's look at the sequence aaaaaaaaaab. We can match this string with the following regular expressions: aaaaaaaaaab, a*b, a+b, .*b, .+b. If you want a more realistic example, here is one: the regex colou?r should match the strings color and colour.

As you can see, the main role of these operators is to control the repetition of the preceding character.

Note that the wildcard (.) can also be placed before these operators, in which case any character is matched zero or several times.

## Objectives

The best way to implement these metacharacters is by adding more conditions to the function that matches the patterns of equal length.

In the case of the operator ?, there are two possible scenarios:

    The preceding character occurs zero times, so basically it is skipped. This means that only the part of the regex after the metacharacter ? is passed to the recursive function along with the unmodified input string.
    The preceding character occurs once. This means that if the character preceding ? matches the first character of the input string, the part of the regex after ? is passed to the recursive function along with the part of the input string without the character that is already matched.

In the case of the operator *, there are the following scenarios:

    The preceding character occurs zero times (just like with ?). The condition from the previous case can be reused.
    The preceding character occurs one or more times. Like in the case of ?, the character preceding * should match the first character of the input string. Since we don’t know how many times it is going to be repeated, the regex should be passed to the recursive function without any modification, and the first character of the input string should be chopped off. In this case, since the metacharacter * is not removed, the second case is repeated until the preceding character can be matched. After that, the first case applies and the function comes out of the recursion.

Finally, here is what can happen with the operator +:

    The preceding character occurs once. This case is the same as the second case with the operator ?.
    The preceding character occurs more than once. This case is basically the same as the second case with the operator *.

You could create separate functions for each operator and invoke them from the match function, or you could include these cases into that function. The important thing to understand is that the logic of recursion does not change with the implementation of these operators, but you might have to fiddle with the number of characters that are going (or not going) to be sliced. Use boolean logic where possible in order to simplify the code and minimize the number of if else clauses.
Examples

    Input: 'colou?r|color'       Output: True
    Input: 'colou?r|colour'      Output: True
    Input: 'colou?r|colouur'     Output: False
    Input: 'colou*r|color'       Output: True
    Input: 'colou*r|colour'      Output: True
    Input: 'colou*r|colouur'     Output: True
    Input:  'col.*r|color'       Output: True
    Input:  'col.*r|colour'      Output: True
    Input:  'col.*r|colr'        Output: True
    Input:  'col.*r|collar'      Output: True
    Input: 'col.*r$|colors'      Output: False

    ? matches the preceding character zero times or once;
    * matches the preceding character zero or more times;
    + matches the preceding character once or more times.

1. podría encontrar la posición del operador, buscar el caracter anterior guardarlo, buscar el segundo anterior y su posición, y el caracter siguiente al operador.
2. Desde la posición del primer caracter (o) empiezo a contar en el string cuantos matches hasta el caracter final (r).
3. y poner true o false en base a la cuenta y el operador.
4. Remover la parte del string y que siga con las siguientes operaciones.