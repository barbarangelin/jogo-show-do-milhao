import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def definicao_dos_dados(empresa):
    return yf.download(empresa, start = "2025-05-30", end= "2026-05-30")

def plotar_grafico(nome_da_empresa, moeda, informacoes):
    plt.figure(figsize = (7,3))
    plt.scatter(informacoes.index, informacoes["Close"], alpha=0.5, label="Preco Real")
    plt.plot(informacoes.index, informacoes["Regressao_Linear"], color= "pink", linewidth=4, label="Regressão Linear")
    plt.title(nome_da_empresa+" - Regressão linear com dados de 1 ano")
    plt.xlabel("Data")
    plt.ylabel("Preco das acoes (" + moeda + ")")
    plt.legend()
    plt.grid(True)
    plt.show()



def regressao_linear_para_predicao(nome_da_empresa, moeda):
    dados = definicao_dos_dados(nome_da_empresa)
    dados["Datas"] = np.arange(len(dados))
    eixo_X_dias = dados[["Datas"]]
    eixo_Y_fechamento = dados["Close"]
    modelo_de_regressao = LinearRegression()
    modelo_de_regressao.fit(eixo_X_dias,eixo_Y_fechamento)
    dados["Regressao_Linear"] = modelo_de_regressao.predict(eixo_X_dias)
    plotar_grafico(nome_da_empresa, moeda, dados)

