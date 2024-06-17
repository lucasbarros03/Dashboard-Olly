import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def ChartBar(df, column, title, x_label, fig_type = 'bar'):
    if filtro_var == None:
        fig = getattr(px,fig_type)(df, x = column, title = title, labels = {column:x_label, 'count':'Total'}) \
            .update_xaxes(categoryorder='total descending') \
            .update_traces(marker_color='rgb(221,110,28)')
    else:    
        fig = getattr(px,fig_type)(df_filtro, x = column, title = title, labels = {column:x_label, 'count':'Total'}) \
            .update_xaxes(categoryorder='total descending') \
            .update_traces(marker_color='rgb(221,110,28)')
    return fig

def ChartPie(df, column, title, fig_type = 'pie'):
    if filtro_var == None:
        fig = getattr(px, fig_type)(df, names = column, title=title, color = column, color_discrete_map = {'Casado': 'rgb(221,110,28)', 'Solteiro': 'rgb(184,138,117)', 'Não informado': 'rgb(52,46,48)'}) \
            .update_xaxes(categoryorder = 'total descending')
    else:
        fig = getattr(px, fig_type)(df_filtro, names = column, title=title, color = column, color_discrete_map = {'Casado': 'rgb(221,110,28)', 'Solteiro': 'rgb(184,138,117)', 'Não informado': 'rgb(52,46,48)'}) \
            .update_xaxes(categoryorder = 'total descending')
    return fig

def ChartHist(df, column, column_color, title, x_label, fig_type = 'histogram'):
    if filtro_var == None:
        fig = getattr(px, fig_type)(df, x = column, color = column_color, color_discrete_map = {'Masculino': 'rgb(221,110,28)', 'Feminino': 'rgb(184,138,117)', 'Não informado': 'rgb(52,46,48)'}, title = title, labels = {column:x_label, 'count':'Total'}) \
        .update_layout(bargap = 0.1)
    else:
        fig = getattr(px, fig_type)(df_filtro, x = column, color = column_color, color_discrete_map = {'Masculino': 'rgb(221,110,28)', 'Feminino': 'rgb(184,138,117)', 'Não informado': 'rgb(52,46,48)'}, title = title, labels = {column:x_label, 'count':'Total'}) \
        .update_layout(bargap = 0.1)
    return fig


st.set_page_config(
    page_title = 'Olly Dashboard',
    page_icon= ':bar_chart:',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.header('Olly DashBoard')

df = pd.read_excel('Dados enriquecidos projeto.xlsx')
df = df[df['tem_carro'] != 'Não']
df = df.dropna()

opcoes = {
    'Cor': 'cor',
    'Esporte': 'esporte',
    'Estado Civil': 'estcivil',
    'Filme': 'filme',
    'Gênero': 'genero',
    'Idade': 'idade',
    'Música': 'musica',
    'Região': 'regiao',
    'Tipo do Veículo': 'tipo'}

st.sidebar.image('image_olly_.png')

opt = st.sidebar.radio('Por qual tipo de variável deseja filtrar?', list(opcoes.keys()))
filtro_col = opcoes[opt]
filtro_var = st.sidebar.selectbox(f'Qual {opt.lower()}',df[filtro_col].sort_values().unique(), index= None, placeholder=f'Selecione o {opt.lower()}', help='Selecione o filtro que deseja')
df_filtro = df[df[filtro_col] == filtro_var]

col1, col2 ,col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Chart 1
fig_car = ChartBar(df, 'tipo', 'Total de carros', 'Tipos Carros')
col1.plotly_chart(fig_car, use_container_width=True)

# Chart 2
fig_consi = ChartBar(df, 'se_considera', 'Total de como se considera', 'Se considera')
col2.plotly_chart(fig_consi, use_container_width=True)

# Chart 3
fig_idade = ChartHist(df, 'idade', 'genero', 'Total de Idade', 'Idades')
col3.plotly_chart(fig_idade, use_container_width=True)

# Chart 4
fig_reg = ChartBar(df, 'regiao', 'Total por região', 'Regiões')
col4.plotly_chart(fig_reg, use_container_width=True)

# Chart 5
fig_estciv = ChartPie(df, 'estcivil', 'Total Estado Civil')
col5.plotly_chart(fig_estciv, use_container_width=True)

# Chart 6
fig_fds = ChartBar(df, 'fds', 'Total Fim de Semana', 'Fim de Semana')
col6.plotly_chart(fig_fds, use_container_width=True)