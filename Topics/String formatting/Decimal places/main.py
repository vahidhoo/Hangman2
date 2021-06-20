number = float(input())
precision = int(input())
split = '.{}f'.format(precision)

print(f'{number:.{precision}f}')
