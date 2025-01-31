import sys

def decrypter_fichier_binaire(entree, sortie):
    with open(entree, 'rb') as f_in, open(sortie, 'wb') as f_out:
        contenu = f_in.read()
        resultat = bytearray()
        decalage = 0

        for octet in contenu:
            nouveau_octet = (octet - decalage) % 256  # Assurer que ça reste un octet valide
            resultat.append(nouveau_octet)
            decalage += 1

        f_out.write(resultat)

decrypter_fichier_binaire(sys.argv[1], sys.argv[2])
