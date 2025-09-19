import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
 
domain = Domain([ContinuousVariable("age"),
                 ContinuousVariable("height"),
                 DiscreteVariable("gender", values=("M", "F"))])
arr = np.array([
  [25, 186, 0],
  [30, 164, 1]])
out_data = Table.from_numpy(domain, arr)
 
 
# Supondo que você tenha "predictions" e "true values"
y_true = in_data.Y  # Valores reais
y_rf = in_data.metas[:, 0]  # Random Forest
y_lr = in_data.metas[:, 1]  # Linear Regression
y_tree = in_data.metas[:, 2]  # Tree
y_knn = in_data.metas[:, 3]  # kNN
 
models = {
    "Random Forest": y_rf,
    "Linear Regression": y_lr,
    "Tree": y_tree,
    "kNN": y_knn,
}
 
# Armazenar as métricas para comparar
model_scores = {}
 
for name, y_pred in models.items():
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # Guardar as métricas para comparar os modelos
    model_scores[name] = {
        "RMSE": rmse,
        "MAE": mae,
        "R²": r2
    }
 
    # Exibir as métricas do modelo
    print(f"\n{name}:")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  MAE:  {mae:.2f}")
    print(f"  R²:   {r2:.3f}")
 
# Identificar o melhor e pior desempenho
best_model = min(model_scores, key=lambda x: model_scores[x]["RMSE"])  # Melhor modelo baseado no RMSE (menor erro)
worst_model = max(model_scores, key=lambda x: model_scores[x]["RMSE"])  # Pior modelo baseado no RMSE (maior erro)
 
# Exibir o melhor e pior modelo
print("\nResumo:")
print(f"O modelo com o melhor desempenho é o **{best_model}** com RMSE = {model_scores[best_model]['RMSE']:.2f}, MAE = {model_scores[best_model]['MAE']:.2f}, R² = {model_scores[best_model]['R²']:.3f}.")
print(f"O modelo com o pior desempenho é o **{worst_model}** com RMSE = {model_scores[worst_model]['RMSE']:.2f}, MAE = {model_scores[worst_model]['MAE']:.2f}, R² = {model_scores[worst_model]['R²']:.3f}.")
 
# Descrição dos resultados
print("\nDescrição dos Resultados:")
print("""
Neste exercício, foram utilizados quatro modelos de regressão para prever o consumo de energia de eletrodomésticos com base em variáveis ambientais.
O modelo de **Árvore de Decisão** apresentou o melhor desempenho, com RMSE = 29.16, MAE = 10.48 e R² = 0.919, indicando boa capacidade preditiva.
Em contraste, o modelo de **Regressão Linear** apresentou o pior desempenho, com RMSE = 93.69, MAE = 52.85 e R² = 0.165, indicando que ele não conseguiu capturar bem os padrões dos dados.
Com base nas métricas de **RMSE**, **MAE** e **R²**, podemos concluir que modelos não lineares, como a **Árvore de Decisão**, são mais eficazes para esse tipo de dado, enquanto o modelo de **Regressão Linear** apresentou um desempenho insatisfatório.
""")
