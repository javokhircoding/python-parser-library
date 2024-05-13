import argparse

parser = argparse.ArgumentParser()

parser.add_argument("x", help="The base", type=int)
parser.add_argument("y", help="The exponent", type=int)
parser.add_argument("-v", "--verbose", help="Shows the squre with full option", action="count")

arg = parser.parse_args()
answer = arg.x**arg.y

if arg.verbose >= 2:
    print("Running '{}'".format(__file__)) #fowmat method is used on simple
if arg.verbose >= 1:                                                    #string like 
    print("{} ^ {} = ".format(arg.x, arg.y), end="")               # "hello {}".format(name)
print(answer)


#usage: my6.py x y -v(vv...)