import sys


def print_result(count):
    """print result as required"""
    print("The text contains " + str(sum(count)) + " characters:")
    print(str(count[0]) + " upper letters")
    print(str(count[1]) + " lower letters")
    print(str(count[2]) + " punctuation marks")
    print(str(count[3]) + " spaces")
    print(str(count[4]) + " digits")


def parse(argument, count):
    """parser for argument"""
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for x in argument:
        if x.isupper():
            count[0] += 1
        elif x.islower():
            count[1] += 1
        elif x in punctuation:
            count[2] += 1
        elif x.isspace():
            count[3] += 1
        elif x.isdigit():
            count[4] += 1
    print_result(count)


def main():
    """main function"""
    count = [0, 0, 0, 0, 0]
    try:
        assert len(sys.argv) < 3, "AssertionError: more than 1 argument"
    except AssertionError as message:
        print(message)
    else:
        if len(sys.argv) < 2 or sys.argv[1] is None:
            print("What is the text to count?")
            input_string = sys.stdin.readline()
            parse(input_string, count)
        else:
            parse(sys.argv[1], count)


if __name__ == "__main__":
    main()
