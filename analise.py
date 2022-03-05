import re
import nltk
import joblib

# verifica se a palavra eh canonica
def eh_canonica(palavra):
    vogais = ["a", "á", "à", "ã", "â", "e", "é", "ê", "i", "í", "o", "ó", "õ", "ô", "u", "ú"]

    if len(palavra) % 2 == 0:
        for i in range(0, len(palavra), 2):
            if not (palavra[i] not in vogais and palavra[i+1] in vogais):
                return False
            return True    
    return False

# remove do texto os sinais de pontuacao e stopwords
def pre_processamento(texto):
    # deixa o texto todo em minusculo e remove a pontuacao 
    texto_letras_minusculas = re.findall(r"\b[A-zÀ-úü]+\b", texto.lower())

    # usa as stopwords do nltk
    stopwords = nltk.corpus.stopwords.words("portuguese")

    # remove os stopwords
    sem_stopwords = [letra for letra in texto_letras_minusculas if letra not in stopwords]
    
    return " ".join(sem_stopwords)


# analiza o texto, guardando algumas informacoes como: 
# porcentagem de verbos, substantivos, palavras canonicas, palavras diferentes, palavras por frases
def analisa(texto):
    # guarda a quantidade de frases antes do pre porcessamento, pelo nltk
    quantidade_frases = len(nltk.tokenize.sent_tokenize(texto, "portuguese"))

    texto = pre_processamento(texto)

    # quebra o texto em palavras, pelo ntlk
    palavras = nltk.tokenize.word_tokenize(texto, "portuguese")

    # pos tagger treinado em portugues
    tagger = joblib.load("trained_POS_taggers/POS_tagger_brill.pkl")
    tags = tagger.tag(palavras)
    
    verbos = 0.0
    substantivos = 0.0
    canonicas = 0.0

    # tag[0] eh a palavra, tag[1] eh a classe gramatical (tag)
    for tag in tags:
        if tag[1] == "V":
            verbos += 1
        if tag[1] == "N":
            substantivos += 1
        if eh_canonica(tag[0]):
            canonicas += 1

    # guardas os valores da porcentagens
    verbos =  verbos * 100 / len(palavras)
    substantivos = substantivos * 100 / len(palavras)
    canonicas = canonicas * 100 / len(palavras)
    palavra_frase = len(palavras) / quantidade_frases

    frequencia = nltk.probability.FreqDist(palavras)
    palavras_diferentes = (100 * len(frequencia) / len(palavras))

    return [verbos, substantivos, canonicas, palavras_diferentes, palavra_frase]
