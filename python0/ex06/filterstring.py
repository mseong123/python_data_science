import ft_filter
import sys


def main():
    """main"""
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the arguments are bad"
        str(sys.argv[1])
        int(sys.argv[2])
    except AssertionError as message:
        print(message)
    except ValueError:
        print("AssertionError: the arguments are bad")
    else:
        a = ft_filter.ft_filter(lambda b:
                                b.isalnum() or b.isspace(), str(sys.argv[1]))
        a = ''.join(a)
        a = a.split()
        a = ft_filter.ft_filter(lambda b:
                                len(b) > int(sys.argv[2]), a)
        print(a)


if __name__ == "__main__":
    main()
