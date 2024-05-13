from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square', help='Squeares a given number', type = int)
parser.add_argument('-v', '--verbose', help='Provides a verbose desc', action = 'store_true')
''' yuqorida qanqadir bir balo yaratdi brat kegin uni shartladi xuysnim hech baloga chunmadm 
oylaab ko`rsam bunaqa qilib ishlatsa bolarkan: python3 main.py -v 10
javobi: 10 squeared is : 100 '''



args: Namespace = parser.parse_args()


if args.verbose:
    print(f'{args.square} squared is : {args.square**2}')
else:
    print(args.square**2)


