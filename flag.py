class ArgumentError(Exception):

    def __init__(self, message='N shall be an integer even number'):
        super().__init__(message)


def get_circle_line(k, border_symbol, width):
    circle_symbol = "oo"
    circle = circle_symbol * k
    horizontal_distance = (width / 2) - 1 - k
    return f'{border_symbol}{"":{horizontal_distance}}*{circle}*{"":{horizontal_distance}}{border_symbol}\n'


def flag(n):
    try:
        if n % 2 != 0 or n <= 0:
            raise ArgumentError
        border_symbol = '#'
        width = n * 3
        border_line = border_symbol * (width + 2)
        empty_line = f'{border_symbol}{"":{width}}{border_symbol}\n'
        half_height = int(n / 2)
        empty_line = empty_line * half_height
        circle_line = ''.join([get_circle_line(k, border_symbol, width) for k in range(half_height)])
        s = f'{border_line}\n{empty_line}{circle_line[:-1]}{circle_line[::-1]}\n{empty_line}{border_line}'
        return s
    except ArgumentError as err:
        print(err)


def main():
    n = int(input('Input parameter N\n'))
    print(flag(n))


if __name__ == '__main__':
    main()
