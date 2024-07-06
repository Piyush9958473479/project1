import streamlit as st
st.title('voting eligibility app')
st.header('Enter Your Name')
s=st.text_input('Name:')
st.header('Gender')
st.radio('Specify Your Gender',options=['m','f'])
st.header('Enter your age')
p=st.number_input('Age:')
if p<18:
    st.write('sorry')
else:
    st.write('You Are Eligible')
    st.balloons()

