from analise import analisa
from troca_texto import troca
from chefboost import Chefboost 
from flask import Flask, render_template, request
import nltk

# na primeira execucao, o nltk faz download das suas dependencias
nltk.download("popular")
nltk.download("mac_morpho")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", 
                variavel_texto = "", 
                variavel_classificacao = "",
                variavel_visivel_classifica = "hidden",
                variavel_visivel_troca = "hidden",
                variavel_texto_trocado = "")

    elif request.method == "POST":
        texto = str(request.form.get("texto"))
        botao = str(request.form.get("botao"))
        
        visivel_classifica = visivel_troca = "hidden"
        
        classficacao = texto_trocado = ""

        if texto.strip() != "":
            if botao == "classifica":
                visivel_classifica = "visible"
                
                obj = analisa(texto)
                model = Chefboost.load_model("model.pkl")
                
                classficacao = Chefboost.predict(model, obj)
            
            elif botao == "troca":
                visivel_troca = "visible"

                texto_trocado = troca(texto)
        
        return render_template("index.html", 
                                variavel_texto = texto, 
                                variavel_visivel_classifica = visivel_classifica,
                                variavel_classificacao =  classficacao,
                                variavel_visivel_troca = visivel_troca,
                                variavel_texto_trocado = texto_trocado)


@app.errorhandler(404)
def not_found(e):
  return render_template("index.html")

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("index.html")

    
app.run()
