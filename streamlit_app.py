import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid

# baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 

# membuat text
  st.write('Belajar Streamlit di Pusdiklat KU')
  st.write('Minimal Example')

# membuat header, subheader, markdown
  st.header('Halaman Streamlit Adrianta Ras Sembiring')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

# menampilkan dataframe
  st.write('Contoh dataframe')
  st.dataframe(house)

# menampilkan metrics
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# menampilkan buttons
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
      st.write('Anda Setuju')
    
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)

# menampilkan slider
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)

# menampilkan input typing

  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

if __name__ == '__main__' : 
  main()
