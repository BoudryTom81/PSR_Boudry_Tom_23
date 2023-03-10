#Serveur
import socket
import argparse

# initialise argparse
parser = argparse.ArgumentParser(description='Serveur')
parser.add_argument('-p', '--port', type=int, default=8112, help='Port')
parser.add_argument('-a', '--ipaddress', type=str, default='localhost' ,help='Addresse IP du serveur')
args = parser.parse_args()

#socket de server et lie addresse ip avec port du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((args.ipaddress, args.port))
server_socket.listen(1)

print('Ecoute du serveur sur le port', args.port)

# Je précise ici le nom
chemin ='C:/Users/tipil/Projet_SCF2/Projet_SCF/login/'
files = {'FB?QVMTI': chemin+'Baki.Hanma.txt', 'MOAF9FV1': chemin+'Michel.Giroud.txt',
         '20I6UCVH': chemin+'Olivia.Bisquet.txt,','1S5Q44S4': chemin+'Françis.Malcolm.txt',
         'DZ9GHHAE': chemin+'Pika.pika.txt','FD522156': chemin+'Patrick.eponge.txt'}

while True:
    # j'attend un client
    client_socket, client_address = server_socket.accept()
    print('Un client se connecte depuis', client_address)

    # je reçois ça cle pour l'identifier (1024 octets pour limité les donné )
    key = client_socket.recv(1024).decode()
    print('Cle reçue :', key)

    # si cle invalide
    if key not in files:
        print('Cle invalide')
        client_socket.send('Cle invalide'.encode())
        client_socket.close()
        #je continue quand meme mais pas le bon fichier et il saura que ça cle est invalide
        continue

    # Envoyer le fichier associé à la clé au client
    filename = files[key]
    #ouvre mon fichier pour le lire en format binaire
    with open(filename, 'rb') as f:
        file_data = f.read()
        client_socket.send(file_data)
        print('Le fichier ->', filename, 'a bien etait envoyer a : ', client_address)

    client_socket.close()
