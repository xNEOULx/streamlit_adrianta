import streamlit as st 
import pandas as pd 
from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 

  st.write('Belajar Streamlit di Pusdiklat KU')
  
  st.write('Minimal Example')

if __name__ == '__main__' : 
  main()

def main() : 
  st.header('Halaman Streamlit Adrianta Ras Sembiring')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

  st.write('Contoh dataframe')
  st.dataframe(house)
  
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

  st.write('Menampilkan Dataframe dengan St AgGrid')
  AgGrid(house)
  st.table([x for x in range(1,5)])

  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
      st.write('Anda Setuju')

if __name__ == '__main__' : 
  main()
