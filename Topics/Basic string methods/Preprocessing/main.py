string = input()

new_string = string.replace('!', '').replace('?', '').replace('.', '').replace(',', '').lower()

print(new_string)
