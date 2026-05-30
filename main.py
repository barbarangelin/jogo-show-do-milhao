from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
from PyQt6 import QtWidgets,uic
import finances
import sys

premio = 0

def mostrar_resposta(nome_da_empresa, moeda):
    finances.regressao_linear_para_predicao(nome_da_empresa, moeda)

def resetarPremio():
    global premio
    premio = 0

def incrementarPremio(incremento):
    global premio
    premio += incremento

def decrementarPremio():
    global premio
    premio /= 2

def alternarInterface(interface_atual, proxima_interface):
    interface_atual.close()
    proxima_interface()

def efeito_sonoro_show_do_milhao(tipo_de_efeito, loop):
    global efeito_sonoro
    efeito_sonoro = QSoundEffect()
    efeito_sonoro.setSource(QUrl.fromLocalFile("./efeitosSonoros/"+tipo_de_efeito+".wav"))
    if loop == True:
        efeito_sonoro.setLoopCount(-2)
    efeito_sonoro.setVolume(1.0)
    efeito_sonoro.play()

def maiorPontuacaoInterface():
    mostrar_resposta("TSM", "USD")
    mostrar_resposta("POSI3.SA", "BRL")
    incrementarPremio(500000)
    efeito_sonoro_show_do_milhao("palmas_vencedor", False)
    global maiorPontuacao
    maiorPontuacao = uic.loadUi("maior pontuacao.ui")
    maiorPontuacao.show()
    maiorPontuacao.premiacao.setText("R$"+str(premio))
    maiorPontuacao.botaoInicio.clicked.connect(lambda: alternarInterface(maiorPontuacao, paginaHomeInterface))


def premiacaoFinalInterface():
    efeito_sonoro_show_do_milhao("palmas", False)
    global premiacaoFinal 
    premiacaoFinal = uic.loadUi("premiacao final.ui")
    premiacaoFinal.show()
    premiacaoFinal.premiacao.setText("R$"+str(premio))
    premiacaoFinal.botaoInicio.clicked.connect(lambda: alternarInterface(premiacaoFinal, paginaHomeInterface))

def respostaErrada(interface_atual):
    decrementarPremio()
    alternarInterface(interface_atual, premiacaoFinalInterface)

def quintaPerguntaInterface():
    mostrar_resposta("INTB3.SA", "BRL")
    mostrar_resposta("AMZN", "USD")
    efeito_sonoro_show_do_milhao("pergunta_de_um_milhao",False)
    incrementarPremio(300000)
    global quintaPergunta
    quintaPergunta = uic.loadUi("quinta pergunta.ui")
    quintaPergunta.show()  
    quintaPergunta.opcaoUm.clicked.connect(lambda: alternarInterface(quintaPergunta,maiorPontuacaoInterface))
    quintaPergunta.opcaoDois.clicked.connect(lambda: respostaErrada(quintaPergunta))
    quintaPergunta.botaoParar.clicked.connect(lambda: alternarInterface(quintaPergunta,premiacaoFinalInterface)) 

def quartaPerguntaInterface():
    mostrar_resposta("VALE3.SA", "BRL")
    mostrar_resposta("OIBR3.SA", "BRL")
    efeito_sonoro_show_do_milhao("certa-resposta", False)
    incrementarPremio(150000)
    global quartaPergunta
    quartaPergunta = uic.loadUi("quarta pergunta.ui")
    quartaPergunta.show()
    quartaPergunta.opcaoUm.clicked.connect(lambda: respostaErrada(quartaPergunta))
    quartaPergunta.opcaoDois.clicked.connect(lambda: alternarInterface(quartaPergunta,quintaPerguntaInterface))
    quartaPergunta.botaoParar.clicked.connect(lambda: alternarInterface(quartaPergunta,premiacaoFinalInterface))

def terceiraPerguntaInterface():
    mostrar_resposta("BYDDF", "USD")
    mostrar_resposta("TSLA", "USD")
    efeito_sonoro_show_do_milhao("certa-resposta",False)
    incrementarPremio(40000)
    global terceiraPergunta
    terceiraPergunta = uic.loadUi("terceira pergunta.ui")
    terceiraPergunta.show()
    terceiraPergunta.opcaoUm.clicked.connect(lambda: respostaErrada(terceiraPergunta))
    terceiraPergunta.opcaoDois.clicked.connect(lambda: alternarInterface(terceiraPergunta,quartaPerguntaInterface))
    terceiraPergunta.botaoParar.clicked.connect(lambda: alternarInterface(terceiraPergunta,premiacaoFinalInterface))

def segundaPerguntaInterface():
    mostrar_resposta("ELF", "USD")
    mostrar_resposta("POSI3.SA", "EUR")
    efeito_sonoro_show_do_milhao("certa-resposta",False)
    incrementarPremio(10000)
    global segundaPergunta
    segundaPergunta = uic.loadUi("segunda pergunta.ui")
    segundaPergunta.show()
    segundaPergunta.opcaoUm.clicked.connect(lambda: alternarInterface(segundaPergunta,terceiraPerguntaInterface))
    segundaPergunta.opcaoDois.clicked.connect(lambda: respostaErrada(segundaPergunta))
    segundaPergunta.botaoParar.clicked.connect(lambda: alternarInterface(segundaPergunta,premiacaoFinalInterface))

def primeiraPerguntaInterface ():
    efeito_sonoro_show_do_milhao("nova_pergunta", False)
    global primeiraPergunta
    primeiraPergunta = uic.loadUi("primeira pergunta.ui")
    primeiraPergunta.show()
    primeiraPergunta.opcaoUm.clicked.connect(lambda: respostaErrada(primeiraPergunta))
    primeiraPergunta.opcaoDois.clicked.connect(lambda: alternarInterface(primeiraPergunta,segundaPerguntaInterface))
    primeiraPergunta.botaoParar.clicked.connect(lambda: alternarInterface(primeiraPergunta,premiacaoFinalInterface))


def paginaHomeInterface ():
    resetarPremio()
    global paginaHome
    paginaHome = uic.loadUi("home.ui")
    paginaHome.show()
    efeito_sonoro_show_do_milhao("tema_de_abertura",True)
    paginaHome.botaoJogar.clicked.connect(lambda: alternarInterface(paginaHome,primeiraPerguntaInterface))


def incicialzação():
    aplicação = QtWidgets.QApplication(sys.argv)
    paginaHomeInterface()
    aplicação.exec()

incicialzação()