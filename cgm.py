import matplotlib.pyplot as plt
import streamlit as st




fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 형태를 선택하시오',['-',':','-.','--'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오',['o','^','s','p'])


fig, ax = plt.subplots()

col = st.columns(3)
with col[0]:
    a = st.number_input('insert a', step = 1)
with col[1]:
    b = st.number_input('insert b', step = 1)    
with col[2]:
    c = st.number_input('insert c', step = 1)
with col[2]:
    d = st.number_input('insert d', step = 100)


x = []
y2 = []
for i in range(-29,30,3):
    x.append(i)
    y2.append(d/i)


y = []
for i in x:
    y.append(a*i**2 + b*i + c)

plt.plot(x,y)

st.pyplot(fig)

plt.plot(x,y,color=c1, linestyle=s1, marker=m1)

st.pyplot(fig)

import sys
sys.exit()





