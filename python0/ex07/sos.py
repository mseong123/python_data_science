import sys


def main():
    """main"""
    errMessage = "AssertionError: the arguments are bad"
    NESTED_MORSE = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
        'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
        'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
        'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ',
        '2': '..--- ', '3': '...-- ', '4': '....- ', '5':
        '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ', ' ': '/ '
        }
    result = ''
    try:
        assert len(sys.argv) == 2, errMessage
        for c in sys.argv[1]:
            assert c.isalnum() or c == " ", errMessage
    except AssertionError as message:
        print(message)
    else:
        for x in sys.argv[1]:
            result = NESTED_MORSE[x.upper()] + result
        print(result.strip())


if __name__ == "__main__":
    main()
