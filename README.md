# Checkpoint 02 Casos de Uso de ML - Energia Eólica e Energia-Solar

## Integrantes:
Gustavo Cordeiro Braga / RM: 562247

Murilo Justino Arcanjo / RM: 565470

Rafael Quattrer Dalla Costa / RM: 562052

## Sobre

Este projeto corresponde ao **Checkpoint 02** da disciplina de Machine Learning. O foco é aplicar técnicas de ML para casos de uso em energia renovável, especificamente **energia eólica** e **energia solar**. Serão realizadas análises, modelos de previsão e comparações de desempenho entre métodos.

## Entrega

- Prazo de submissão: **inserir data/hora limite aqui**.  
- Formato: repositório GitHub completo com código, notebooks, dados utilizados e este README atualizado.  
- Os notebooks/scripts devem estar funcionando e documentados — comentar código, explicar cada etapa.  
- Opcional: incluir uma seção de conclusões com o que funcionou bem, o que poderia melhorar.  


## Dataset

- Fonte do(s) dado(s): *inserir origem do dataset* (ex: repositórios públicos, dados da disciplina, API etc.).  
- Descrição geral: informações meteorológicas, produção de energia solar/eólica, localização, períodos de medição etc.  
- Estrutura / Colunas principais:  
  | Coluna | Tipo | Descrição |
  |---|---|---|
  | `data` | Data / Timestamp | Momento da medição |
  | `vento_vel` | Numérico | Velocidade do vento (m/s) |
  | `vento_dir` | Categórico / Numérico | Direção do vento ou setor |
  | `radiacao` | Numérico | Irradiação solar (W/m² ou outra unidade) |
  | `temperatura` | Numérico | Temperatura ambiente (°C) |
  | `produção_solar` | Numérico | Produção de energia solar (kW ou unidade específica) |
  | `produção_eolica` | Numérico | Produção de energia eólica (kW ou unidade específica) |
  | … | … | … |

- Limpeza / tratamento esperado: tratar valores faltantes (missing), outliers, normalização ou padronização se necessário.  
