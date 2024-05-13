import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", help="squares a given number", type=int)
parser.add_argument("-v", "--verbose", help="Shows the squre with full option", action="store_true")

arg = parser.parse_args()
answer = arg.square**2

if arg.verbose:
    print("The square of {} is {}".format(arg.square, answer)) #fowmat method is used on simple string like 
else:                                                         # "hello {}".format(name)
    print(answer)