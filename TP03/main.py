import argparse

parser = argparse.ArgumentParser(description='Ecrit plusieurs fois un emoji')
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

fichier=open(args.file, 'r')
lecture=fichier.read()
print(lecture)
fichier.close
