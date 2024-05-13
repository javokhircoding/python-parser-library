import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help='echo the string you use here')
args = parser.parse_args()
print(args.echo)


#It's a echo parser, usage: python3 my.py something, output: something