import argparse

parser = argparse.ArgumentParser(description='Ecrit plusieursfois un emoji')
parser.add_argument('-n', '--fois', type=int, default=5)
emo = "😋"
args = parser.parse_args()
if args.fois < 3:
    print("Marche pas car -n-> top petit")
    exit()
elif args.fois > 15:
    print("Marche pas car -n-> topgrand")
    exit()
for i in range(args.fois):
    print(emo)
