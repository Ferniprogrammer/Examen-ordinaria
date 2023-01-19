import re
import random

def main():
    frases = ["El artista mira hacia arriba. \"Siempre va a tratarse de Tree Fiddy\"",
              "¿Cuál es el precio de una cerveza?",
              "¿Cuánto cuesta una habitación para una noche?",
              "¿Puedo tener una cucharada de azúcar?",
              "¿Qué tal si nos tomamos una cerveza juntos?"]
    nessie = random.choice(frases)
    print("Frase elegida: ", nessie)
    resultado = re.search("tree fiddy|3\.50|three fifty", nessie, re.IGNORECASE)
    if resultado:
        print("Hemos encontrado a nessie")
    else:
        print("No está Nessie")
    main()
