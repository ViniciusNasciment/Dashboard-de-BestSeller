import streamlit as st
import pandas as pd
import plotly.express as px
import openai

st.set_page_config(layout="wide")

# CARREGAMENTOS DE DADOS
df_reviews = pd.read_csv('DashBoard Livros + CHATGPT/datasets/customer reviews.csv')
df_top100_books = pd.read_csv('DashBoard Livros + CHATGPT/datasets/Top-100 Trending Books.csv')
 
# TITULO DAS PAGINAS
st.title("Lista dos BestSeller Amazon")
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

st.sidebar.image('DashBoard Livros + CHATGPT/imgbin_amazon-logo-png.png', use_column_width=True)

with st.sidebar:
    seller_selected = st.radio("**Listas De Vendedores**", ["Rebecca Yarros", "Britney Spears", "Matthew Perry", "Unknown"])

# Filtro por vendedor
df_books = df_top100_books[df_top100_books['author'] == seller_selected]

max_price = st.sidebar.slider("**Filtro de Preço**", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

# Figuras
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["year of publication"])

# Colunas
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)


     
