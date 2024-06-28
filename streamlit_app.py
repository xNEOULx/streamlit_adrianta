import streamlit as st 
import pandas as pd 
import requests
from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.write('Minimal Example')

if __name__ == '__main__' : 
  main()

def main() : 
  st.header('Halaman Streamlit Adrianta Ras Sembiring')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()

def main() : 
  st.write('Contoh dataframe')
  st.dataframe(house)
  st.write('Contoh JSON')
  st.write('Menampilkan Dataframe dengan St AgGrid')
  AgGrid(house)
  st.table([x for x in range(1,5)])
if __name__ == '__main__' : 
  main()
