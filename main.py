import pandas as pd
from graphics import *
from openAiAPI import *


dados = pd.read_csv('/content/feedbacks.csv', delimiter=';')

class Feedback:
  def __init__(self, nota, comentario):
    self.nota = nota
    self.comentario = comentario

class AnalisadorFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calcular_nps(self):
    detratores = sum(1 for feedback in self.feedbacks if feedback.nota <= 6)
    promotores = sum(1 for feedback in self.feedbacks if feedback.nota >= 9)

    return (promotores - detratores) / len(self.feedbacks) * 100

feedbacks = dados.apply(lambda linha: Feedback(linha['nota'], linha['comentario']), axis=1)

# Função para calcular o NPS
analisador = AnalisadorFeedback(feedbacks)
nps = analisador.calcular_nps()
print(nps)

# Função para criar o grafico
criar_grafico_nps(nps)

# Função para fazer o requeste para API
insigths = analisar_sentimentos(feedbacks)
print(insigths)
