import argparse

parser = argparse.ArgumentParser()

parser.add_argument("x", help="The base", type=int)
parser.add_argument("y", help="The exponent", type=int)
parser.add_argument("-v", "--verbose", help="Shows the squre with full option", action="count")

arg = parser.parse_args()
answer = arg.x**arg.y

if arg.verbose == 1:
    print("{} tp the power {} equals {}".format(arg.x, arg.y, answer)) #fowmat method is used on simple
elif arg.verbose == 2:                                                    #string like 
    print("{} ** {} = {}".format(arg.x, arg.y, answer))                  # "hello {}".format(name)
else:
    print(answer)

#usage: my6.py x y -v(vv...)