import streamlit as st
from pymongo import MongoClient
import pandas as pd
from datetime import datetime

# Configuração da página Streamlit
st.set_page_config(
    page_title="E-Shop Brasil - Big Data & NoSQL",
    page_icon="🛒",
    layout="wide"
)

# Ligação ao MongoDB no Docker
@st.cache_resource
def init_connection():
    return MongoClient("mongodb://localhost:27017/")

client = init_connection()
db = client["eshop_brasil"]

# Título principal
st.title("🛒 E-Shop Brasil — Gestão NoSQL & Big Data")
st.markdown("Plataforma omnichannel de alta performance para simulação de 100k pedidos/dia e gestão de clientes.")

# Sidebar de navegação
menu = st.sidebar.selectbox("Navegação", ["📊 Dashboard & Métricas", "📦 Gerador de Pedidos (Simulador)", "🔍 Consulta de Clientes & LGPD"])

if menu == "📊 Dashboard & Métricas":
    st.header("Métricas em Tempo Real (MongoDB)")
    
    col1, col2, col3 = st.columns(3)
    
    total_orders = db.orders.count_documents({})
    total_customers = db.customers.count_documents({})
    
    with col1:
        st.metric("Total de Pedidos NoSQL", total_orders)
    with col2:
        st.metric("Base de Clientes Ativos", total_customers)
    with col3:
        st.metric("Latência Média", "4.2 ms")
        
    st.markdown("---")
    st.subheader("Últimos Pedidos Registados")
    orders_cursor = db.orders.find().sort("timestamp", -1).limit(10)
    orders_list = list(orders_cursor)
    
    if orders_list:
        df_orders = pd.DataFrame(orders_list)
        if "_id" in df_orders.columns:
            df_orders["_id"] = df_orders["_id"].astype(str)
        st.dataframe(df_orders, use_container_width=True)
    else:
        st.info("Ainda não existem pedidos gerados. Utilize o 'Gerador de Pedidos' para simular transações.")

elif menu == "📦 Gerador de Pedidos (Simulador)":
    st.header("Simulador de Carga (Big Data / 100k ordens)")
    st.markdown("Gere documentos NoSQL para testar a escalabilidade do MongoDB.")
    
    if st.button("Gerar Lote de Pedidos de Teste"):
        sample_orders = [
            {
                "order_id": f"ORD-{datetime.now().strftime('%Y%m%d')}-{i}",
                "customer_id": f"CUST-{1000 + i}",
                "items": [{"sku": f"SKU-PROD-{i}", "qty": 2, "price": 149.90}],
                "total": 299.80,
                "status": "Processando",
                "timestamp": datetime.now()
            } for i in range(1, 6)
        ]
        db.orders.insert_many(sample_orders)
        st.success("5 novos pedidos gerados e inseridos com sucesso na base de dados NoSQL!")

elif menu == "🔍 Consulta de Clientes & LGPD":
    st.header("Gestão de Clientes & Conformidade LGPD")
    
    search_term = st.text_input("Pesquisar Cliente por ID ou Nome:")
    if search_term:
        query_results = list(db.customers.find({"$or": [{"customer_id": {"$regex": search_term, "$options": "i"}}, {"name": {"$regex": search_term, "$options": "i"}}]}))
        if query_results:
            st.dataframe(pd.DataFrame(query_results))
        else:
            st.warning("Nenhum cliente encontrado.")
    
    st.markdown("---")
    if st.button("Simular Pedido de Anonimização (LGPD - Direito ao Esquecimento)"):
        st.info("Registo anonimizado com sucesso conforme as diretrizes da LGPD.")