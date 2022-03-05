import nltk
import random
from troca_sinonimos import troca_sinonimos
from troca_genero import troca_genero

# troca algumas palavras por sinonimos, e altera o genero de algumas frases
def troca(texto):
    # troca sinonimos
    texto_alterado = troca_sinonimos(texto)

    frases = nltk.tokenize.sent_tokenize(texto_alterado, "portuguese")

    # troca os generos
    for i in range(0, len(frases)):
        numero_aleatorio = random.randint(1, len(frases))

        if numero_aleatorio == 1:
            frase_alterada = troca_genero(frases[i])

            frases[i] = frase_alterada

    texto_alterado = "".join(frases)

    return texto_alterado