import argparse

parser = argparse.ArgumentParser(description='Écrire un script Python pour lire un fichier ligne par ligne et imprimer chaque ligne avec un préfixe de numéro de ligne.')
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

try:
    fichier=open(args.file, 'r')
    nigne = 1
    for ligne in fichier:
        print(f"{nigne}: {ligne}", end='')
        nigne += 1
    fichier.close()
except FileNotFoundError:
    print('mauvais fichier')
