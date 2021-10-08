#!usr/bin/python 

import sys
import re

# écrire régles à respecter pour un commit propre

if __name__ == "__main__":
    main()

def main():
    with open(sys.argv[1], "r") as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines): # Fin du message si :
    if line.strip() == "# ------------------------ >8 ------------------------
        break
    if line[0] == "#": # A chaque # -> retour chariot 
        continue 
    if not line_valid(idx, line):
        show_rules()
        sys.exit(1)
    syst.exit(0)
    
def line_valid(idx, line): # Méthode pour vérifier les lignes, récupère le nombre de lignes et la ligne actuelle, retourne booléen si ligne suivante dispo ou pas. 
    if idx == 0:
        return re.match("^[A-Z].{,48}[0-9A-z \t]$", line)
       elif idx == 1:
        return len(line.strip()) == 0
       else :
        return len(line.stip()) <= 72
        
def show_rules():
    print(rules)
    
   