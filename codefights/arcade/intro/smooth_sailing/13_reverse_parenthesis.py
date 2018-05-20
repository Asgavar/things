def reverseParentheses(s):
    print(s)
    if '(' not in s:
        return s
    if s[0] == '(' and s[-1] == ')' and '(' not in s[1:-1]:
        return ''.join(reversed(s[1:-1]))
    opened_parens = []
    paren_pairs = []
    for _ in range(len(s)):
        if s[_] == '(':
            opened_parens.append(_)
        if s[_] == ')':
            paren_pairs.append((opened_parens.pop(), _))
    innermost_pair = list(paren_pairs)[0]
    innermost_replacement = reverseParentheses(s[innermost_pair[0]:innermost_pair[1] + 1])
    s_charlist = [c for c in s]
    s_charlist[innermost_pair[0]] = ''
    s_charlist[innermost_pair[1]] = ''
    s_charlist = s_charlist[0:innermost_pair[0] + 1] + list(innermost_replacement) + s_charlist[innermost_pair[1]:]
    print("".join(["a", " ", "v"]))
    return reverseParentheses(''.join(s_charlist))
