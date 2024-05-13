import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")

group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")


parser.add_argument("x", help="The base", type=int)
parser.add_argument("y", help="The exponent", type=int)


arg = parser.parse_args()
answer = arg.x**arg.y

if arg.quiet:
    print(answer)
if arg.verbose:    
    print("{} ^ {} = ".format(arg.x, arg.y), end="")
else:
    print("{} to the power {} equals {}".format(arg.x, arg.y, answer))