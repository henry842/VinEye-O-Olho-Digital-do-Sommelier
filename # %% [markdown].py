# %% [markdown]
# # **MÓDULO 32 - Exercício**
# # Random Forest
# 

# %% [markdown]
# Nesta tarefa, vocês vão trabalhar com uma base de dados de avaliações de vinhos, onde o objetivo é prever a pontuação dos vinhos usando o algoritmo de Random Forest para classificação multiclasse.

# %%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("winequality-red.csv", delimiter=',')

df.head(10)

# %% [markdown]
# **Vamos conhecer nossa base:**
# 
# Características dos Vinhos (Features)
# 
# Fixed Acidity: Acidez fixa do vinho.
# 
# Volatile Acidity: Acidez volátil do vinho.
# 
# Citric Acid: Quantidade de ácido cítrico no vinho.
# 
# Residual Sugar: Açúcar residual presente no vinho.
# 
# Chlorides: Nível de cloretos no vinho.
# 
# Free Sulfur Dioxide: Dióxido de enxofre livre no vinho.
# 
# Total Sulfur Dioxide: Quantidade total de dióxido de enxofre no vinho.
# 
# Density: Densidade do vinho.
# 
# pH: Nível de pH do vinho.
# 
# Sulphates: Quantidade de sulfatos no vinho.
# 
# Alcohol: Teor alcoólico do vinho.
# 
# 
# 
# **Variável de Saída (Target):**
# 
# Quality: Pontuação do vinho baseada em dados sensoriais, variando de 0 a 10.
# 

# %% [markdown]
# Esta abordagem permitirá que vocês explorem como diferentes características químicas influenciam a qualidade dos vinhos e como o Random Forest pode ser usado para fazer previsões precisas com base nesses dados.

# %% [markdown]
# # 1 - Realize a primeira etapa de pré processamento dos dados.
# 
# A) Verifique os tipos de dados.
# 
# 
# B) Verifique os dados faltantes, se houver dados faltantes faça a substituição ou remoção justificando sua escolha.

# %%
#seu código aqui

# %% [markdown]
# # 2 - Realize a segunda e terceita etapa de pré processamento dos dados.
# 
# A) Utilize a função describe para identificarmos outliers e verificarmos a distribuição dos dados.
# 
# B) Verifique o balanceamento da váriavel Target.
# 
# C)  Plote o gráfico ou a tabela e indique as variáveis que te parecem mais "fortes" na correlação para nosso modelo.
# 
# D) Crie um novo dataframe apenas com as váriaveis que parecem ter maior correlação com a target. (Negativa ou positiva)
# 

# %%
#seu código aqui

# %% [markdown]
# # 3 - Preparação Final dos Dados
# 
# A) Separe a base em X(Features) e Y(Target)
# 
# B) Separe a base em treino e teste.
# 

# %%
#seu código aqui

# %% [markdown]
# # 4 - Modelagem
# 
# A) Inicie e treine o modelo de Random Forest
# 
# B) Aplique a base de teste o modelo.
# 

# %%
#seu código aqui

# %% [markdown]
# # 5 - Avaliação
# 
# A) Avalie as principais métricas da Claissificação e traga insights acerca do resultado, interprete os valores achados.
# 
# B) Você nota que o modelo teve dificuldade para prever alguma classe? Se sim, acredita que tenha relação com o balanceamento dos dados? Explique.
# 

# %%
#seu código aqui

# %% [markdown]
# # 5 - Melhorando os Hyperparametros
# 
# A) Defina o Grid de parametros que você quer testar
# 
# B) Inicie e Treine um novo modelo utilizando o random search.
# 
# C) Avalie os resultados do modelo.
# 
# D) Você identificou melhorias no modelo após aplicar o random search? Justifique.
# 
# 
# ps. Essa parte da atividade demorará um pouco para rodar!

# %%
#seu código aqui

# %% [markdown]
# # 6 - Chegando a perfeição
# 
# Baseado em tudo que você já aprendeu até agora, quais outras técnicas você acredita que poderiam ser aplicadas ao modelo para melhorar ainda mais suas previsões?


