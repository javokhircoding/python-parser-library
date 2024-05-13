import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", help="squares a given number", type=int)
parser.add_argument("-v", "--verbose", help="Shows the squre with full option", action="count", default=0)

arg = parser.parse_args()
answer = arg.square**2

if arg.verbose == 1:
    print("The square of {} is {}".format(arg.square, answer)) #fowmat method is used on simple
elif arg.verbose == 2:                                                    #string like 
    print("{} ** {} = {}".format(arg.square, arg.square, answer))                  # "hello {}".format(name)
else:
    print(answer)

#usage: my6.py squarenum -v(vv...)