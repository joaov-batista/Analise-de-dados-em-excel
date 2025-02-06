import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Análise de Viagens",
    page_icon="📊",
    layout="wide"
)

# Carregar os dados
@st.cache_data
def carregar_dados():
    dados = pd.read_csv("2024_Viagem.csv", sep=";", encoding="latin1")
    return dados

dados = carregar_dados()

# Manter apenas colunas relevantes
dados = dados[["Destinos", "Valor diárias", "Valor passagens", "Valor devolução", "Valor outros gastos", "Cargo", "Nome", "Identificador do processo de viagem"]]

# Função para converter valores numéricos corretamente
def convert_to_float(value):
    try:
        return float(str(value).replace(".", "").replace(",", "."))
    except:
        return 0.0

# Convertendo colunas numéricas
dados["Valor diárias"] = dados["Valor diárias"].apply(convert_to_float)
dados["Valor passagens"] = dados["Valor passagens"].apply(convert_to_float)
dados["Valor devolução"] = dados["Valor devolução"].apply(convert_to_float)
dados["Valor outros gastos"] = dados["Valor outros gastos"].apply(convert_to_float)
dados["Custo Total"] = dados["Valor diárias"] + dados["Valor passagens"] + dados["Valor devolução"] + dados["Valor outros gastos"]

# Adicionando filtros interativos na barra lateral
st.sidebar.header("Filtros")

# Filtro por cargo
cargos_disponiveis = ["Todos"] + sorted(dados["Cargo"].dropna().unique())
cargo_selecionado = st.sidebar.selectbox("Filtrar por Cargo", options=cargos_disponiveis, index=0)
dados_filtrados = dados if cargo_selecionado == "Todos" else dados[dados["Cargo"] == cargo_selecionado]

# Filtro por valor máximo gasto
valor_max = st.sidebar.slider("Filtrar por Custo Total", min_value=dados_filtrados["Custo Total"].min(), max_value=dados_filtrados["Custo Total"].max(), value=dados_filtrados["Custo Total"].max())
dados_filtrados = dados_filtrados[dados_filtrados["Custo Total"] <= valor_max]

# Exibir tabela dos dados filtrados
st.subheader("📋 Dados Filtrados")
st.dataframe(dados_filtrados)

# Layout em colunas
col1, col2 = st.columns(2)

# Gráfico: Cargo que mais gastou
with col1:
    st.subheader("💸 Cargos que mais gastaram")
    gastos_por_cargo = dados_filtrados.groupby("Cargo")["Custo Total"].sum().nlargest(5)
    fig = px.bar(gastos_por_cargo, x=gastos_por_cargo.index, y=gastos_por_cargo, title="Top 5 Cargos que mais Gastaram")
    st.plotly_chart(fig)

# Gráfico: Funcionário que mais gastou por cargo
with col2:
    st.subheader("👤 Funcionário que mais gastou em cada cargo")
    func_mais_gastou = dados_filtrados.loc[dados_filtrados.groupby("Cargo")["Custo Total"].idxmax()][["Nome", "Cargo", "Custo Total"]].nlargest(5, "Custo Total")
    fig = px.bar(func_mais_gastou, x="Nome", y="Custo Total", color="Cargo", title="Top 5 Funcionários que mais Gastaram")
    st.plotly_chart(fig)

col3, col4 = st.columns(2)

# Gráfico: Cargo que mais viajou
with col3:
    st.subheader("✈️ Cargos que mais viajaram")
    viagens_por_cargo = dados_filtrados["Cargo"].value_counts().nlargest(5)
    fig = px.bar(viagens_por_cargo, x=viagens_por_cargo.index, y=viagens_por_cargo, title="Top 5 Cargos que mais Viajaram")
    st.plotly_chart(fig)

# Gráfico: Pessoa que mais viajou por cargo
with col4:
    st.subheader("🚶 Pessoas que mais viajaram por cargo")
    func_mais_viajou = dados_filtrados.groupby(["Cargo", "Nome"]).size().reset_index(name="Quantidade de Viagens")
    func_mais_viajou = func_mais_viajou.loc[func_mais_viajou.groupby("Cargo")["Quantidade de Viagens"].idxmax()].nlargest(5, "Quantidade de Viagens")
    fig = px.bar(func_mais_viajou, x="Nome", y="Quantidade de Viagens", color="Cargo", title="Top 5 Pessoas que mais Viajaram")
    st.plotly_chart(fig)

col5, _ = st.columns([1, 1])

# Gráfico: Gasto médio por tipo de despesa
with col5:
    st.subheader("📊 Gasto médio por tipo de despesa")
    gasto_medio = dados_filtrados[["Valor diárias", "Valor passagens", "Valor devolução", "Valor outros gastos"]].mean()
    fig = px.pie(gasto_medio, values=gasto_medio, names=gasto_medio.index, title="Distribuição Média dos Gastos por Viagem")
    st.plotly_chart(fig)
