import sys
import getopt

#Listess des arguments de commandes passé au script
def main(argv):
    # Tous none sauf num car au cas ou il n'a pas de valeurs il faudrait quand méme qu'il écrive
    file = None
    message = None
    end = None
    num = 1

#Utiliser une fonction d'un ancien projet mais il ne fonctionnet pas sans des variables mancantes donc j'ai demandé a chat gpt de les changé et voila
    try:
        opts, args = getopt.getopt(argv, "hf:m:e:n:", ["file=", "message=", "end=", "num="])
    except getopt.GetoptError:
        print("Usage: python script.py -f <file> -m <message> -e <end> [-n <num>]")
        sys.exit(2)

# la meme boucle for que pour votre example
    for opt, arg in opts:
        # Parcque qu au début je connaissais pas les arguments donc c'es plus facile avec ça
        if opt == "-h":
            print("Ex: python script.py -f <file> -m <message> -e <end> -n <num>")
            sys.exit()

        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("-m", "--message"):
            message = arg
        elif opt in ("-e", "--end"):
            end = arg
        elif opt in ("-n", "--num"):
            num = int(arg)
# car je comprenais pas du tout et en plus c'es chatGPT qui la conseiller donc je vefifie qu'ils est une valeur non null
    if file is None or message is None or end is None:
        print("EXX: python script.py -f <file> -m <message> -e <end> -n <num>")
        sys.exit(2)
#Je l'ai repris de votre cours
    with open(file, "a") as f:
        for i in range(num):
            f.write(f"{message}\n")
        f.write(f"\n{end}")
#Puis j'appelle ma fonction de cette maniere comme le projet INFACO
if __name__ == "__main__":
    main(sys.argv[1:])
