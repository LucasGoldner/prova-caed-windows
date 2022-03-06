# Resolução da Prova - Fundação CAEd 
## Versão Windows - Instruções para a execução


Abrir o terminal (ps ou cmd) e seguir os seguintes passos:

Fazer o git clone do repositório:

    git clone https://github.com/LucasGoldner/prova-caed-linux

Dentro da pasta *"prova-caed-windows"*, ativar o ambiente virtual:
 
    .\venv\Scripts\Activate.ps1 (no powershell)
    .\venv\Scripts\activate.bat (no cmd)

Talvez seja necessário executar o seguinte comando no powershell (admin):

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Com o ambiente virtual ativado, executar o comando:
  
    python app.py

Acessar o seguinte endereço: 

    http://127.0.0.1:5000/

Para encerrar a execução:

    (ctrl+c para sair)
    
    deactivate                    (no powershell)
    .\venv\Scripts\deactivate.bat (no cmd)

O primeiro comando encerra a execução, o segundo desativa o ambiente virtual.
    
## Relatório

O relatório detalhando o processo de desenvolvimento: 
[relatório-prova-prática](https://docs.google.com/document/d/1j3nS6w3SwsXBgtOjVmHf9iBw4D1BGw0NzjQl9GTVer4/edit?usp=sharing)
