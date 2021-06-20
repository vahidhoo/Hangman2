input_value = float(input())

if input_value < 2.0:
    print('Analytic')
elif 2.0 <= input_value <= 3.0:
    print('Synthetic')
else:
    print('Polysynthetic')
