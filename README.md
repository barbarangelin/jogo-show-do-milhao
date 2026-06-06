## Jogo do Milhão Finances <img alt="python" src="https://img.shields.io/badge/python-red?style=for-the-badge&logo=python&logoColor=white" /> <img alt="pyqt6" src="https://img.shields.io/badge/PyQt6-005C84?style=for-the-badge&logo=pyqt6&logoColor=white" /> <img alt="scikit-learn" src="https://img.shields.io/badge/scikit-pink?style=for-the-badge&logo=scikit&logoColor=white" />  <img alt="y-finances" src="https://img.shields.io/badge/y-finances-yellow?style=for-the-badge&logo=yfinances&logoColor=white" /> <img alt="mit" src="https://img.shields.io/badge/mit-green?style=for-the-badge&logo=mit&logoColor=white" />

### O objetivo desse projeto é estudar a aplicação da regressão linear na área do mercado financeiro através de um jogo eletrônico

## Tabela de conteúdos
- [Concepção do software](#concepção-do-software)
- [Lógica do jogo](#lógica-do-jogo)
- [Como utilizar](#como-utilizar)
  

<img width="1436" height="465" alt="Captura de tela 2026-06-06 120643" src="https://github.com/user-attachments/assets/37eed900-afec-49c6-b2d0-8a5b19a29bca" />

# Concepção do software
O jogo foi pensando para um trabalho acadêmico da disciplina de inteligência computacional. Os requisitos do projeto eram: escolher ações que estivessem em $\color{red}{alta}$, aplicar a $\color{red}{regressão \space linear}$ nos dados extraídos pelo $\color{red}{Yahoo \space Finances}$ e discutir em sala de aula os dados alcançados.

Era permitida a criatividade, então, decidi acoplar os requisitos dentro de um "Jogo do Milhão". Assim, o jogador deve pensar como um analista financeiro para escolher as alternativas corretas e alcançar o prêmio máximo.

# Lógica do jogo
O jogo possui $\color{red}{cinco \space perguntas}$ distintas. Cada uma dela possui um enunciado e alternativas diferentes. Ou seja, nenhuma ação aparece repitida.

Além disso, foi priorizado relacionar ações de âmbitos similares. Por exemplo, na primeira pergunta ambas as ações são de empresas de produtos de beleza.

<img width="1447" height="465" alt="image" src="https://github.com/user-attachments/assets/5bc2f750-b4a9-40c3-8039-e3d2a79f6b19" />


E, da mesma forma que o Show do Milhão original, há 3 possibilidades: a possibilidade de errar, de parar ou de acertar.
- Errar: o jogador perde metade do que conquistou.
- Parar: o jogador nem ganha e nem perde o que conquistou.
- Acertar: o jogador ganha um acréscimo no que já conquistou, verifica o gabarito da questão e acessa a próxima pergunta.

Na verificação do gabarito é onde exatamente foi aplicado a regressão linear com o $\color{red}{scikit-learn}$. Assim, no gabarito é exposto um gráfico **tempo X valor da ação**. O eixo do tempo abrange um perído de um ano (maio/2025 - maio/2026) e o eixo do valor da ação é mostrado com a sinalização da moeda (exemplo: euro). Outrossim, a linha rosa dos gráficos representa a predição pela regressão linear, enquanto os pontos azuis representam os valores reais.

<img width="1752" height="459" alt="Captura de tela 2026-06-06 173610" src="https://github.com/user-attachments/assets/91afb476-978d-457c-90dd-2751fc81b3b0" />

A cada pergunta respondida corretamente o jogador avança no jogo e fica mais perto da pergunta de um milhão de reais.

# Como utilizar
Baixe o repositório e abra a pasta em seu editor de código predileto. Mas tenha certeza de ter todas as bibliotecas instaladas previamente em sua máquina.
