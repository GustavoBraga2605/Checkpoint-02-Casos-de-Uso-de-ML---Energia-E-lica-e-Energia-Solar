import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# 1. Caminho para o seu arquivo CSV
file_path = "/content/T1.csv"

# 2. Ler o arquivo (tentando com separador padrão ou ajustando se necessário)
df = pd.read_csv(file_path)

# 3. Remover espaços extras dos nomes das colunas (se houver)
df.columns = df.columns.str.strip()

# 4. Visualizar as colunas para garantir que estão corretas
print("Colunas disponíveis:", df.columns)

# 5. Converter a coluna Date/Time (opcional)
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format="%d %m %Y %H:%M")

# 6. Selecionar features e target
features = df[['Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)', 'Wind Direction (°)']]
target = df['LV ActivePower (kW)']

# 7. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 8. Normalizar os dados para o SVM
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 9. Definir os modelos
models = {
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'SVM': SVR()
}

# 10. Treinar e avaliar os modelos
for name, model in models.items():
    print(f"\n=== {name} ===")

    # Usar dados normalizados apenas no SVM
    if name == 'SVM':
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    # Avaliação
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse:.2f}")
    print(f"R²: {r2:.2f}")

    # Comparar real vs previsto
    comparison = pd.DataFrame({'Real': y_test.values, 'Previsto': y_pred})
    print(comparison.head())
