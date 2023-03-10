#client
import socket
import argparse

# initialise argparse
parser = argparse.ArgumentParser(description='Client')
parser.add_argument('-p', '--port', type=int, default=8112, help='numero de port à se connecter')
parser.add_argument('-k', '--key', required=True, help='cle pour etre identifier')
parser.add_argument('-a', '--ipaddress', type=str, default='localhost' ,help='Addresse IP du serveur')
parser.add_argument('-l', '--login', type=str, help='nom du login souhaiter')
args = parser.parse_args()

#socket client et connection au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((args.ipaddress, args.port))

# Envoyer la clé d'identification au serveur
client_socket.send(args.key.encode())

# Recevoir les données du fichier du serveur(limite a 1024 octet)
file_data = client_socket.recv(1024)

# si cle invalide
if file_data == 'cle invalide'.encode():
    print('Clé invalide')
#sinon
else:
    # sauvegarde
    filename = args.login + '.txt'
    #ouvre mon fichier pour le lire en format binaire
    with open(filename, 'wb') as f:
        f.write(file_data)
        print('Fichier', filename, 'enregistré dans C:/Users/tipil/Projet_SCF2')

client_socket.close()
