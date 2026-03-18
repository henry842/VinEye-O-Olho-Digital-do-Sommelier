# 🍷 VinEye — O Olho Digital do Sommelier

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Random Forest](https://img.shields.io/badge/Random_Forest-Scikit--Learn-F7931E?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-00d4ff?style=flat-square)

**Previsão de qualidade de vinhos tintos com Random Forest e análise de correlações químicas.**

</div>

---

## 📋 Sobre o Projeto

Utilizando o famoso dataset de vinhos tintos portugueses, este projeto treina um modelo para **prever a nota de qualidade** de um vinho com base em suas propriedades físico-químicas — como se fosse um sommelier digital.

---

## 🔬 Análise Exploratória

Correlações investigadas:
- `alcohol` × `quality` — maior teor alcoólico tende a notas maiores
- `volatile acidity` × `quality` — acidez volátil reduz qualidade percebida
- `sulphates` × `quality` — sulfatos em quantidade adequada melhoram a conservação

---

## 🤖 Modelagem

| Etapa | Detalhe |
|-------|---------|
| Baseline | Regressão Logística |
| Modelo Final | Random Forest Classifier |
| Otimização | GridSearchCV para hiperparâmetros |
| Avaliação | Acurácia, F1-Score, Matriz de Confusão |

### Hiperparâmetros otimizados:
- `n_estimators` — número de árvores
- `max_depth` — profundidade máxima
- `min_samples_split` — mínimo de amostras para split

---

## 📊 Features Mais Importantes

1. `alcohol` — teor alcoólico
2. `sulphates` — nível de sulfatos
3. `volatile acidity` — acidez volátil
4. `citric acid` — ácido cítrico
5. `total sulfur dioxide`

---

## 🛠️ Tecnologias

- **Random Forest / Scikit-Learn**
- **GridSearchCV** — otimização de hiperparâmetros
- **Pandas / NumPy / Seaborn**
- **Jupyter Notebook**

---

## 🚀 Como Executar

```bash
git clone https://github.com/henry842/VinEye-O-Olho-Digital-do-Sommelier.git
cd VinEye-O-Olho-Digital-do-Sommelier
pip install -r requirements.txt
jupyter notebook vineye.ipynb
```

---

<div align="center">
  <a href="https://github.com/henry842">👤 henry842</a> •
  <a href="https://github.com/henry842?tab=repositories">📂 Outros projetos</a>
</div>

---
---
