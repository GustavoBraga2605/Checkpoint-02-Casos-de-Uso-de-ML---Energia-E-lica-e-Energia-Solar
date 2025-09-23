import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
 
domain = Domain([ContinuousVariable("age"),
                 ContinuousVariable("height"),
                 DiscreteVariable("gender", values=("M", "F"))])
arr = np.array([
  [25, 186, 0],
  [30, 164, 1]])
out_data = Table.from_numpy(domain, arr)
 
 
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
 
import numpy as np
 
# Valores reais (classe verdadeira)
 
y_true = np.array(in_data.Y)
 
resultados = []
 
# Percorre todas as colunas de predição (cada modelo)
 
for col in in_data.domain.class_vars:
 
    y_pred = np.array(in_data.get_column(col.name))
 
    acc = accuracy_score(y_true, y_pred)
 
    cm = confusion_matrix(y_true, y_pred)
 
    f1 = f1_score(y_true, y_pred, average="weighted")
 
    resultados.append((col.name, acc, f1, cm))
 
    print(f"\n=== Modelo: {col.name} ===")
 
    print(f"Acurácia: {acc:.4f}")
 
    print("Matriz de Confusão:")
 
    print(cm)
 
    print(f"F1-score: {f1:.4f}")
 
# Seleciona o melhor modelo pelo F1-score
 
melhor_modelo = max(resultados, key=lambda x: x[2])
 
print("\n===============================")
 
print(f"🏆 Melhor modelo: {melhor_modelo[0]}")
 
print(f"Acurácia: {melhor_modelo[1]:.4f}")
 
print(f"F1-score: {melhor_modelo[2]:.4f}")
 
print("Matriz de Confusão:")
 
print(melhor_modelo[3])
