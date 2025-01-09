import streamlit as st
import pandas as pd
import plotly.express as px

# Ler o arquivo CSV em um DataFrame
car_data = pd.read_csv('/Users/brunabiazolli/Desktop/applesson/data/vehicles_us.csv')

# Criar um cabeçalho para o aplicativo
st.header('Análise de Dados de Vendas de Carros Usados')

# Botões para criar gráficos
st.subheader('Selecione um gráfico para exibir:')
hist_button = st.button('Criar Histograma')
scatter_button = st.button('Criar Gráfico de Dispersão')

# Lógica para o botão de histograma
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de vendas de carros usados.')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribuição de Quilometragem")
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para o botão de gráfico de dispersão
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados.')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Preço vs Quilometragem")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Alternativa: Usar caixas de seleção
st.subheader('Ou selecione usando caixas de seleção:')
show_hist = st.checkbox('Mostrar Histograma')
show_scatter = st.checkbox('Mostrar Gráfico de Dispersão')

# Lógica para a caixa de seleção de histograma
if show_hist:
    st.write('Criando um histograma para o conjunto de dados de vendas de carros usados.')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribuição de Quilometragem")
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para a caixa de seleção de gráfico de dispersão
if show_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados.')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Preço vs Quilometragem")
    st.plotly_chart(fig_scatter, use_container_width=True)
