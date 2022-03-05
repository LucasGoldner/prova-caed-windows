import joblib
import nltk 
import random
import requests
import json
from string import punctuation

url = "https://significado.herokuapp.com"

def api_json(acao, palavra):
    obj = requests.get(url + "/" + acao + "/" + palavra)
    obj_json = json.loads(obj.text)
    
    return obj_json


def troca_sinonimos(texto):
    # pos tagger treinado em portugues
    tagger = joblib.load("trained_POS_taggers/POS_tagger_brill.pkl")

    # separa o texto em frases
    frases = nltk.tokenize.sent_tokenize(texto, "portuguese")

    frases_alteradas = []

    for frase in frases:
        palavras = nltk.tokenize.word_tokenize(frase, "portuguese")
        tags = tagger.tag(palavras)

        total = 0

        # loop ate substituir algumas palavras da frase ou nao conseguir substituir nenhuma
        while total < len(palavras):
            total += 1
            
            # sorteia uma palavra aleatoria
            numero_aleatorio_palavra = random.randint(0, len(palavras)-1)
            palavra_aleatoria = palavras[numero_aleatorio_palavra]

            # tratar alguns casos
            if len(palavra_aleatoria) > 2 and palavra_aleatoria == palavra_aleatoria.lower():
                if palavra_aleatoria not in punctuation and palavra_aleatoria not in nltk.corpus.stopwords.words("portuguese"):
            
                    tag_palavra_aleatoria = tags[numero_aleatorio_palavra][1]

                    # confere se a tag da palavra eh um verbo(V) ou substantivo(N)
                    if tag_palavra_aleatoria == "V" or tag_palavra_aleatoria == "N":
                        
                        # pega os sinonimos por uma api
                        sinonimos_json = api_json("synonyms", palavra_aleatoria)

                        # se for verbo, troca por um sinonimo
                        if tag_palavra_aleatoria == "V":
                            if len(sinonimos_json) > 0:
                                frase = frase.replace(palavra_aleatoria, sinonimos_json[0])
                                break

                        # se for substantivo, verifica se eles tem o mesmo genero
                        elif tag_palavra_aleatoria == "N":
                            
                            # pega o significado pela api
                            significado_json = api_json("meanings", palavra_aleatoria)

                            if "error" not in significado_json:
                                classe_gramatical = significado_json[0]["class"]

                                for sinonimo in sinonimos_json:
                                    significado_sinonimo_json = api_json("meanings", sinonimo)

                                    classe_gramatical_sinonimo = significado_sinonimo_json[0]["class"]

                                    # verifica se o genero da palavra e dos sinonimo eh o mesmo
                                    if classe_gramatical == classe_gramatical_sinonimo:
                                        frase = frase.replace(palavra_aleatoria, sinonimo)
                                        break
            
        frases_alteradas.append(frase)

    return " ".join(frases_alteradas)
