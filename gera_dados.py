import os
from analise import analisa

diretorio = "dataset_caed"

arquivo_csv = open("dados.csv", "w")
arquivo_csv.write("Verbos,Substantivos,Canonicas,Diferentes,Palavras_Frase,Decision\n")

for sub_diretorio in os.listdir(diretorio):
    for txt in os.listdir(diretorio + "/" + sub_diretorio):
        caminho = diretorio + "/" + sub_diretorio + "/" + txt

        arquivo = open(caminho)
        texto = arquivo.read()
        
        obj = analisa(texto)
        
        linha = str(obj[0])+","+str(obj[1])+","+str(obj[2])+","+str(obj[3])+","+str(obj[4])+","+sub_diretorio+"\n"
        arquivo_csv.write(linha)

        arquivo.close()    

arquivo_csv.close()