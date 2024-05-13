import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbo", help='I dunno it is verbo', 
                    action="store_true")
a = parser.parse_args()
if a.verbo:
    print("it worked!")