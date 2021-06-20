name = input()


def normalize(name_str):
    # put your code here
    new_name = str(name_str)
    new_name = new_name.replace('é', 'e', new_name.count('é')) \
        .replace('ë', 'e', new_name.count('ë')) \
        .replace('á', 'a', new_name.count('á')) \
        .replace('å', 'a', new_name.count('å')) \
        .replace('œ', 'oe', new_name.count('œ')) \
        .replace('æ', 'ae', new_name.count('æ'))

    return new_name


print(normalize(name))
