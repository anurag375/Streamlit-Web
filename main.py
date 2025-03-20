import streamlit as st
import pandas as pd
import seaborn as sns

#@st.cache_data
df = sns.load_dataset('iris')
df

st.write('Hellow World!')
st.title('My_Title')
st.image("./bird.png")


st.number_input('Enter a number: ', 0,5)
st.date_input('Enter your birth date')
st.slider('Slide it', 0,100,25)
# st.file_uploader("Upload a CSV")

with st.sidebar:
    st.text_input('Filter by name')
    st.selectbox('Sort by', ['a-z', 'A-Z'])
    st.file_uploader('Upload a csv')

# st.write("Most objects") # df, err, func, keras!
