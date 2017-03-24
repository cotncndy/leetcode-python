def minCount(regex):
    stack = [[float('inf'), 0]]
    for c in regex:
        if c == 'x':
            stack[-1][-1] += 1
        elif c == '|':
            stack[-1] = [min(stack[-1]), 0]
        elif c == '(':
            stack.append([float('inf'), 0])
        elif c == ')':
            pre, cur = stack.pop()
            stack[-1] = [stack[-1][0], stack[-1][1] + min(pre, cur)]
        else:
            raise Exception('Malformed regex')
    return min(stack[-1])

tests = [
        'xxxx',
        '(x)x',
        'xx|xxx',
        '(xxxx)',
        '(x|)x',
        '((xx|)|x)x(xxxx)'
        ]
for test in tests:
    print test, minCount(test)