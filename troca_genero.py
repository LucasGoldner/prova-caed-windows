import joblib
import nltk 
from string import punctuation

# nao troca palavras em plural
def eh_plural(palavra):
    return palavra.endswith("s")

# algumas excecoes de adjtivos terminados em or
def eh_excecao(palavra):
    return palavra in ["maior", "menor", "melhor", "pior", "superior", "inferiro", "anterior", "posterior"]

# troca do feminino para o masculino
def troca_adjetivo_feminino(palavra):
    if eh_excecao(palavra):
        return palavra    

    elif palavra.endswith("eia"):
        return palavra[0: -3] + "eu"
    
    elif palavra.endswith("oa"):
        return palavra[0: -2] + "éu"

    elif palavra.endswith("ã"):
        return palavra[0: -1] + "ão"

    elif palavra.endswith("ona"):
        return palavra[0: -3] + "ão"

    elif palavra.endswith("oa"):
        return palavra[0: -2] + "ão"

    elif palavra.endswith("êsa") or palavra.endswith("ora") or palavra.endswith("u"):
        return palavra[0: -1]

    elif palavra.endswith("a"):
        return palavra[0: -1] + "o"
    
    else:
        return palavra

# troca do masculino para o feminino
def troca_adjetivo_masculino(palavra):
    if eh_excecao(palavra):
        return palavra

    elif palavra.endswith("ês") or palavra.endswith("or") or palavra.endswith("u"):
        return palavra + "a"

    elif palavra.endswith("ão"):
        return palavra[0: -2] + "ona"

    elif palavra.endswith("eu"):    
        return palavra[0: -2] + "eia"
    
    elif palavra.endswith("éu"): 
        return palavra[0: -2] + "oa" 

    elif palavra.endswith("o"):
        return palavra[0: -1] + "a"
    
    else:
        return palavra

def troca_adjetivos(palavra):
    troca = troca_adjetivo_masculino(palavra)

    if palavra == troca:
        return troca_adjetivo_feminino(palavra)
    
    else:
        return troca

# algumas excecoes dos substantivos
def eh_substantivo_uniforme(palavra):
    comum = ["estudante","imigrante","acrobata","agente","intérprete","lojista","mártir","viajante","aspirante","atleta","camelô","chofer","fã","gerente","médium","porta-voz","protagonista","puxa-saco","sem-terra","sem-vergonha","xereta","xerife"]
    sobrecomum = ["área", "cônjuge","criança","carrasco","indivíduo","apóstolo","monstro","pessoa","testemunha","algoz","verdugo","vítima","tipo","animal","bóia-fria","cadáver","criatura","dedo-duro","defunto","gênio","ídolo","líder","membro","nó-cego","pão-duro", "comida", "estudo"]
    epiceno = ["girafa","andorinha","águia","barata","cobra","jacaré","onça","sabiá","tatu","anta","arara","borboleta","canguru","caranguejo","coruja","crocodilo","escorpião","formiga","girafa","mosca","onça","pantera","pernilongo","piolho"]

    return palavra in [comum + sobrecomum + epiceno]

# alguns substantivos que tem a flexao diferente
def eh_substantivo_biforme(palavra):
    biforme = {"masculino":"feminino","bode":"cabra","boi":"vaca","cão":"cadela","carneiro":"ovelha","cavaleiro":"amazona","cavalheiro":"dama","cavalo":"égua","frade":"freira","frei":"sóror","genro":"nora","homem":"mulher","padastro":"madrasta","padre":"madre","veado":"cerva","zangão":"abelha","pai":"mãe", "avô":"avó","reú":"ré","grou":"grua","poeta":"poetisa","profeta":"profetisa","diácono":"diaconisa","abade":"abadessa","conde":"condessa","visconde":"viscondessa","embaixador":"embaixatriz","imperador":"imperatiriz","ator":"atriz","pavão":"pavoa","melão":"meloa","patrão":"patroa","cidadão":"cidadã","campeão":"campeã","anão":"anã","são":"sã"}

    if palavra in biforme.keys():
        return biforme[palavra]
    
    elif palavra in biforme.values():
        for chave in biforme.keys():
            if palavra == biforme[chave]:
                return chave

    else:
        return palavra

# troca os substantivos, usa as mesmas regras dos adjetivos
def troca_substantivos(palavra):
    if eh_substantivo_uniforme(palavra):
        return palavra

    else:
        troca = eh_substantivo_biforme(palavra)
        
        if palavra == troca:
            return troca_adjetivos(palavra)

        else:
            return troca

# troca artigos
def troca_artigos(palavra):
    if palavra == "o":
        return "a"
    
    elif palavra == "a":
        return "o"

    elif palavra.endswith("um"):
        return palavra + "a"

    elif palavra.endswith("uma"):
        return palavra[0: -1]


def troca_outras_palavras(palavra):
    if palavra == "ela":
        return "ele"
    
    elif palavra == "ele":
        return "ela"

    elif palavra == "na":
        return "no"
    
    elif palavra == "no":
        return "na"

    elif palavra == "da":
        return "do"
    
    elif palavra == "do":
        return "da"
    
    else:
        return palavra

# troca o genero das palavras de uma frase
def troca_genero(frase):
    # pos tagger treinado em portugues
    tagger = joblib.load("trained_POS_taggers/POS_tagger_brill.pkl")
    
    # separa a frase em palavras
    palavras = nltk.tokenize.word_tokenize(frase, "portuguese")
    tags = tagger.tag(palavras)

    frase_trocada = []

    # percorre toda a frase, trocando os generos dos artigos, substantivos e adjetivos
    for tag in tags:
        palavra = str(tag[0].lower())

        if palavra not in punctuation and not(eh_plural(palavra)):
            if tag[1] == "ART":
                palavra = troca_artigos(palavra)
            
            elif tag[1] == "N":
                palavra = troca_substantivos(palavra)
            
            elif tag[1] == "ADJ":
                palavra = troca_adjetivos(palavra)

        palavra = troca_outras_palavras(palavra)

        frase_trocada.append(palavra)

    return " ".join(frase_trocada)

