import sys

# Vérifier que 2 arguments sont bien fournis
if len(sys.argv) != 3:
    print("Erreur : Deux arguments sont nécessaires.")
    sys.exit(1)

# Essayer de convertir les arguments en nombres
try:
    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])
except ValueError:
    print("Erreur : Les arguments doivent être des nombres.")
    sys.exit(1)

# Calculer la somme
resultat = arg1 + arg2

# Afficher le résultat
print(f"Le résultat est : {resultat}")
