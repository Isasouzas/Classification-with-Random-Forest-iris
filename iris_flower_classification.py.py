# -*- coding: utf-8 -*-
"""iris-flower-classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QMcUw7Vd1IyzTteoO2PDUoSpTZ6kuJ8t

Desafio: Utilizar algoritmos de aprendizado supervisionado para classificação dos tipos de flores, conforme dataset que contém 3 tipos de rótulos existentes (flor setosa, versicolor e virginica )


**1- Importação das bibliotecas**

Primeiro passo foi importar bibliotecas conforme modelo de Classificação escolhido para resolução do Desafio.

O Random Forest foi escolhido pois é um modelo de aprendizado de máquina baseado em árvores de decisão que funciona bem em problemas com muitas variáveis e em datasets pequenos e médios, como o dataset Iris. Ele pode lidar com dados ruidosos e é menos propenso ao overfitting, o que garante boa generalização.
"""

# Bibliotecas para manipulação de dados
import pandas as pd
import numpy as np

#  Bibliotecas para visualização de dados
import seaborn as sns
import matplotlib.pyplot as plt

#  Bibliotecas de Machine Learning (sklearn)
from sklearn.model_selection import train_test_split  # Para dividir os dados em treino e teste
from sklearn.ensemble import RandomForestClassifier   # Algoritmo escolhido para classificação
from sklearn.metrics import classification_report, confusion_matrix  # Métricas de avaliação do modelo

# Carreguei o dataset Iris diretamente da biblioteca seaborn, que já disponibiliza esse conjunto de dados em formato de DataFrame.

df = sns.load_dataset('iris')

"""**2- Análise Exploratória (EDA)/Entendimento dos dados**"""

# Para realizar a Análise Exploratória dos Dados (EDA), utilizei os comandos .head() e .info()
# com o objetivo de verificar os tipos das variáveis, a presença de valores nulos ou inconsistentes
# e entender a estrutura geral do DataFrame.


df.head()

# Como podemos observar abaixo, o dataset já está "limpo": os tipos de dados estão corretos
# e não há valores nulos ou inconsistentes, o que facilita o pré-processamento.

df.info()

# Também é importante observar as colunas do conjunto de dados:
# Temos o comprimento e a largura das sépalas e pétalas, que são características morfológicas relevantes
# para a classificação das espécies. Essas serão nossas variáveis preditoras (features).
# Além disso, todas as variáveis de entrada são numéricas, o que dispensa a aplicação de técnicas
# de codificação (encoding) para este caso.

# Para melhor entendimento dos valores das features, realizei a plotagem para entender as dimensões dos dados existentes:

df.plot()

# Uma visualização bastante útil é o Pairplot, que mostra a distribuição das variáveis numéricas
# e suas relações para cada classe da variável alvo ('species').
# É possível perceber graficamente que a espécie Setosa se diferencia com mais clareza das demais,
# especialmente pelo menor tamanho das pétalas, o que facilita sua separação no processo de classificação.
# Já as espécies Versicolor e Virginica apresentam características mais semelhantes entre si,
# o que pode representar um desafio maior para o modelo.

sns.pairplot(df, hue='species')
plt.suptitle('Distribuição das Espécies', y=1.05)
plt.show()

# A coluna "species" é nossa variável alvo, ou "target", que contém os rótulos de classificação das flores.
# Ela será usada para ensinar ao algoritmo supervisionado qual a classificação correta de cada amostra.
# Ou seja, o modelo irá aprender a associar as características (features) das flores ao seu respectivo tipo de flor.

df['species'].value_counts()  # Verificando a distribuição das espécies no dataset
df['species']  # Exibindo a coluna 'species' com os rótulos das flores

# Como podemos observar, cada tipo de flor tem exatamente 50 amostras, o que garante um equilíbrio
# entre as classes, facilitando o treinamento do modelo.

"""**3-Separação: variáveis preditoras e alvo/Treino e Teste**"""

# Separando variáveis preditoras e alvo
# Nesta etapa, separamos as colunas que serão utilizadas como entrada (X) daquela que queremos prever (y), que é a espécie da flor.

X = df.drop(['species'], axis = 1) # X são as features
y = df['species'] # y Definição do target


# Após a separação entre features (X) e target (y), é necessário dividir os dados em conjuntos de treino e teste.
# Defini o parâmetro test_size como 0.2, ou seja, 20% dos dados serão usados para teste e avaliação do modelo.
# Os 80% restantes serão utilizados para o treinamento, permitindo que o modelo aprenda os padrões antes da validação.

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 99)

# "Utilizei o parâmetro random_state para fixar a aleatoriedade da divisão entre treino e teste, garantindo que os resultados sejam reproduzíveis, o que é uma boa prática em experimentos com Machine Learning

"""**4- Treinamento do modelo**"""

# Treinando modelo de classificação


model = RandomForestClassifier(random_state = 99)
model.fit(X_train,y_train)

"""**5- Avaliação do modelo**"""

# Avaliação do modelo

# Avaliação do modelo: após treinar o modelo com os dados de treino, realizei a previsão no conjunto de teste.
# A seguir, são apresentadas as métricas de avaliação do modelo: Relatório de Classificação e Matriz de Confusão.

y_pred = model.predict(X_test)

print("\n Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# O Relatório de Classificação nos fornece três métricas principais para cada classe (espécie):
# - Precision: A precisão indica a taxa de acerto do modelo em relação às previsões positivas. Quanto maior, melhor o modelo acerta ao prever uma classe.
# - Recall: O recall indica a taxa de acerto do modelo para identificar todas as instâncias de uma classe específica.
# - F1-Score: A média harmônica entre precisão e recall, útil quando há um desbalanceamento nas classes.
# O "accuracy" representa a acurácia geral do modelo, enquanto o "macro avg" e "weighted avg" mostram a média das métricas de todas as classes.

print('\n Matriz de Confusão')

print(confusion_matrix(y_test,y_pred))


# A Matriz de Confusão é uma ferramenta importante para analisar o desempenho do modelo. Ela mostra os acertos e erros
# de classificação para cada classe. As linhas representam as classes reais (observadas), enquanto as colunas
# representam as classes previstas. Por exemplo, o modelo classificou corretamente todas as amostras de 'setosa',
# mas cometeu um pequeno erro na classificação de 'versicolor' e 'virginica'.