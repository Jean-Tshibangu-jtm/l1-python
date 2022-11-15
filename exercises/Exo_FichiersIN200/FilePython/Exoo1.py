#Ouvrir le fichier en écrire 
import os

fichier1 = open("test2" , "w")

#Écrire dans un fichier
# buffer : La mémoire tampon, salle d'attente
fichier1.write("Bonjour Jean")

fichier1.close()