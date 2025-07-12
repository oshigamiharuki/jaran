#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


jalan_df = pd.read_csv('jalan.csv')


# In[3]:


st.title('サーチ')
価格8_limit = st.slider('最低宿泊価格の上限',min_value = 4000,
                      max_value = 40000,step = 200,value = 6000)
score_limit = st.slider('人気スコアの下限',min_value=0.0,
                        max_value = 35.0,step = 2.0,value = 5.0)


# In[5]:


filtered_df = jalan_df[
    (jalan_df['価格8']<=価格8_limit)&
    (jalan_df['score']>=score_limit)
]


# In[7]:


fig = px.scatter(
    filtered_df,
    x = 'score',
    y = '価格8',
    hover_data = ['タイトル','概要','概要9'],
    title = '人気スコアと最低宿泊価格の散布図'
)
st.plotly_chart(fig)


# In[12]:


selected_yado = st.selectbox('気になる宿を選んで詳細を確認する',filtered_df['タイトル'])

if selected_yado:
    url = filtered_df[filtered_df['タイトル'] == selected_yado]['タイトルURL'].values[0]
    st.markdown(f"{selected_yado}のページへ移動{url}",unsafe_allow_html=True)


# In[ ]:




