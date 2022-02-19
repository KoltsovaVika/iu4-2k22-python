import sys


def caesar_cipher(d_e: str = 'd', string_to_work: str = "ZzY9", key: int = 2):
    """
    Caesar ciphers for encoding and decoding strings
        :param
        string_to_work: Line to change
        key: if the key is greater than zero, then encode, if the key is less than zero, then decode
    """
    numbers = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    end_string = []

    if d_e == 'd':
        key = -key
    elif d_e == 'e':
        key = key
    else:
        print("Not expected value d/e:", d_e)
        sys.exit(-1)

    for i in string_to_work:
        if i in numbers:
            a = (numbers.index(i) + key) % 10
            end_string.append(numbers[a])

        elif i in uppercase:
            a = (uppercase.index(i) + key) % 26
            end_string.append(uppercase[a])

        elif i in lowercase:
            a = (lowercase.index(i) + key) % 26
            end_string.append(lowercase[a])
        else:
            print("Invalid symbol:", i)
            sys.exit(-1)

    print("Old value:", string_to_work)
    print("New value:", "".join(end_string))


def main(arg: list):
    if len(arg) != 4:
        print("Wrong number of values", len(arg))
        sys.exit(-1)

    caesar_cipher(arg[1], arg[2], int(arg[3]))
    # Функции для проверки шифра
    #caesar_cipher("e", "Bat2022", 5)
    #caesar_cipher("d", "Gfy7577", 5)


if __name__ == '__main__':
    main(sys.argv)
