import argparse

parser = argparse.ArgumentParser(description='Ajoute Hellow World a un txt')
parser.add_argument('-f', '--file', type=str)
parser.add_argument('-m', '--message', type=str)
args = parser.parse_args()

fichier=open(args.file, 'a')
fichier.write('\n'+args.message)
fichier.close()
