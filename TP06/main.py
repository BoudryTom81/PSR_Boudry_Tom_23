import argparse

parser = argparse.ArgumentParser(description='Écrire un script Python pour lire un fichier et créer un nouveau fichier qui ne contient que les lignes du fichier original qui ne contiennent pas une chaîne de caractères spécifique. ')
parser.add_argument('-f', '--file', type=str)
parser.add_argument('-c', '--chaine', type=str)
args = parser.parse_args()

try:
    with open(args.file, 'r') as Original:
        with open('Pas_Original.txt', 'w') as Nouv:
            for ligne in Original:
                if args.chaine not in ligne:
                    Nouv.write(ligne)
except FileNotFoundError:
    print('mauvais fichier')
