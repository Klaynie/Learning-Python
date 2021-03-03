from enum import IntEnum


class Commands(IntEnum):
    HELP = 0
    DONE = 1


class Formats(IntEnum):
    PLAIN = 0
    BOLD = 1
    ITALIC = 2
    LINK = 3
    INLINE_CODE = 4
    HEADER = 5
    ORDERED_LIST = 6
    UNORDERED_LIST = 7
    LINE_BREAK = 8


class Prompts(IntEnum):
    CHOOSE = 0
    UKNOWN_FORMATER = 1
    AVAILABLE_FORMATERS = 2
    SPECIAL_COMMANDS = 3
    TEXT = 4
    LEVEL = 5
    LABEL = 6
    URL = 7
    ROWS = 8
    NUMBER = 9
    INVALID_NUMBER = 10
    NEGATIVE_NUMBER = 11


class Symbols(IntEnum):
    HEADER = 0
    URL_LABEL_OPEN = 1
    URL_LABEL_CLOSE = 2
    URL_OPEN = 3
    URL_CLOSE = 4
    ITALIC = 5
    BOLD = 6
    CODE = 7
    SPACE = 8
    ORDERED_LIST = 9
    UNORDERED_LIST = 10


commands = [
    '!help', '!done'
]

formats = [
    'plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'ordered-list', 'unordered-list', 'line-break'
]

prompts = [
    'Choose a formatter: ', 'Unknown formatter or command. Please try again', 'Available formatters:', 'Special commands:', '- Text: ', '- Level: ', '- Label: ', '- URL: ', '- Number of rows: ', '- Row #%d: ', 'Not a valid number', 'The number of rows should be greater than zero'
]

symbols = [
    '#', '[', ']', '(', ')', '*', '**', '`', ' ', '%d. ', '* '
]

formatted_text = ''


def get_user_input(prompt):
    return input(prompt)


def print_help():
    global formatted_text, formats, commands
    print(prompts[Prompts.AVAILABLE_FORMATERS], ' '.join(formats))
    print(prompts[Prompts.SPECIAL_COMMANDS], ' '.join(commands))


def format_plain():
    global formatted_text
    text = get_user_input(prompts[Prompts.TEXT])
    formatted_text += text


def format_bold():
    global formatted_text
    text = get_user_input(prompts[Prompts.TEXT])
    formatted_text += symbols[Symbols.BOLD] + text + symbols[Symbols.BOLD]


def format_italic():
    global formatted_text
    text = get_user_input(prompts[Prompts.TEXT])
    formatted_text += symbols[Symbols.ITALIC] + text + symbols[Symbols.ITALIC]


def format_link():
    global formatted_text
    label = get_user_input(prompts[Prompts.LABEL])
    url = get_user_input(prompts[Prompts.URL])
    formatted_text += \
        symbols[Symbols.URL_LABEL_OPEN] + label + symbols[Symbols.URL_LABEL_CLOSE] \
        + symbols[Symbols.URL_OPEN] + url + symbols[Symbols.URL_CLOSE]


def format_inline_code():
    global formatted_text
    text = get_user_input(prompts[Prompts.TEXT])
    formatted_text += symbols[Symbols.CODE] + text + symbols[Symbols.CODE]


def format_header():
    global formatted_text
    level = int(get_user_input(prompts[Prompts.LEVEL]))
    text = get_user_input(prompts[Prompts.TEXT])
    formatted_text += \
        level * symbols[Symbols.HEADER] \
        + symbols[Symbols.SPACE] + text
    format_line_break()


def list_generator(row, symbol):
    global formatted_text
    text = get_user_input(prompts[Prompts.NUMBER] % row)
    formatted_text += symbol + text
    format_line_break()


def get_number_of_rows():
    result = 0
    try:
        result = int(get_user_input(prompts[Prompts.ROWS]))
    except ValueError:
        print(prompts[Prompts.INVALID_NUMBER])
    if result <= 0:
        print(prompts[Prompts.NEGATIVE_NUMBER])
        result = get_number_of_rows()
    return result


def format_ordered_list():
    global formatted_text
    number_of_rows = get_number_of_rows()
    for row in range(1, number_of_rows + 1):
        symbol = symbols[Symbols.ORDERED_LIST] % row
        list_generator(row, symbol)


def format_unordered_list():
    global formatted_text
    number_of_rows = get_number_of_rows()
    for row in range(1, number_of_rows + 1):
        symbol = symbols[Symbols.UNORDERED_LIST]
        list_generator(row, symbol)


def format_line_break():
    global formatted_text
    formatted_text += '\n'


def input_processor(user_input):
    if user_input == commands[Commands.HELP]:
        print_help()
    elif user_input in formats:
        if user_input == formats[Formats.PLAIN]:
            format_plain()
        elif user_input == formats[Formats.BOLD]:
            format_bold()
        elif user_input == formats[Formats.ITALIC]:
            format_italic()
        elif user_input == formats[Formats.LINK]:
            format_link()
        elif user_input == formats[Formats.INLINE_CODE]:
            format_inline_code()
        elif user_input == formats[Formats.HEADER]:
            format_header()
        elif user_input == formats[Formats.ORDERED_LIST]:
            format_ordered_list()
        elif user_input == formats[Formats.UNORDERED_LIST]:
            format_unordered_list()
        elif user_input == formats[Formats.LINE_BREAK]:
            format_line_break()
    else:
        print(prompts[Prompts.UKNOWN_FORMATER])


def save_file():
    file_name = 'result.md'
    with open(file_name, 'w') as f:
        f.write(formatted_text)


def input_handler():
    result = True
    user_input = get_user_input(prompts[Prompts.CHOOSE])
    if user_input == commands[Commands.DONE]:
        save_file()
        result = False
    else:
        input_processor(user_input)
    return result


def main():
    global formatted_text
    keep_going = True
    while keep_going:
        keep_going = input_handler()
        if keep_going:
            print(formatted_text)


main()
