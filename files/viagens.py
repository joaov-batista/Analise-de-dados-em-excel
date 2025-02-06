import pandas as pd
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(layout='wide', page_title='Análise de Viagens', page_icon='✈️')

# Função para carregar os dados
@st.cache_data
def carregar_dados(arquivo):
    return pd.read_csv(arquivo, sep=";", encoding="latin1")

# Carregamento do dataset
dados = carregar_dados("2024_Viagem.csv")

# Sidebar - Filtro de Cargo
cargos = dados["Cargo"].unique()
cargo = st.sidebar.selectbox('Selecione o Cargo', cargos)
df_cargo = dados[dados["Cargo"] == cargo]

# Sidebar - Filtro de Nome do Viajante
nomes_filtrados = df_cargo["Nome"].unique()
nome_viajante = st.sidebar.selectbox('Nome do Viajante', nomes_filtrados)
df_viajante = df_cargo[df_cargo["Nome"] == nome_viajante]

# Sidebar - Filtro de Destino
destinos_filtrados = df_viajante["Destinos"].unique()
destino = st.sidebar.selectbox('Destino da Viagem', destinos_filtrados)
df_destino = df_viajante[df_viajante["Destinos"] == destino]

# Sidebar - Filtro por ID da Viagem
identificador_pesquisa = st.sidebar.text_input('Pesquisar por ID da Viagem')
if identificador_pesquisa:
    df_destino = dados[dados["Identificador do processo de viagem"].astype(str) == identificador_pesquisa]
    if df_destino.empty:
        st.error("Nenhuma viagem encontrada para este ID.")

# Exibição dos dados filtrados
if df_destino.empty:
    st.error("Nenhuma viagem encontrada para os filtros selecionados.")
else:
    # Extração dos dados principais
    identificador_viagem = df_destino["Identificador do processo de viagem"].iloc[0]
    numero_proposta = df_destino["Número da Proposta (PCDP)"].iloc[0]
    situacao_viagem = df_destino["Situação"].iloc[0]
    urgencia_destino = df_destino["Viagem Urgente"].iloc[0]
    justificativa_urgencia = df_destino["Justificativa Urgência Viagem"].iloc[0]
    orgao_superior = df_destino["Nome do órgão superior"].iloc[0]
    orgao_solicitante = df_destino["Nome órgão solicitante"].iloc[0]
    data_inicio = df_destino["Período - Data de início"].iloc[0]
    data_fim = df_destino["Período - Data de fim"].iloc[0]
    motivo_viagem = df_destino["Motivo"].iloc[0]

    # Função para converter valores monetários corretamente
    def convert_to_float(value):
        try:
            return float(str(value).replace(".", "").replace(",", "."))
        except:
            return 0.0

    # Extração e conversão dos valores monetários
    valor_diarias = convert_to_float(df_destino["Valor diárias"].iloc[0])
    valor_passagens = convert_to_float(df_destino["Valor passagens"].iloc[0])
    valor_devolucao = convert_to_float(df_destino["Valor devolução"].iloc[0])
    valor_outros_gastos = convert_to_float(df_destino["Valor outros gastos"].iloc[0])
    custo_total = valor_diarias + valor_passagens + valor_devolucao + valor_outros_gastos

    # Exibição das informações
    st.title(f"📌 Análise da Viagem - {identificador_viagem}")
    st.subheader(f"🧑‍💼 {nome_viajante} ({cargo}) - Destino: {destino}")
    st.divider()

    # Identificação da Viagem
    st.subheader("📌 Identificação da Viagem")
    col1, col2, col3 = st.columns(3)
    col1.metric("ID", str(identificador_viagem))
    col2.metric("Proposta (PCDP)", numero_proposta)
    col3.metric("Situação", situacao_viagem)
    st.divider()

    # Urgência
    st.subheader("⚠️ Urgência da Viagem")
    st.write(f"**Viagem Urgente:** {urgencia_destino}")
    st.write(f"**Justificativa:** {justificativa_urgencia}")
    st.divider()

    # Órgão Responsável
    st.subheader("🏛️ Órgão Responsável")
    col1, col2 = st.columns(2)
    col1.metric("Órgão Superior", orgao_superior)
    col2.metric("Órgão Solicitante", orgao_solicitante)
    st.divider()

    # Detalhes da Viagem
    st.subheader("🛫 Detalhes da Viagem")
    col1, col2, col3 = st.columns(3)
    col1.metric("Início", data_inicio)
    col2.metric("Fim", data_fim)
    col3.metric("Destino", destino)
    st.write(f"**Motivo:** {motivo_viagem}")
    st.divider()

    # Custos da Viagem
    st.subheader("💰 Custos da Viagem")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Diárias", f"R$ {valor_diarias:,.2f}")
    col2.metric("Passagens", f"R$ {valor_passagens:,.2f}")
    col3.metric("Devolução", f"R$ {valor_devolucao:,.2f}")
    col4.metric("Outros Gastos", f"R$ {valor_outros_gastos:,.2f}")
    col5.metric("💵 Custo Total", f"R$ {custo_total:,.2f}")
    st.divider()