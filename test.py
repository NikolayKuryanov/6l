def prime_calculator(first, operator, second):
    if type(first) not in [int, float] or type(second) not in [int, float]:
        raise TypeError('Incorect input')
    if operator not in '-+*/':
        raise ValueError('operator should be one of thi s: +, -, *, /')
    if operator == '+': return first+second
    if operator == '-': return first - second
    if operator == '*': return first*second
    if operator == '/': return first/second

