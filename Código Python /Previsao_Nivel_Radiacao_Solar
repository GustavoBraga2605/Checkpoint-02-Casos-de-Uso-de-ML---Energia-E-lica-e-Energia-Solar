import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carregar dados
file_path = "/content/SolarPrediction.csv"
df = pd.read_csv(file_path)

# 2. Criar coluna datetime unindo Data e Time
df['Datetime'] = pd.to_datetime(df['Data'] + ' ' + df['Time'])

# 3. Verificar dados faltantes
print("Valores faltantes por coluna:")
print(df.isnull().sum())

# 4. Selecionar features e target
features = df[['Radiation', 'Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)']]
target = df['Speed']

# 5. Dividir treino e teste
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 6. Definir os modelos
models = {
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'SVM': SVR()
}

# 7. Treinar, prever e avaliar cada modelo
for name, model in models.items():
    print(f"\nTreinando e avaliando: {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")

    # Mostrar as 5 primeiras previsões comparadas com o real
    comparison = pd.DataFrame({"Real": y_test.values, "Previsto": y_pred})
    print(comparison.head())
