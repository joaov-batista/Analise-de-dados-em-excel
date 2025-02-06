# Análise de Viagens de Servidores Públicos

Este projeto foi desenvolvido em Python como uma iniciativa para praticar e aprimorar habilidades de programação e análise de dados. Utilizando as bibliotecas **Streamlit**, **Pandas** e **Plotly**, o sistema realiza a análise de viagens de servidores públicos, considerando custos como diárias, passagens, devoluções e outros gastos. A aplicação fornece **gráficos interativos** e **filtros dinâmicos**, permitindo uma exploração detalhada dos dados relacionados às viagens, cargos, gastos e destinos.

## Funcionalidades
- **Filtros Interativos**: Filtro por cargo, nome do viajante, destino da viagem e valor máximo gasto.
- **Visualização de Gráficos**: Exibição de gráficos interativos sobre os cargos e funcionários que mais gastaram, mais viajaram, além da distribuição dos custos por tipo de despesa.
- **Exibição de Detalhes**: Detalhamento completo das viagens, incluindo dados sobre custos, órgãos responsáveis e justificativas de urgência.
- **Análise de Custos**: Visão detalhada do custo total das viagens e distribuição dos gastos.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Streamlit**: Biblioteca para criação de interfaces web interativas.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Biblioteca para visualização interativa de gráficos.

## Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina. Em seguida, instale as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

### Iniciar a aplicação Streamlit
Para rodar a aplicação, utilize o seguinte comando:

```bash
streamlit run app.py
```

## Estrutura do Projeto

```
/
├── app.py              # Código principal que roda a aplicação Streamlit
├── 2024_Viagem.csv     # Dataset de exemplo com informações sobre as viagens dos servidores públicos
├── requirements.txt    # Arquivo com as dependências necessárias para rodar o projeto
```

## Demonstração
```
https://youtu.be/LOPacISyt-I
```

## Observações
- O arquivo **2024_Viagem.csv** deve estar na mesma pasta que o **.py** ou ser especificado corretamente no código.
- Certifique-se de que as colunas e os dados estejam no formato esperado para garantir que a aplicação funcione corretamente.

---

Projeto desenvolvido para fins de aprendizado e aprimoramento em análise de dados e desenvolvimento web com Python.

