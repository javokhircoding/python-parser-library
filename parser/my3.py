import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--verbo", help='I dunno it is verbo', type=int)
a = parser.parse_args()
if a.verbo:
    print("it worked!")