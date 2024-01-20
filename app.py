import streamlit as st
st.title('demo app')
st.write('this is a demo app')

  with st.sidebar:
  st.write('this is a sidebar')
  col1,col2 = st.columns(2)
  with col1:
      a = st.number_input('enter a value',value=10)
      b = st.text_input('enter a text')
sub = st.button(label='submit')
if sub:
  st.write(a)
  st.write(b)
print(a)
