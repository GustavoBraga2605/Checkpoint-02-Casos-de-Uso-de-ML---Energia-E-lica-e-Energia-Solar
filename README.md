# Checkpoint 02 Casos de Uso de ML - Energia Eólica e Energia-Solar

## Integrantes:
Gustavo Cordeiro Braga / RM: 562247

Murilo Justino Arcanjo / RM: 565470

Rafael Quattrer Dalla Costa / RM: 562052

## Sobre

Este projeto tem como objetivo aplicar técnicas de **Machine Learning** em diferentes bases de dados relacionadas à geração e consumo de energia, tanto solar quanto eólica, bem como estabilidade de redes elétricas.  

## Estrutura do Projeto

- `SolarPrediction.csv` → Previsão de geração solar com base em condições climáticas.  
- `T1.csv` → Produção de energia em turbina eólica.  
- `smart_grid_stability_augmented.csv` → Estabilidade de redes inteligentes de energia.  
- `energydata_complete.csv` → Consumo energético em ambiente doméstico.  
- `README.md` → Este documento, com explicações detalhadas.

## Descrição dos Datasets

### SolarPrediction.csv
Contém medições climáticas e solares para prever a radiação e geração de energia solar.  
**Colunas principais:**
- `UNIXTime` → Carimbo de tempo em formato UNIX.  
- `Data`, `Time` → Data e horário da medição.  
- `Radiation` → Radiação solar medida.  
- `Temperature` → Temperatura ambiente.  
- `Pressure` → Pressão atmosférica.  
- `Humidity` → Umidade relativa do ar.  
- `WindDirection(Degrees)` → Direção do vento em graus.  
- `Speed` → Velocidade do vento.  
- `TimeSunRise`, `TimeSunSet` → Horários de nascer e pôr do sol.  

### T1.csv
Dados reais de uma turbina eólica com medições de potência e condições do vento.  
**Colunas principais:**
- `Date/Time` → Data e hora da medição.  
- `LV ActivePower (kW)` → Potência ativa gerada (kW).  
- `Wind Speed (m/s)` → Velocidade do vento em metros por segundo.  
- `Theoretical_Power_Curve (KWh)` → Potência teórica esperada.  
- `Wind Direction (°)` → Direção do vento em graus.  

### smart_grid_stability_augmented.csv
Simulações sobre estabilidade de redes inteligentes de energia elétrica.  
**Colunas principais:**
- `tau1`, `tau2`, `tau3`, `tau4` → Constantes de tempo de diferentes geradores.  
- `p1`, `p2`, `p3`, `p4` → Potências ativas dos geradores.  
- `g1`, `g2`, `g3`, `g4` → Ganhos de controle dos geradores.  
- `stab` → Indicador numérico de estabilidade.  
- `stabf` → Classe de estabilidade (stable / unstable).  

### energydata_complete.csv
Base com consumo de energia em uma residência e variáveis ambientais internas e externas.  
**Colunas principais:**
- `date` → Data e hora da medição.  
- `Appliances` → Consumo de energia de eletrodomésticos (Wh).  
- `lights` → Consumo de energia da iluminação (Wh).  
- `T1` a `T9` → Temperaturas internas em diferentes cômodos.  
- `RH_1` a `RH_9` → Umidades relativas correspondentes aos cômodos.  
- `T_out`, `RH_out` → Temperatura e umidade externas.  
- `Windspeed`, `Visibility`, `Tdewpoint` → Variáveis meteorológicas.  
- `rv1`, `rv2` → Variáveis aleatórias adicionadas para validação.  

## Objetivo
A partir destes dados, será possível:  
- Treinar modelos de **regressão** e **classificação**.  
- Prever geração e consumo de energia.  
- Avaliar estabilidade de redes elétricas.  
- Analisar o impacto de variáveis ambientais na eficiência energética.  

